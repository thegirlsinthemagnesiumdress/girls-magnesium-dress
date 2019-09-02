goog.declareModuleId('dmb.survey');

/**
 * Defining the properties we use on the globally provided Qualtrics instance
 *
 * @type {{
 *  SurveyEngine: {
      addOnload:Function,
      addOnReady:Function,
      addOnUnload:Function
 *  }
 * }}
 */
window.Qualtrics;

import * as focusControl from './components/focus-control/focus-control.run';
import * as scrollToFirstError from './survey-components/scroll-to-first-error';
import * as sidePanel from './survey-components/side-panel';
import * as stickyProgress from './survey-components/sticky-progress';

focusControl.main();
scrollToFirstError.init();
sidePanel.init();
stickyProgress.init();
