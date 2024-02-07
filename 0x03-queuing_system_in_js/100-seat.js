import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

const PORT = 1245;
let reservationEnabled = true;
let availableSeats = 50;

// Set the initial number of available seats to 50
reserveSeatAsync('available_seats', availableSeats);

app.get('/available_seats', async (req, res) => {
  try {
    const numberOfAvailableSeats = await getCurrentAvailableSeatsAsync('available_seats');
    res.json({ numberOfAvailableSeats });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/reserve_seat', async (req, res) => {
  try {
    if (!reservationEnabled) {
      return res.json({ status: 'Reservation are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
      if (err) {
        return res.json({ status: 'Reservation failed' });
      }
      res.json({ status: 'Reservation in process' });
    });

    job.on('complete', (result) => {
      console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
      console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/process', async (req, res) => {
  try {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
      const currentSeats = await getCurrentAvailableSeatsAsync('available_seats');
      if (currentSeats <= 0) {
        reservationEnabled = false;
        return done(new Error('Not enough seats available'));
      }

      availableSeats--;
      await reserveSeatAsync('available_seats', availableSeats);

      if (availableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
