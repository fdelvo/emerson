$(document).ready(function () {
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
        $(".mobile-nav").show();
        $("#open-nav").hide();
        $("#close-nav").show();
    });

    $("#close-nav").click(function () {
        $(".mobile-nav").hide();
        $("#open-nav").show();
        $("#close-nav").hide();
    });

    $('#dark-theme-off, #dark-theme-off-mobile').click(function () {
        sessionStorage.setItem('dark-theme', true);
        sessionStorage.setItem('bgColor', '#212121');
        sessionStorage.setItem('color', '#FBF9FA');
    });

    $('#dark-theme-on, #dark-theme-on-mobile').click(function () {
        sessionStorage.setItem('dark-theme', false);
        sessionStorage.removeItem('bgColor');
        sessionStorage.removeItem('color');
    });

    let darkTheme = sessionStorage.getItem('dark-theme');

    if (darkTheme === 'true') {
        $('#dark-theme-on, #dark-theme-on-mobile').show();
        $('#dark-theme-off, #dark-theme-off-mobile').hide();
        $('#dark-theme').css('color', '#ca519e');
        $('body, section, header').css({
            'background-color': sessionStorage.getItem('bgColor'),
            'color': sessionStorage.getItem('color')
        });
        $('h1, h2, h3, h4, h5, h6').css({
            'color': sessionStorage.getItem('color')
        })
    } else {
        $('#dark-theme-off, #dark-theme-off-mobile').show();
        $('#dark-theme-on, #dark-theme-on-mobile').hide();
    }
});
