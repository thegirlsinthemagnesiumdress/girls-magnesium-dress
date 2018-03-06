

// import {init} from './controllers/controller-manager.js';
// import {Controller} from './controllers/controller.js';

import fullpage from 'fullpage.js/dist/jquery.fullpage';
import jQuery from "jquery";

window.$ = jQuery;

// init();
$(document).ready(function() {
	$('#fullpage').fullpage();
});
