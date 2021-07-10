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
        $(".carousel-control-next").css('background', '#EFEFEF'); // White

        setTimeout(function() {
            $(".carousel-control-next").css('background', 'rgb(239, 239, 239)'); // Gray
        }, 1000);
    });
    $(".carousel-control-prev").click(function() {
        $(".carousel-control-prev").css('background', '#EFEFEF'); // White

        setTimeout(function() {
            $(".carousel-control-prev").css('background', 'rgb(239, 239, 239)'); // Gray
        }, 1000);
    });
});
