goog.module('dmb.components.sidePanel.service');

/**
 * Sidepanel service.
 */
class SidePanelService {
  /**
   * Side panel service constructor.
   */
  constructor() {
    /**
     * @type {object}
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


exports = {
  main: SidePanelService,
  SERVICE_NAME: SidePanelService.SERVICE_NAME,
};
