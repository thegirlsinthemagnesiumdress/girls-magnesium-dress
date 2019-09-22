// import {log} from './logger';
// import {init as initHeader} from './components/header';
import {init as initEvents} from './components/events';
// import SmoothScroll from 'smooth-scroll';
import './components/events/events-controller';

// import initPlugins from './all-plugins';
import 'jquery';
import 'bootstrap';
import ScrollReveal from 'scrollreveal'
import 'fancybox';
// import 'bxslider';


$(document).ready(function() {
  // Mobile menu trigger script
  $(".menu-trigger").click(function() {
      $(this).toggleClass('active');
      $(".mobile-menu").toggleClass('visible');
  });
  // Smoothscroll script
  $('.nav-link').click(function() {
      var dis = $(this),
          disTarget = dis.children('a').data('target'),
          ScrollTo = $(disTarget).offset().top;
      dis.siblings('.nav-link').removeClass('active');
      dis.addClass('active')
      $('html,body').animate({ scrollTop: ScrollTo });
  });
  // contact form script
  $('.form-wrap input').blur(function() {
      tmpval = $(this).val();
      if (tmpval == '') {
          $(this).addClass('empty');
          $(this).removeClass('not-empty');
      } else {
          $(this).addClass('not-empty');
          $(this).removeClass('empty');
      }
  });
  // testimonial slider
  // $('.testimonial-slider').bxSlider({
  //     auto: true,
  //     mode: 'fade',
  //     infiniteLoop: true,
  //     controls: false
  // });
  // Changing the defaults
  window.sr = ScrollReveal();
  // Customizing a reveal set
  sr.reveal('.each-service', { origin: 'bottom', distance: '100px', duration: 1000, delay: 0, easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)' });
  // sript for fixed header on scroll
  $(window).scroll(function() {
      var scroll = $(window).scrollTop();
      if (scroll >= 60) {
          $("#Header").addClass("header-fixed");
      } else {
          $("#Header").removeClass("header-fixed");
      }
  });
});


// const initSmoothScrollLinks = () => {
//   var scroll = new SmoothScroll('a[href*="#"]', {
//     ignore: '[data-scroll-ignore]', // Selector for links to ignore (must be a valid CSS selector)
//     header: '.aa-header', // Selector for fixed headers (must be a valid CSS selector)
//     topOnEmptyHash: true, // Scroll to the top of the page for links with href="#"
//     speed: 500, // Integer. How fast to complete the scroll in milliseconds
//     clip: true, // If true, adjust scroll distance to prevent abrupt stops near the bottom of the page
//     easing: 'easeInOutCubic', // Easing pattern to use
//     customEasing: function (time) {
//       return time < 0.5 ? 2 * time * time : -1 + (4 - 2 * time) * time;
//     },
//     updateURL: true, // Update the URL on scroll
//     popstate: true, // Animate scrolling with the forward/backward browser buttons (requires updateURL to be true)
//     emitEvents: true // Emit custom events
//   });
// }

// initHeader();
// initSmoothScrollLinks();
// initSmoothScrollLinks();
initEvents();
