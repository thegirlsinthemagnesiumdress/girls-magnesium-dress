export default class ParallaxSection extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    console.log('Hello from custom element!')
  }
}
