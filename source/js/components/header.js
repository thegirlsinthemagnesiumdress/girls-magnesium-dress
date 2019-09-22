const OFFSET = 10;
const selector = '[data-js-header]';
const CLASSES = {
  scrolled: 'aa-header--scrolled',
}

const init = () => {
    const header = document.querySelector(selector);
    const setHeaderState = () => {
      const scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
      if (scrollTop > OFFSET) {
        header.classList.add(CLASSES.scrolled)
      } else {
        header.classList.remove(CLASSES.scrolled);
      }
    }
    setHeaderState();
    window.addEventListener('scroll', setHeaderState);
}



export {
  init,
}
