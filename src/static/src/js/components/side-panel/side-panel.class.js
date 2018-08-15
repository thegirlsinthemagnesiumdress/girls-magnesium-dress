goog.module('dmb.components.sidePanel.class');

/**
 * Side panel class
 */
class SidePanel {
  /**
   * Constructor
   * @param  {Element} element The panel element to set up
   */
  constructor(element) {
    /**
     * @const
     * @type {Element}
     */
    this.el = element;


    /**
     * The id of the element
     * @const
     * @type {string}
     * @export
     */
    this.id = element.id;


    /**
     * Array of all the elements on the page that can open this side panel
     * @type {Array.<Element>}
     */
    this.triggers = [...document.querySelectorAll(`[data-side-panel-trigger="#${this.id}"]`)];


    /**
     * Bound context for triggerClickHandler
     * @type {Fuction}
     * @export
     */
    this.onTriggerClick = this.triggerClickHandler.bind(this);

    this.bindEvents();
  }


  /**
   * Binds the event listeners to all of the triggers
   */
  bindEvents() {
    if (!this.triggers) {
      return;
    }

    this.triggers.forEach((trigger) => {
      trigger.addEventListener('click', this.onTriggerClick);
    });
  }


  /**
   * Handles when a side panel trigger is clicked on
   * @param  {Event} event The native click event
   * @export
   */
  triggerClickHandler(event) {
    event.preventDefault();

    alert('Triggered'); // eslint-disable-line
  }


  /**
   * Handles the unbinding of any events outside of this component
   * @export
   */
  destroy() {
    this.triggers.forEach((trigger) => {
      trigger.removeEventListener('click', this.onTriggerClick);
    });
  }
}


exports = {
  main: SidePanel,
};
