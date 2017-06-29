
# Simple component system using ES6 classes

## Usage

You can specify controllers using the `data-controllers=""` attribute on dom elements.

```
<div id="my-element" data-controllers="hello-world">
    <div id="my-other-element" data-controllers="hello-world">

    </div>
</div>
```

Controllers are subclasses of Controller, and must be registered with the controller manager:

```
import {Controller} from 'controller.js';

class HelloWorld extends Controller {

    init(element) { //< element is passed to init
        // You can register listeners for 'messages'
        this.listen("hello:message, this.messageCallback.bind(this));

        // You can listen to message groups
        this.listen("hello", this.messageCallback.bind(this));

        // You can broadcast messages to other controllers
        this.broadcast("hello:message", {data:1});

        // this.parent() is available as is this.parents()
        this.parent().helloWorld();
    }

    cleanup() {
        // Called when the counterpart element is destroyed
        super.cleanup() //< Cleans up listners
    }

    helloWorld() {
        // this.element is also a thing
        alert(this.element.id);
    }

    messageCallback(message, data) {
        // Messages are processed from most specific, to least specific in the order they are added
        // e.g. hello:message listeners will be processed before hello listeners

        return true; // Returning true will stop propagation immediately, no further listeners will be called
    }
}

window.controllers.register("hello-world", HelloWorld); // Register the controller
```