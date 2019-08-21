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
   * Attachs clippy functionality to element.
   * @param {Node} elem : Element to attach Clippy to.
   */
  static attachTo(elem) {
    // Create new clipboard JS object which gets the value of the dmb-clipp attribute.
    let clipboard = new ClipboardJs(elem, {
      text: (trigger) => {
        return trigger.getAttribute('dmb-clippy');
      },
    });
    // On success clear the selection and TODO: show a toast notification.
    clipboard.on('success', (e) => {
      e.clearSelection();
    });
  }
}
