$(document).ready(function () {
    $("#revert").hide();
    $(".index-picture").mouseover(function () {
        if ($(this).attr("src") === "/static/images/Emerson.jpg") {
            $(this).animate({
                opacity: 0,
                width: 0
            }, 700, "linear", function () {
                $(this).attr("src", "/static/images/Emerson2.jpg");
            }).delay(250).animate({
                opacity: 1,
                width: '60%'
            }, 700, "linear", function () {
                $("#revert").show();
            });
        }
    });

    $("#revert").click(function () {
        $(".index-picture").animate({
            opacity: 0,
            width: 0
        }, 700, "linear", function () {
            $(this).attr("src", "/static/images/Emerson.jpg");
        }).delay(250).animate({
            opacity: 1,
            width: '60%'
        }, 700, "linear", function () {
            $("#revert").hide();
        });
    });

    $("#youtube-container").hide();
    $("#spotify").click(function () {
        $("#spotify-container").show();
        $("#youtube-container").hide();
    });

    $("#youtube").click(function () {
        $("#spotify-container").hide();
        $("#youtube-container").show();
    })
});
