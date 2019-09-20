/**
 * LdapLink Component
 */
export default class LdapLink {
  /**
   * @param {Element} elem
   * @return {LdapLink}
   */
  static attachTo(elem) {
    return new LdapLink(elem);
  }

  /**
   * @param {Element} elem
   */
  constructor(elem) {
    this.elem = elem;

    this.onClick = this.onClick.bind(this);

    this.elem.addEventListener('click', this.onClick);
  }

  /**
   * @param {Event} e Click event
   */
  onClick(e) {
    e.stopPropagation();
  }
}
