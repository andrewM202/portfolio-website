$(document).ready(function () {
    // Animation for header
    // If window is bigger than 1000px, do margin animation, else only fade animation
    if (Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0) >  1000) {
        $("header h1.animation").hide().fadeIn(1500).animate({"margin-right": '+=50'}, 2500);
        $(".card").addClass("hvr-float")
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
        // $("body").css({
        //     "overflow": "hidden"
        // })
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
        // $("body").css({
        //     "overflow": "inherit"
        // })
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
        // $("body").css({
        //     "overflow": "inherit"
        // })
    });
            
    let projDescs =  [
        {
            // Weather site
            "desc": `Utilizes the PHP framework Laravel to dynamically 
            access current weather, news, pollution data, 
            and facts of the country of original with API calls.`,
            "link": `https://weather-app421.herokuapp.com/`,
            'github': `https://github.com/andrewM202/weather-news-app`,
            'alt': `Weather_Website`,
            'name': `Weather Website`
        },
        {
            // Social media site
            "desc": `A global chat application created in collaboration 
            with peer developers using git. Utilizes the Flask framework,
            with WebSocket requests for the chat functionality.`,
            "link": `https://social-media-app421.herokuapp.com/`,
            'github': `https://github.com/andrewM202/social-media-app`,
            'alt': `Chat_Application`,
            'name': `Chat Application`
        },
        {
            // shopping site
            "desc": `The first application I created with a SQL backend. Utilizes 
            the Flask framework.`,
            "link": `https://shopping-cart952.herokuapp.com/`,
            'github': `https://github.com/andrewM202/shopping-cart`,
            "alt": `Shopping_Site`,
            'name': `Shopping Site`
        },
        {
            // old portfolio
            "desc": `My previous portfolio website! A static website that 
            uses custom SVGs as a border for the website.`,
            "link": `https://andrewm202.github.io/`,
            "github": `https://github.com/andrewM202/andrewM202.github.io`,
            "alt": `Old_Portfolio`,
            'name': `Old Portfolio`
        },
        {
            // DOM adventure game
            "desc": `An adventure game entrirely created using vanilla JavaScript 
            DOM methods to rebuild each scene in the game.`,
            "link": `https://andrewm202.github.io/dom-adventure-game/`,
            "github": `https://github.com/andrewM202/dom-adventure-game`,
            "alt": `DOM_Adventure_Game`,
            "name": `DOM Adventure Game`
        },
        {
            // tic tac toe
            "desc": `A simple tic-tac-toe game built from scratch using vanilla
            JavaScript.`,
            "link": `https://andrewm202.github.io/tic-tac-toe/`,
            "github": `https://github.com/andrewM202/tic-tac-toe`,
            "alt": `Tic-Tac-Toe`,
            "name": `Tic-Tac-Toe`
        },
        {
            // Website template
            "desc": `A static website template built as I was learning CSS Grid and
            Flexbox, in order to fully understand the concept.`,
            "link": `https://andrewm202.github.io/Website-Template/`,
            "github": `https://github.com/andrewM202/Website-Template`,
            "alt": `Website_Template`,
            "name": `Website Template`
        }
    ]

    const initializeCarousel = function() {
        let carouselChildren = $(".carousel-container > figure").children("img");
        $(".carousel-prev").click(function() {
            for(let child of carouselChildren) {
                if(child.className === "active") {
                    for(let i=0; i<projDescs.length; i++) {
                        if(child.alt === projDescs[i].alt) {
                            if($(".active").prev("img").length === 0) {
                                $("figure").children("img:last-of-type").addClass("active")
                                $("figure").children(`[alt=${child.alt}]`).removeClass()
                                $(".project-desc").text(projDescs[projDescs.length-1].desc);
                                // Refresh the text and href for the project link
                                $("#resume-link").attr("href", projDescs[projDescs.length-1].link)
                                $("#resume-link").children().text(projDescs[projDescs.length-1].name + "\'s Live URL")
                                // Refresh the text and href for the project github
                                $("#resume-github").attr("href", projDescs[projDescs.length-1].github)
                                $("#resume-github").children().text(projDescs[projDescs.length-1].name + "\'s Github")

                            } else {
                                $(".active").prev().addClass('active')
                                $("figure").children(`[alt=${child.alt}]`).removeClass()
                                $(".project-desc").text(projDescs[i-1].desc);
                                // Refresh the text and href for the project link
                                $("#resume-link").attr("href", projDescs[i-1].link)
                                $("#resume-link").children().text(projDescs[i-1].name + "\'s Live Site Here")
                                // Refresh the text and href for the project github
                                $("#resume-github").attr("href", projDescs[i-1].github)
                                $("#resume-github").children().text(projDescs[i-1].name + "\'s Github Here")
                            }
                        }
                    }
                    break;
                }
            }
        })
        $(".carousel-next").click(function () {
            for(let child of carouselChildren) {
                if(child.className === "active") {
                    for(let i=0; i<projDescs.length; i++) {
                        if(child.alt === projDescs[i].alt) {
                            if($(".active").next("img").length === 0) {
                                $("figure").children("img:first-of-type").addClass("active")
                                $("figure").children(`[alt=${child.alt}]`).removeClass()
                                $(".project-desc").text(projDescs[0].desc);
                                // Refresh the text and href for the project link
                                $("#resume-link").attr("href", projDescs[0].link)
                                $("#resume-link").children().text(projDescs[0].name + "\'s Live URL")
                                // Refresh the text and href for the project github
                                $("#resume-github").attr("href", projDescs[0].github)
                                $("#resume-github").children().text(projDescs[0].name + "\'s Github")

                            } else {
                                $(".active").next().addClass('active')
                                $("figure").children(`[alt=${child.alt}]`).removeClass()
                                $(".project-desc").text(projDescs[i+1].desc);
                                // Refresh the text and href for the project link
                                $("#resume-link").attr("href", projDescs[i+1].link)
                                $("#resume-link").children().text(projDescs[i+1].name + "\'s Live URL")
                                // Refresh the text and href for the project github
                                $("#resume-github").attr("href", projDescs[i+1].github)
                                $("#resume-github").children().text(projDescs[i+1].name + "\'s Github")
                            }
                        }
                    }
                    break;
                }
            }
        })

        setInterval(function() {
            const nextSlide = function() {
                for (child of carouselChildren) {
                    if(child.className === "active") {
                        for(let i=0; i<projDescs.length; i++) {
                            if(projDescs[i].alt === child.alt) {
                                if($(".active").next("img").length === 0) {
                                    $(`[alt=${child.alt}]`).removeClass("active")
                                    $("figure").children("img:first-of-type").addClass("active")
                                    $(".project-desc").text(projDescs[0].desc);
                                    // Refresh the text and href for the project link
                                    $("#resume-link").attr("href", projDescs[0].link)
                                    $("#resume-link").children().text(projDescs[0].name + "\'s Live URL")
                                    // Refresh the text and href for the project github
                                    $("#resume-github").attr("href", projDescs[0].github)
                                    $("#resume-github").children().text(projDescs[0].name + "\'s Github")
                                } else {
                                    $(".active").next("img").addClass("active")
                                    $(`[alt=${child.alt}]`).removeClass("active")
                                    $(".project-desc").text(projDescs[i+1].desc);
                                    // Refresh the text and href for the project link
                                    $("#resume-link").attr("href", projDescs[i+1].link)
                                    $("#resume-link").children().text(projDescs[i+1].name + "\'s Live URL")
                                    // Refresh the text and href for the project github
                                    $("#resume-github").attr("href", projDescs[i+1].github)
                                    $("#resume-github").children().text(projDescs[i+1].name + "\'s Github")
                                }
                            }
                        }
                        break;
                    }
                }
            }
            nextSlide()
        }, 10000)
    }
    initializeCarousel()

    $(".blog-submit").click(function() {
        let form = $(".blog-form")
        alert(form[0])
    })
});
