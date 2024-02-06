import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function createHash(hashKey, hashValues) {
  Object.entries(hashValues).forEach(([key, value]) => {
    client.hset(hashKey, key, value, redis.print);
  });
}

function displayHash(hashKey) {
  client.hgetall(hashKey, (err, reply) => {
    if (err) {
      console.error(`Error retrieving hash ${hashKey}: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
};

createHash('HolbertonSchools', hashValues);
displayHash('HolbertonSchools');
