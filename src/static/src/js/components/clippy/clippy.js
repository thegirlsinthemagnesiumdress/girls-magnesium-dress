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
   * Attaches methods to provided element.
   * @param {Node} elem : Element to attach clippy functionality to.
   */
  constructor(elem) {
    this.root = elem;
    // Create new clipboard JS object which gets the value of the dmb-clipp attribute.
    this.selector = 'dmb-clippy';
    this.clipboard = new window['ClipboardJS'](this.root, {
      text: (trigger) => {
        return trigger.getAttribute(this.selector);
      },
    });
    // Find toast notifcations for this dmb-clippy.
    this.toastSelector = 'dmb-clippy-toast';
    this.toasts = Array.from(document.querySelectorAll(`[${this.toastSelector}]`))
    .filter((toast) => {
      return toast.getAttribute(this.toastSelector) == this.root.id;
    });
    // On success clear the selection and show a toast notification.
    this.clipboard.on('success', this.onSuccess.bind(this));
  }

  /**
   * Attachs clippy functionality to element.
   * @param {Node} elem : Element to attach Clippy to.
   * @return {Clippy} : Returns a reference to the clippy instance created.
   */
  static attachTo(elem) {
    return new Clippy(elem);
  }

  /**
   * Callback function for ClipboardJS onSuccess event.
   * @param {Event} e : Event returned from ClipboardJS success.
   */
  onSuccess(e) {
    const className = 'dmb-toast--active';
    // Add timeout to toasts to show and hide them.
    this.toasts.forEach((toast) => {
      if (toast.classList.contains(className)) {
        return;
      }
      const onAnimationEnd = function() {
        toast.classList.remove(className);
        toast.removeEventListener('animationend', onAnimationEnd);
      };
      toast.addEventListener('animationend', onAnimationEnd);
      toast.classList.add(className);
    });
    e['clearSelection']();
  }
}
