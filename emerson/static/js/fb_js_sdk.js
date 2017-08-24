window.fbAsyncInit = function () {
    FB.init({
        appId: '340183253073041',
        autoLogAppEvents: true,
        xfbml: true,
        version: 'v2.10'
    });
    FB.AppEvents.logPageView();

    function statusChangeCallback(response) {
        console.log('statusChangeCallback');
        console.log(response);

        if (response.status === 'connected') {
            console.log("Logged in.");
        } else {
            console.log("Please log in.");
        }
    }

    FB.getLoginStatus(function (response) {
        statusChangeCallback(response);
    });
};

function importFacebookEvents() {
    FB.api(
        "/1039991669406220/events",
        function (response) {
            if (response && !response.error) {
                console.log(response || response.error);
                let eventsToImport = [];
                for (let i of response.data) {
                    let location = "";
                    if ("location" in i.place) {
                        if ("country" in i.place.location) {
                            location = i.place.location.country;
                        }
                        if ("city" in i.place.location) {
                            location = location + " " + i.place.location.city;
                        }
                        if ("street" in i.place.location) {
                            location = location + " " + i.place.location.street;
                        }
                    }
                    let event = {
                        'name': i.name,
                        'date': i.start_time,
                        'location': location,
                        'link': "https://www.facebook.com/events/" + i.id,
                        'remarks': "Facebook Event"
                    };
                    eventsToImport.push(event);
                }
                let stringifyConversion = {eventsToImport};
                $.ajax({
                    type: "POST",
                    url: "/admin/import_events",
                    data: JSON.stringify(stringifyConversion),
                    contentType: 'application/json;charset=UTF-8',
                    success: function (result) {
                        console.log(result);
                        location.href = result;
                    }
                });
            }
        }
    );
}

(function (d, s, id) {
    let js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
