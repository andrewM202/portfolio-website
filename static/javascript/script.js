$(document).ready(function () {
    // Animation for header
    if (jQuery(window).width >= 500) {
        $("header h1").hide().fadeIn(1500).animate({"margin-right": '+=50'}, 2500)
    }
    else {
        $("header h1").hide().fadeIn(1500)
    }
});
