/**
 * Creates Analytics click events on elements that contain the `data-tr-event`
 * attribute.
 */
export function initAnalytics() {
  var customEventEls = document.querySelectorAll('[data-tr-event]');
  customEventEls.forEach(function (el) {
    el.addEventListener('click', function (e) {
      var el = e.currentTarget;
      ga('send', {
        hitType: 'event',
        eventAction: el.getAttribute('data-tr-action'),
        eventCategory: el.getAttribute('data-tr-category'),
        eventLabel: el.getAttribute('data-tr-label')
      });
    });
  });

}
