$(document).ready(function () {
    $(".index-picture").mouseenter(function () {
        var img = $(this).attr("src");
        if (img === "/static/images/Emerson.jpg") {
            $(this).attr("src", "/static/images/Emerson2.jpg");
        } else {
            $(this).attr("src", "/static/images/Emerson.jpg");
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
