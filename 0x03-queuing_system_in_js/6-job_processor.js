import kue from 'kue';
const queue = kue.createQueue();


function sendNotification(phoneNumber, message) {
  const jobData = {
    phoneNumber,
    message
  };

  const job = queue.create('push_notification_code', jobData)
    .save((err) => {
      if (err) {
        console.error('Notification job failed');
      } else {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  job.on('complete', () => {
    console.log('Notification job completed');
  });

  job.on('failed', () => {
    console.log('Notification job failed');
  });
}