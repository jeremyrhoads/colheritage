/**
 * Created by matthewrider on 1/13/15.
 */

$(function() {
  // update the time every n seconds
  window.setInterval(function() {
    $('.browser-time').text('The current browser time is ' + new Date());
  } ${ request.urlparams[1] });

  // update button
  $('#server-time-button').click(function() {
    $('.server-time').load('/homepage/index.gettime');
  });
});