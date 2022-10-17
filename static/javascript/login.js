function login() {
    log_email = document.getElementById('loginEmail').value;
    log_senha = document.getElementById('loginSenha').value;
    
    var dados = JSON.stringify({email: log_email, senha: log_senha})

    $.ajax({
        url: 'http://localhost:5000/login',
        type: 'POST',
        contentType: 'text/plain',
        dataType: 'json',
        xhrFields: { withCredentials: true },
        data: dados,
        success: function(retorno) {
            if (retorno.resultado == "ok") {
            sessionStorage.setItem('login', login);
            window.location.assign('/');
            }},
        error: function() {
            alert("Deu erro otaro");
        }
    })
}