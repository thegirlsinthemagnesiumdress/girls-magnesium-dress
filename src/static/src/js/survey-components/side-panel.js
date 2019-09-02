import {SidePanel} from '../components/side-panel/side-panel.class';

/**
 * Initialises the side panels on the page
 * @return {Array.<SidePanel>} An array of the SidePanel instances
 */
export function init() {
  const sidePanelElements = [...document.querySelectorAll('[dmb-side-panel]')];

  return sidePanelElements.map((element) => {
    return new SidePanel(element);
  });
}
