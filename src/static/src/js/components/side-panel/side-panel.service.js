goog.module.declareNamespace('dmb.components.sidePanel.service');

/**
 * Sidepanel service.
 */
class SidePanelService {
  /**
   * Side panel service constructor.
   */
  constructor() {
    /**
     * @type {Object}
     */
    this.sidePanelMap = {};
  }

  /**
   *
   * @param {string} id The panel id
   * @param {dmb.components.sidePanel.class} service
   */
  registerPanel(id, service) {
    this.sidePanelMap[id] = service;
  }

  /**
   * Open the appropriate panel.
   * @param {string} id
   */
  openPanel(id) {
    this.sidePanelMap[id].open();
  }
}

SidePanelService.SERVICE_NAME = 'sidePanelService';


export const main = SidePanelService;
export const SERVICE_NAME = SidePanelService.SERVICE_NAME;
