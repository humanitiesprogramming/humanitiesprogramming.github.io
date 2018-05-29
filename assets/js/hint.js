$(document).ready(function() {
  $('.highlight').hide().before($('<a class="answer"><i class="fas fa-terminal"></i></a>'));

  $('.answer').click(function() {
    $(this).next('.highlight').slideToggle('slow');
  });
});
