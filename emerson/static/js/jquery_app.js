$(document).ready(function () {
    function getRandomIntInclusive(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    $("#youtube-container").hide();
    $("#spotify").click(function () {
        $("#spotify-container").show();
        $("#youtube-container").hide();
    });

    $("#youtube").click(function () {
        $("#spotify-container").hide();
        $("#youtube-container").show();
    });

    $(".mobile-nav").hide();
    $("#close-nav").hide();

    $("#open-nav").click(function () {
        $(".main-nav").css('display', 'flex');
        $("#open-nav").hide();
        $("#close-nav").show();
    });

    $("#close-nav").click(function () {
        $(".main-nav").hide();
        $("#open-nav").show();
        $("#close-nav").hide();
    });

    $(".nav-link").click(function () {
        $(".main-nav").hide();
        $("#open-nav").show();
        $("#close-nav").hide();
    });

    let newsThumbnails = [
        "Emerson-min.jpg",
        "Emerson2-min.jpg",
        "JESSE-WIEBE-EP20170622-513_WEB.png",
        "JESSE-WIEBE-EP20170622-395_WEB.png",
        "JESSE-WIEBE-EP20170622-329-Zusatzmotiv_WEB.png",
        "JESSE-WIEBE-EP20170622-257_WEB.png",
        "JESSE-WIEBE-EP20170622-186_WEB.png",
        "JESSE-WIEBE-EP20170622-172_WEB.png"
    ];

    $(".news-thumbnail").each(function () {
        let imageUrl = newsThumbnails[getRandomIntInclusive(0, 7)];
        $(this).attr("src", "../static/images/" + imageUrl);
    });

    if (location.pathname === '/') {
        $('#branding').css({position: 'fixed', bottom: '0.5rem', right: '0.5rem'});
    }

    $("a[href*=\"#\"]").click(function (e) {
        e.preventDefault();

        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 400, 'linear');
    });
});
