import {MessageRouter} from './message-router.js';

class ControllerManager {
  constructor(window, router, observerClass) {
    this._window = window;
    this._document = window.document;
    this._router = router;
    this._registry = {};
    this._observer = new observerClass(this.onDOMChanged.bind(this));
    this._observer.observe(this._document.documentElement, {childList: true, subtree: true});

    this._id_generator = function() {
      // https://stackoverflow.com/a/2117523
      return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
        return v.toString(16);
      });
    }
  }

  addController(node, controllerName) {
    if(this._registry[controllerName]) {
      const newController = new this._registry[controllerName](this._id_generator(), node, this._router);

      if(newController.init) {
        newController.init(node);
      }

      if(node.controllerInstances === undefined) {
        node.controllerInstances = {};
      }

      node.controllerInstances[controllerName] = newController;
    }
  }

  removeController(node, controllerName) {
    const controller = node.controllerInstances[controllerName];

    if(controller) {
      controller.cleanup();
      node.controllerInstances[controllerName] = null;
    }
  }

  register(name, klass) {
    if(!this._registry[name]) {
      this._registry[name] = klass;
    }

    [...this._document.querySelectorAll(`[data-controllers*="${name}"]`)]
      .forEach(node => { this.addController(node, name); });
  }

  registerHandler(nodeSelector, event, handler) {
    let nodes = [...this._document.querySelectorAll(nodeSelector)];
    nodes.forEach(node => node.addEventListener(event, handler));
  }

  onDOMChanged(mutations) {
    let self = this;

    let removeControllerFromElement = (elem) => {
      for(let key in elem.controllerInstances) {
        self.removeController(elem, key);
      }
    };

  let addControllersToElement = (elem) => {
    if(elem.dataset.controllers) {
        const controllers = elem.dataset.controllers.split(" ");

      for(let j = 0; j < controllers.length; ++j) {
        const controller = controllers[j];
        self.addController(elem, controller);
      }
    }
  };

  const ELEMENT = 1;

  mutations
    .filter(m => m.type === 'childList')
    .forEach(function(mutation) {
      for(let i = 0; i < mutation.addedNodes.length; ++i) {
        const node = mutation.addedNodes[i];
        if(node.nodeType !== ELEMENT) {
          continue;
        }

        [...node.querySelectorAll("[data-controllers]")].forEach(addControllersToElement);
      }

      for(let i = 0; i < mutation.removedNodes.length; ++i) {
        const node = mutation.removedNodes[i];
        if(node.nodeType !== ELEMENT) {
          continue;
        }

        [...node.querySelectorAll("[data-controllers]")].forEach(removeControllerFromElement);
      }
  });
  }
}

function init(win, observerClass=MutationObserver) {
  win = win || window;
  win.router = win.router || new MessageRouter();
  win.controllers = win.controllers || new ControllerManager(win, win.router, observerClass);
}

export {init};