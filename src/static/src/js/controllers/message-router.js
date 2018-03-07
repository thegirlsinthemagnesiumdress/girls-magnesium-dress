

let matches_filter = function(message_id, filter) {
    let message_parts = message_id.split(":");
    let filter_parts = filter.split(":");

    if(filter_parts.length > message_parts.length) {
        return false;
    }

    for(let i = 0; i < filter_parts.length; ++i) {
        if(filter_parts[i] !== message_parts[i]) {
            return false;
        }
    }

    return true;
}

class MessageRouter {
    constructor() {
        this._listeners = {}
    }

    registerListener(message_id, controller, callback) {
        let id = [controller.id, message_id];
        let element = {
            "id": id,
            "callback": callback
        };
        if(this._listeners[message_id]) {
            this._listeners[message_id].push(element);
        } else {
            this._listeners[message_id] = [element];
        }

        return id;
    }

    unregisterListener(id) {
        let message_id = id[1];

        if(this._listeners[message_id]) {
            let items = this._listeners[message_id];
            while(items.indexOf(id) !== -1) {
                items.splice(items.indexOf(id), 1);
            }
        }
    }

    sendMessage(message_id, data) {
        let filters = Object.keys(self._listeners);
        filters.sort();
        filters.reverse(); // Call more specific filters first

        for(let filter in self._listeners) {
            if(self._listeners.hasOwnProperty(filter)) {
                if(matches_filter(message_id, filter)) {
                    let handlers = self._listeners[filter];
                    for(let i = 0; i < handlers.length; ++i) {
                        let callback = handlers[i]['callback'];
                        if(callback(message_id, data)) {
                            // Stop calling things
                            return;
                        }
                    }
                }
            }
        }
    }
}

const eventBus = new MessageRouter()
export { eventBus };
