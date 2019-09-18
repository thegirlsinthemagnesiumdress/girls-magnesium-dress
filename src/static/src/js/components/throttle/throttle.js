/**
 * Utility function that throttles a function call by a set ammount of time,
 * e.g. throttle API calls and only call them every (x)ms
 *
 * Usage:
 * Import { throttle } into component and run it with the following args
 *
 * @param {Function} func: function to call every <limit>ms
 * @param {number} limit: time interval to wait between <func> calls
 *
 * @return {Function}
 *
 */
const throttle = (func, limit) => {
  let lastFunc;
  let lastRan;

  return (...args) => {
    if (!lastRan) {
      func(...args);
      lastRan = Date.now();
      return;
    }

    clearTimeout(lastFunc);
    lastFunc = setTimeout(
      () => {
        if ((Date.now() - lastRan) >= limit) {
          func(...args);
          lastRan = Date.now();
        }
      },
      limit - (Date.now() - lastRan)
    );
  };
};

export {throttle};
