let token = ''

function sendForm(form) {
    const XHR = new XMLHttpRequest();
    const FD = new FormData(form);
    XHR.addEventListener("load", function(event) {
        if(XHR.status == 200) {
            token = JSON.parse(XHR.response)
            console.log(token)
            logged_status.innerHTML = 'Logged in'
            token = token['access_token']
        }
    } );
    XHR.addEventListener("error", function( event) {
        console.log('Oops! Something went wrong.');
    } );
    XHR.open("POST", form.action);
    XHR.setRequestHeader('Content-Type', 'application/json')
    XHR.send(JSON.stringify(Object.fromEntries(FD)));
}


function open_protected() {
    const XHR = new XMLHttpRequest()
    XHR.addEventListener("load", function(event) {
        result.innerHTML = XHR.response
    } );
    XHR.addEventListener("error", function( event) {
        console.log('Oops! Something went wrong.');
    } );
    XHR.open("GET", '/protected')
    XHR.setRequestHeader('Authorization', 'JWT '+token)
    XHR.send()
}

function logout() {
    token = ''
    logged_status.innerHTML = 'Not logged in'
    result.innerHTML = ''
}