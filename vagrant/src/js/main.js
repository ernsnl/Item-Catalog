function connect(type) {
    if (type == 'facebook') {
        handleFacebook()
    }
}

function handleFacebook() {
    FB.getLoginStatus(function(response) {
        console.log(response)
        if (response.status != 'connected') {
            FB.login(function(response) {
                console.log(response)
                if (response.status === 'connected') {
                    FB.api('/' + response.authResponse.userID + '?fields=id,name,email,picture',
                        function(infoResponse) {
                            console.log(infoResponse);
                            if (infoResponse && !infoResponse.error) {
                                sendlogininfo('facebook', infoResponse.name, infoResponse.email, infoResponse.picture.data.url)
                            }
                        });
                } else if (response.status === 'not_authorized') {
                    alert('You did not authorize our app. :(')
                }
            }, {
                scope: 'public_profile,email'
            });
        }
    });
}

function renderButton() {
    gapi.load('auth2', function() {
        // Retrieve the singleton for the GoogleAuth library and set up the client.
        auth2 = gapi.auth2.init({
            client_id: '781690799289-2q0asjktodv4j1nlf5vu6mu34cr1h7i2.apps.googleusercontent.com',
            cookiepolicy: 'single_host_origin',
            // Request scopes in addition to 'profile' and 'email'
            //scope: 'additional_scope'
        });
        attachSignin(attachSignin(document.getElementById('google-signin')));
    });
}

function attachSignin(element) {
    auth2.attachClickHandler(element, {},
        function(googleUser) {
            var profile = googleUser.getBasicProfile();
            sendlogininfo('google', profile.getName(), profile.getEmail(), profile.getImageUrl())
        },
        function(error) {
            console.log(error);
        });
}

function sendlogininfo(type, name, email, profile_pic) {
    $.ajax({
        url: '/connect',
        dataType: 'text',
        data: {
            type: type,
            name: name,
            email: email,
            picture_url: profile_pic,
            CSRFToken: $('#CSRFToken').val()
        },
        beforeSend: function() {
            console.log('Disable other sign in links.')
        },
        error: function(response) {
            alert("Something went wrong! :(")
        },
        method: 'GET',
        success: function(response) {
            if (response == 'OK') {
                $('.transition-filter').removeClass('hidden');
                document.location.reload();
            } else {
                alert('Something went wrong!')
            }
        },
    });
}

function disconnect(type) {
    $.ajax({
        url: '/disconnect',
        dataType: 'text',
        data: {
            CSRFToken: $('#CSRFToken').val()
        },
        error: function(response) {
            alert("Something went wrong! :(")
        },
        method: 'GET',
        success: function(response) {
            if (response == 'OK') {
                if (type == 'google') {
                    var auth2 = gapi.auth2.getAuthInstance();
                    auth2.signOut().then(function() {
                        console.log('User signed out.');

                    });
                } else if (type == 'facebook') {

                }
                $('.transition-filter').removeClass('hidden');
                document.location.reload();
            }
        },
    });

}
