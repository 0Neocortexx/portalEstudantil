// Cria a função do login
function login() {
    // Pega os dados do formulario
    log_email = document.getElementById('loginEmail').value;
    log_senha = document.getElementById('loginSenha').value;
    
    // Coloca os dados em JSON para enviar para o backend
    var dados = JSON.stringify({email: log_email, senha: log_senha})

    // Faz o envio via AJAX
    $.ajax({
        url: 'http://localhost:5000/login', // Chama a rota de login
        type: 'POST', // Requisição do tipo POST
        contentType: 'text/plain', // Content-type
        dataType: 'json', // Tipo de dado enviado (Em JSON)
        xhrFields: { withCredentials: true }, // Não sei o que é
        data: dados, // Dados enviados
        // Se os dados forem enviados
        success: function(retorno) { // Vai criar uma função
            if (retorno.resultado == "ok") { // se o resultado for positivo
                sessionStorage.setItem('email',retorno.email); 
                sessionStorage.setItem('jwt',retorno.detalhes);
                alert('Login relizado com sucesso!');
                window.location.assign('/');
            } else{
                alert(`Verifique se os dados estão corretos ${retorno.detalhes}`);
            };},
        error: function() {
            window.alert(`Login Incorreto. Verifique a senha,${retorno.detalhes}`)
        }
    })
}