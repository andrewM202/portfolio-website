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

    // Open the resume if the resume button is clicked
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
    // If the cancel button is clicked, close the resume
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
    // If the gray background is clicked, close the resume
    $("#gray-bg").click(function () {
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
        {
            // Weather site
            "desc": `Utilizes the PHP framework Laravel to dynamically 
            access current weather, news, pollution data, 
            and facts of the country of original with API calls.`,
            "link": `https://weather-app421.herokuapp.com/`,
            'github': `https://github.com/andrewM202/weather-news-app`,
            'name': `Weather site`
        },
        {
            // Social media site
            "desc": `A global chat application created in collaboration 
            with peer developers using git. Utilizes the Flask framework,
            with WebSocket requests for the chat functionality.`,
            "link": `https://social-media-app421.herokuapp.com/`,
            'github': `https://github.com/andrewM202/social-media-app`,
            'name': `Chat Application`
        },
        {
            // shopping site
            "desc": `The first application I created with a SQL backend. Utilizes 
            the Flask framework.`,
            "link": `https://shopping-cart952.herokuapp.com/`,
            'github': `https://github.com/andrewM202/shopping-cart`,
            "name": `Shopping site`
        },
        {
            // old portfolio
            "desc": `My previous portfolio website! A static website that 
            uses custom SVGs as a border for the website.`,
            "link": `https://andrewm202.github.io/`,
            "github": `https://github.com/andrewM202/andrewM202.github.io`,
            "name": `Old portfolio`
        },
        
        {
            // DOM adventure game
            "desc": `An adventure game entrirely created using vanilla JavaScript 
            DOM methods to rebuild each scene in the game.`,
            "link": `https://andrewm202.github.io/dom-adventure-game/`,
            "github": `https://github.com/andrewM202/dom-adventure-game`,
            "name": `DOM Adventure Game`
        },
        {
            // tic tac toe
            "desc": `A simple tic-tac-toe game built from scratch using vanilla
            JavaScript.`,
            "link": `https://andrewm202.github.io/tic-tac-toe/`,
            "github": `https://github.com/andrewM202/tic-tac-toe`,
            "name": `Tic-Tac-Toe`
        },
        {
            // Website template
            "desc": `A static website template built as I was learning CSS Grid and
            Flexbox, in order to fully understand the concept.`,
            "link": `https://andrewm202.github.io/Website-Template/`,
            "github": `https://github.com/andrewM202/Website-Template`,
            "name": `Website template`
        }
    ]

    setInterval(function () {
        // Refresh the text for the project description
        let currProject = Number($(".active").attr("id"));
        $(".project-desc").text(projDescs[currProject].desc);
        // Refresh the text and href for the project link
        $("#resume-link").attr("href", projDescs[currProject].link)
        $("#resume-link").children().text(projDescs[currProject].name + "\'s Live Site Here")
        // Refresh the text and href for the project github
        $("#resume-github").attr("href", projDescs[currProject].github)
        $("#resume-github").children().text(projDescs[currProject].name + "\'s Github Here")
    }, 1);
});
