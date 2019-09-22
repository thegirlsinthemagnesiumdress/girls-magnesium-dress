
const selector = '[data-js-event]';
const CLASSES = {
  more: 'aa-event--more',
}
const DOM_SELECTORS = {
  toggle: '.aa-event__toggle-more'
}

const init = () => {
    const events = document.querySelectorAll(selector);

    [].forEach.call(events, (event) => {
      const toggle = event.querySelector(DOM_SELECTORS.toggle);
      if (toggle) {
        toggle.addEventListener('click', (e) => {
          const more = event.classList.toggle(CLASSES.more);
          e.preventDefault();
        });
      }
    })
}



export {
  init,
}
