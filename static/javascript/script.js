$(document).ready(function () {
    // Animation for header
    // If window is bigger than 500px, do margin animation, else only fade animation
    if (Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0) >  500) {
        $("header h1.animation").hide().fadeIn(1500).animate({"margin-right": '+=50'}, 2500);
    }
    else {
        $("header h1").hide().fadeIn(1500);
    }
    $("header h1.fade-animation").hide().fadeIn(1500);

    $(".card").addClass("hvr-float")
    $(".jumbotron").addClass("animate__animated animate__fadeInLeft")
    $(".mini-jumbotron").addClass("animate__animated animate__fadeInRight")

});
