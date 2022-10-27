// Criar a função de cadastrar
function cadastrar(){

    // Resgatar os dados do HTML
    cad_email = document.getElementById('cadastroEmail').value;
    cad_username = document.getElementById('cadastroUsuario').value;
    cad_password = document.getElementById('cadastroSenha').value;
    cad_objective = document.getElementById('cadastroObjetivo').value;

    // Criar uma variável que recebe os dados em JSON
    var data = JSON.stringify({email: cad_email, nome: cad_username, senha: cad_password, objetivo: cad_objective})

    // Enviar os dados para o backend usando o ajax
    $.ajax({
        url: 'http://localhost:5000/cadastro',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: data,
        success: function() {
            alert("Dados enviados com sucesso!");
            window.location.assign('/login');
        },
        error: function() {
            alert("Erro ao contatar backend!")
        }
    })
}