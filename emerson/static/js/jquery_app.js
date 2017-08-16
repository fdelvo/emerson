$(document).ready(function () {
    $(".index-picture").mouseenter(function () {
        if ($(this).attr("src") === "/static/images/Emerson.jpg") {
             $("#index-picture-1").animate({
                    opacity: 0,
                    width: 0
                }, {duration: 800, queue: false, easing: "linear"});
                $("#index-picture-2").animate({
                    opacity: 1,
                    width: "40%"
                }, {duration: 800, queue: false, easing: "linear"});
        } else {
             $("#index-picture-2").animate({
                    opacity: 0,
                    width: 0
                }, {duration: 800, queue: false, easing: "linear"});
                $("#index-picture-1").animate({
                    opacity: 1,
                    width: "40%"
                }, {duration: 800, queue: false, easing: "linear"});
        }
    });
    $("#youtube-container").hide();
    $("#spotify").click(function () {
        $("#spotify-container").show();
        $("#youtube-container").hide();
    })
    $("#youtube").click(function () {
        $("#spotify-container").hide();
        $("#youtube-container").show();
    })
});
