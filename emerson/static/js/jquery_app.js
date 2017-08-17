$(document).ready(function () {
    $("#revert").hide();
    $(".index-picture").mouseover(function () {
        if ($(this).attr("src") === "/static/images/Emerson.jpg") {
            $(this).animate({
                opacity: 0
            }, 700, "linear", function () {
                $(this).attr("src", "/static/images/Emerson2.jpg");
            }).delay(500).animate({
                opacity: 1
            }, 700, "linear", function () {
                $("#revert").show();
            });
        }
    });

    $("#revert").click(function () {
        $(".index-picture").animate({
            opacity: 0
        }, 700, "linear", function () {
            $(this).attr("src", "/static/images/Emerson.jpg");
        }).delay(500).animate({
            opacity: 1
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
