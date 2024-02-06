import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    console.log(reply);
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err}`);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');