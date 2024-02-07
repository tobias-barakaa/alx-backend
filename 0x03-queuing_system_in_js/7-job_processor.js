const kue = require('kue');
const queue = kue.createQueue();

// Create an empty array to store blacklisted phone numbers (replace with actual numbers if needed)
const blacklistedNumbers = [];

// Function to send notification, handling blacklisted numbers and logging progress
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0); // Track progress at 0%

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with a generic error message (without mentioning specific numbers)
    return done(new Error('Notification failed due to blacklisted phone number'));
  }

  job.progress(50); // Track progress at 50%

  console.log(`Sending notification to phone number: ${phoneNumber}, with message: ${message}`);

  // Simulate sending notification (replace with actual notification logic)
  setTimeout(() => {
    job.progress(100); // Track progress at 100%
    done(); // Mark job as completed
  }, 1000); // Simulate notification processing time
}

// Create a queue that processes "push_notification_code_2" jobs with concurrency 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data; // Retrieve data from the job
  sendNotification(phoneNumber, message, job, done);
});

// Example usage: Add jobs to the queue (replace with actual data)
queue.create('push_notification_code_2', {
  phoneNumber: '1234567890',
  message: 'This is a sample notification message.'
}).save();

queue.create('push_notification_code_2', {
  phoneNumber: '9876543210',
  message: 'Another sample notification message.'
}).save();

queue.process(); // Start processing jobs
