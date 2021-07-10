$(document).ready(function () {
    // Animation for header
    // If window is bigger than 500px, do margin animation, else only fade animation
    if (Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0) >  500) {
        $("header h1").hide().fadeIn(1500).animate({"margin-right": '+=50'}, 2500);
    }
    else {
        $("header h1").hide().fadeIn(1500);
    }

    // Make buttons fill in white on mobile
    $(".carousel-control-next").click(function() {
        $(".carousel-control-next").css('background', '#FFF'); // White
    });
    $(".carousel-control-prev").click(function() {
        $(".carousel-control-next").css('background', '#FFF'); // White
    });
});
