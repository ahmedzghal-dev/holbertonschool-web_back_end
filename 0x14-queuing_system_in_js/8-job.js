function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
      throw new Error('Jobs is not an array');
    }
  
    jobs.forEach((job) => {
      const { phoneNumber, message } = job;
      const jobData = {
        phoneNumber,
        message,
      };
      
      const pushNotificationJob = queue.create('push_notification_code_3', jobData);
  
      pushNotificationJob.save((err) => {
        if (err) {
          console.log(`Notification job ${pushNotificationJob.id} failed: ${err}`);
        } else {
          console.log(`Notification job created: ${pushNotificationJob.id}`);
        }
      });
  
      pushNotificationJob.on('progress', (progress) => {
        console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
      });
  
      pushNotificationJob.on('complete', () => {
        console.log(`Notification job ${pushNotificationJob.id} completed`);
      });
  
      pushNotificationJob.on('failed', (err) => {
        console.log(`Notification job ${pushNotificationJob.id} failed: ${err}`);
      });
    });
  }
