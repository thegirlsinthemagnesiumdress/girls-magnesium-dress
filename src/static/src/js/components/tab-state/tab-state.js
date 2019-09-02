import {ModelFactory} from '@google/glue/lib/ui/pagination/modelfactory';
const pageAttrName = 'data-glue-pagination-page';

// Function that adds the dimension to the URL and if a dimension is present
// in the URL it takes it and sets the page to the correct one

export default (el) => {
  const tabKey = el.getAttribute('data-glue-pagination');
  const model = ModelFactory.get(tabKey);
  const hash = window.location.hash.split('#!')[1];
  const targetTabLink = el.querySelector(`[href='${hash}']`);
  const targetPage = targetTabLink && targetTabLink.getAttribute(pageAttrName);

  if (targetPage) {
    model.currentPage = parseInt(targetPage, 10);
  }

  model.listen('gluepaginationcurrentpage', () => {
    const pageEl = el.querySelector(`[${pageAttrName}='${model.currentPage}']`);

    if (!pageEl) {
      return;
    }

    window.history.replaceState({}, '', pageEl.href);
  });
};
