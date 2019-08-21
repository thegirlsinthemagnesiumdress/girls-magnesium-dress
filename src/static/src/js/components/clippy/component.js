import ClipboardJs from 'clipboard';

/**
 * Component which copies an elements content to the clipboard
 * when clicked, using clipboard.js and displays a toast
 * notifcation to signal the action has been completed.
 *
 * Usage:
 * Add the 'dmb-clippy' attribute to the element and assign
 * the attribute the value you want copied, e.g:
 *
 * <button class="dmb-button" dmb-clippy="https://p.ota.to">Copy Potato</button>
 */
export default class Clippy {
  /**
   *  Constructor for the clippy module.
   * @param {Node} elem : Element in the dom to attach event listeners etc. to.
   */
  constructor(elem) {
    this.root = elem;
    this.clipboard = new ClipboardJs(elem, {
      text: (trigger) => {
        return trigger.getAttribute('dmb-clippy');
      },
    });
    this.clipboard.on('success', (e) => {
      e.clearSelection();
    });
  }

  /**
   * Attachs clippy functionality to element.
   * @param {Node} elem : Element to attach Clippy to.
   * @return {Clippy} : returns a clippy instance for the element.
   */
  static attachTo(elem) {
    return new Clippy(elem);
  }
}
