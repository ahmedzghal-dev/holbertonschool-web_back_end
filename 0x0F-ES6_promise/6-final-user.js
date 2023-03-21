import { signUpUser } from './4-user-promise.js';
import { uploadPhoto } from './5-photo-reject.js';

export function handleProfileSignup(firstName, lastName, fileName) {
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  return Promise.allSettled([signUpPromise, uploadPromise])
    .then((results) => {
      return results.map((result) => {
        return {
          status: result.status,
          value: result.status === 'fulfilled' ? result.value : result.reason,
        };
      });
    });
}