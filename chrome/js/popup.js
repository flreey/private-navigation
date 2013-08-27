var show = function(id){
  $('#login').hide();
  $('#link').hide();
  $(id).show();
}

chrome.cookies.get({"url": domain, "name": 'user_id'}, function(cookie){
    if (cookie) {
      show('#link');
    } else {
      show('#login');
    }
})

$('#login-form').on('submit', function(){
    var email = $('#inputEmail').val().trim();
    var password = $('#inputPassword').val().trim();
    if (email === '' || password === '') {
      return false;
    }

    $.post(domain+'/api/login', {email: email, password: password}, function(data){
        $('#inputEmail').val(email);
        $('#inputPassword').val('');

        if (data.code === 0){
          show('#link');
          $('.form-group').removeClass('has-error');
        } else {
          show('#login');
          $('.form-group').addClass('has-error');
        }
    })
    return false;
})

$('#link-form').on('submit', function(){
    var url = $('#inputUrl').val().trim();
    var name = $('#inputName').val().trim();
    console.log(url);
    $.post(domain+'/api/website', {'title': name, 'url': url}, function(data){
        if (data.code === 0){
          $('.form-group').removeClass('has-error');
          window.close();
        } else {
          $('.form-group').addClass('has-error');
        }
    })
    return false;
})

$('#sign-up').on('click', function(){
    chrome.tabs.create({"url": domain, "active": true}, function(){

    })
})

chrome.browserAction.onClicked.addListener(function(tab){
    console.log(tab);
})

document.addEventListener('DOMContentLoaded', function(){
    chrome.tabs.getSelected(null, function(tab){
        $('#inputUrl').val(tab.url);
        $('#inputName').val(tab.title);
    })
})
