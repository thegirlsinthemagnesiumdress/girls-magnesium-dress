

class Controller {
    constructor(id, element, router) {
        this.id = id;
        this.element = element;

        this._router = router;
        this._listeners = [];
    }

    init(element) {}
    cleanup() {
        // Make sure we detach all listeners
        for(let i = 0; i < this._listeners.length; ++i) {
            this._router.unregisterListener(this._listeners[i]);
        }

        this._listeners = [];
    }

    broadcast(message_id, data) {
        this._router.sendMessage(message_id, data);
    }

    listen(message_filter, callback) {
        this._listeners.push(
            this._router.registerListener(message_filter, this, callback)
        );
    }

    parent(controllerName=null) {
        /*
            Returns this.parents()[0][0]; e.g. the first controller if the closest element with controllers
        */
        return this.parents(component_name)[0][0];
    }

    parents(controllerName=null) {
        /*
            Returns an array of [[controller, controller...], [controller, controller...]] where each element in the outer array
            contains the controllers for a single *[data-controllers] element.
        */

        let a = this.element;
        let els = [];

        let results = [];
        while (a) {
            els.unshift(a);
            a = a.parentNode;

            let level = [];

            if(a.controllerInstances) {
                for(let key in a.controllerInstances) {
                    if(controllerName && controllerName !== key) {
                        continue;
                    }
                    level.push(a.controllerInstances[key]);
                }
            }

            results.push(level);
        }

        return results;
    }
}

export {Controller};