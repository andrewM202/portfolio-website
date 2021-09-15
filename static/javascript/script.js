$(document).ready(function () {
    // Animation for header
    // If window is bigger than 500px, do margin animation, else only fade animation
    if (Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0) >  500) {
        $("header h1.animation").hide().fadeIn(1500).animate({"margin-right": '+=50'}, 2500);
        $(".card").addClass("hvr-float")
        // $(".jumbotron").addClass("animate__animated animate__fadeInLeft")
        // $(".mini-jumbotron").addClass("animate__animated animate__fadeInRight")
    }
    else {
        $("header h1").hide().fadeIn(1500);
    }
    $("header h1.fade-animation").hide().fadeIn(1500);

    $("#resume-click").click(function () {
        $("#gray-bg").css({
            "display": "inherit",
            "height": $(document).height()
        })
        $("#adobe-close").css({
            "display": "inherit",
            "top": $(document).scrollTop() + 10
        })
        $("body").css({
            "overflow": "hidden"
        })
        $("#adobe-dc-view").css({
            "display": "inherit",
            "opacity": "100%",
            "top": $(document).scrollTop()
        })
    });
    $("#adobe-close").click(function () {
        $("#adobe-close").css("display", "none")
        $("#gray-bg").css({
            "display": "none"
        })
        $("#adobe-dc-view").css({
            "display": "none",
        })
        $("body").css({
            "overflow": "inherit"
        })
    });

    let projDescs =  [
        // Weather site
        "Utilizes the PHP framework Laravel to dynamically access current weather, news, pollution data, and facts of the country of original with API calls.",
        // Social media site
        "social media site",
        // shopping site
        "shopping site",
        // old portfoio
        "Old portfolio",
        // DOM adventure game
        "DOM adventure",
        // tic tac toe
        "Tic tac toe",
        // Website template
        "Website template"
    ]

    // Refresh the text for the project description
    setInterval(function () {
        let currProject = Number($(".active").attr("id"));
        $(".project-desc").text(projDescs[currProject]);
    }, 1);
});
