//chrome.cookies.get({url: 'http://localhost:8000', name: 'user_id'}, function(cookie){
    //if (cookie) {
      //$('#login').hide();
      //$('#link').show();
    //} else {
      //$('#login').show();
      //$('#link').hide();
    //}
//})

var login = function(){

}
$('#login-form').on('submit', function(){
    var email = $('#inputEmail').val().trim();
    var password = $('#inputPassword').val().trim();
    if (email === '' || password === '') {
      return false;
    }

    $.post(domain+'/login', {email: email, password: password}, function(data){
        console.log(data);
    })
    return false;
    //$.post()
})
