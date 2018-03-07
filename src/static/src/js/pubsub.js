// Simple PubSub implementation with JavaScript - taken from Addy Osmani's design patterns book -

const pubsub = {};
const topics = {};
let subUid = -1;

pubsub.subscribe = function (topic, func) {
  if (!topics[topic]) {
    topics[topic] = [];
  }
  var token = (++subUid).toString();
  topics[topic].push({
    token: token,
    func: func
  });
  return token;
};

pubsub.publish = function (topic, ...args) {
  if (!topics[topic]) {
    return false;
  }
  setTimeout(function () {
    const subscribers = topics[topic];
    let len = subscribers ? subscribers.length : 0;

    while (len--) {
      subscribers[len].func(topic, ...args);
    }
  }, 0);
  return true;
};

pubsub.unsubscribe = function (token) {
  for (let m in topics) {
    if (topics[m]) {
      for (let i = 0, j = topics[m].length; i < j; i++) {
        if (topics[m][i].token === token) {
          topics[m].splice(i, 1);
          return token;
        }
      }
    }
  }
  return false;
};

export default pubsub;