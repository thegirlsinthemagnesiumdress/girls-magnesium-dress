import axios from 'axios';
import handlebars from 'handlebars'

import eventsTemplate from './events-tempate';
import {init as initEvents} from '../events';
import eventTemplate from './event-template';

const eventsEndpoint = '/events.json';
const eventsContainer = document.querySelector('.aa-events__container');

handlebars.registerHelper('formatDate', function(dateString) {
    return new handlebars.SafeString(
        new Date(dateString).toLocaleDateString()
    );
});

handlebars.registerHelper('formatTime', function(dateString) {
    return new handlebars.SafeString(
        new Date(dateString).toLocaleTimeString('en-US', {hour: '2-digit', minute: '2-digit', hour12: true})
    );
});

handlebars.registerPartial('event', eventTemplate)
const html = handlebars.compile(eventsTemplate);


axios.get(eventsEndpoint)
    .then((r) => {
        const events = r.data.sort((a, b) => new Date(a.date) - new Date(b.date));
        const now = new Date()
        const futureEvents = events
            .filter((e) => new Date(e.date) > now)
        let pastEvents = events
            .filter((e) => new Date(e.date) < now)
            .slice(-7, -1);

         eventsContainer.innerHTML = html({
            futureEvents,
            pastEvents: pastEvents.sort((a, b) => new Date(b.date) - new Date(a.date))
        });
        initEvents();
    });

