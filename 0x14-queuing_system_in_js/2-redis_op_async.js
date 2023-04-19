import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
  }
  
async function displaySchoolValue(schoolName) {
    const getAsync = promisify(client.get).bind(client);
    const value = await getAsync(schoolName);
    console.log(`${schoolName}: ${value}`);
}
  
(async function() {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
    client.quit();
})();
