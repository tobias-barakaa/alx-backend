// 7-job_processor.js

import kue from 'kue';
import { promisify } from 'util'

// Connect to Redis server
const queue = kue.createQueue();

// Array to contain blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
const sendNotification = async (phoneNumber, message, job, done) => {
  // Track progress
  job.progress(0, 100);
  
  // Check if phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    return done(error);
  }
  
  // Track progress
  job.progress(50, 100);
  
  // Log notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  
  // Simulate sending notification (you can replace this with actual sending logic)
  await promisify(setTimeout)(2000); // Simulating a delay
  
  // Complete the job
  done();
};

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

// Add jobs to the queue
const phoneNumbers = [
  '4153518743',
  '4153538781',
  '4153118782',
  '4153718781',
  '4159518782',
  '4158718781',
  '4153818782',
  '4154318781',
  '4151218782',
];

phoneNumbers.forEach((phoneNumber, index) => {
  queue.create('push_notification_code_2', {
    phoneNumber,
    message: `This is the code ${index + 1} to verify your account`,
  }).save();
});

// Log job status changes
queue.on('job enqueue', function(id, type){
  console.log(`Notification job ${id} 0% complete`);
}).on('job progress', function(id, progress){
  console.log(`Notification job ${id} ${progress}% complete`);
}).on('job failed', function(id, errorMessage){
  console.log(`Notification job ${id} failed: ${errorMessage}`);
}).on('job complete', function(id){
  console.log(`Notification job ${id} completed`);
});

// Log if there's any error with Redis
queue.on('error', function(err) {
  console.log('Error in Redis client:', err);
});
