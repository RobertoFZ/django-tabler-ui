import _ from 'lodash';
window.Popper = require('@popperjs/core');
window.bootstrap = require('bootstrap');
window.$ = window.jQuery = require('jquery');
window.moment = require('moment');
window.select2 = require('select2/dist/js/select2.full');
window.Sortable = require('sortablejs').Sortable;
window.ApexCharts = require('apexcharts');
require('./graphs');

// This ensures that jQuery AJAX functions submit the CSRF token
const getCookie = function (name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrfSafeMethod = function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    }
  }
});

window.onload = () => {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  });

  window.loadPopovers = () => {
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    });
  }

  window.loadPopovers();
}

window.isEmpty = (data) => {
  return (
    // this way we can also check for undefined values. null==undefined is true
    data == null ||
    data == "" ||
    (Array.isArray(data) && data.length === 0) ||
    // we want {} to be false. we cannot use !! because !!{} turns to be true
    // !!{}=true and !!{name:"yilmaz"}=true. !! does not work ofr objects
    (data.constructor === Object && Object.keys(data).length === 0)

  );
};
