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
 * <button id="clippy-example" class="dmb-button" dmb-clippy="https://p.ota.to">
 *  Copy Potato
 * </button>
 *
 * If a toast notification is wanted then append the 'dmb-clippy-toast' attribute
 * with a value of the id of the dmb-clippy control onto the element and,
 * optionally, use the 'dmb-toast' class. E.g:
 *
 * <div class="dmb-toast" dmb-clippy-toast="clippy-example" aria-live="assertive">
 *  Copied to clipboard
 * </div>
 *
 * Remember to add 'aria-live="assertive"' for accessibility
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
    // Find toast notifcations for this dmb-clippy.
    const toasts = Array.from(document.querySelectorAll('[dmb-clippy-toast]'))
    .filter((toast) => {
      return toast.getAttribute('dmb-clippy-toast') == elem.id;
    });
    // On success clear the selection and show a toast notification.
    clipboard.on('success', (e) => {
      // Add timeout to toasts to show and hide them.
      toasts.forEach((toast) => {
        toast.classList.add('dmb-toast__active');
        setTimeout(() => {
          toast.classList.remove('dmb-toast__active');
        }, 5000);
      });
      e.clearSelection();
    });
  }
}
