import {Controller} from '../js/controllers/controller.js';
import {init} from '../js/controllers/controller-manager.js';

describe("Controllers", function() {
  let window = window || {
    document: {
      documentElement: {},
      querySelectorAll: function() { return []; }
    }
  };

  class MutationObserver {
    constructor(callback) {
      this.callback = callback;
    }
    observe() {}
  }

  class TestController extends Controller {}

  it("should be instantiated on DOM elements", function() {
    spyOn(window.document, 'querySelectorAll').andReturn([
        {
            tagName: "div",
            dataset: {controllers: "test"}
        }
    ]);

    init(window, MutationObserver);
    window.controllers.register("test", TestController);

    let node = {
        tagName: "div",
        dataset: {controllers: "test"}
    };

    // Trigger the mutation observer
    window.controllers._observer.callback([
      {type: "childList", addedNodes:[{
          nodeType: 1,
          querySelectorAll: function() {
            return [node];
          }
      }], removedNodes: []}
    ]);

    // Component should be registered
    expect(window.controllers._registry["test"]).toBe(TestController);

    // Controller instance should be attached to the node
    expect(node.controllerInstances).toBeDefined();
    expect(node.controllerInstances.test).toBeDefined();
  });
});