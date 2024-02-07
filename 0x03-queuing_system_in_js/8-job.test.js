import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    kue.Job.rangeByState('inactive', 0, -1, 'asc', (err, jobs) => {
      jobs.forEach((job) => {
        job.remove();
      });
    });
  });

  afterEach(() => {
    queue.shutdown();
  });

  it('display a error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      kue.Job.rangeByState('inactive', 0, -1, 'asc', (err, jobs) => {
        expect(jobs).to.have.lengthOf(2);
        done();
      });
    }, 100);
  });
});
