goog.module('dmb.survey.sidePanel');

const SidePanel = goog.require('dmb.components.sidePanel.class');

/**
 * Initialises the side panels on the page
 * @return {Array.<SidePanel>} An array of the SidePanel instances
 */
function init() {
  const sidePanelElements = [...document.querySelectorAll('[dmb-side-panel]')];

  return sidePanelElements.map((element) => {
    return new SidePanel(element);
  });
}

exports = {
  init,
};
