// Criar a função de cadastrar
function cadastrar(){
    var cad_email = document.getElementById('cadastroEmail').value;
    var cad_username = document.getElementById('cadastroUsuario').value;
    var cad_password = document.getElementById('cadastroSenha').value;
    var cad_objective = document.getElementById('cadastroObjetivo').value;
    var checkbox = document.getElementById('cadastroTermos').checked;
    var meuip = sessionStorage.getItem('meuip');

    // Criar uma variável que recebe os dados em JSON
    var data = JSON.stringify({email: cad_email, nome: cad_username, senha: cad_password, objetivo: cad_objective})

    // Enviar os dados para o backend usando o ajax
    $.ajax({
        url: `http://${meuip}:5000/cadastro`,
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: data,
        success: function(retorno) {
            if (retorno.resultado === 'injecao') {
                alert(retorno.detalhes);
                window.location.reload(true);
            } else if (retorno.resultado === 'vazio'){
                alert(retorno.detalhes);
                window.location.reload(true);
            } else if (retorno.resultado === 'invalido') {
                alert(retorno.detalhes);
            } else if (retorno.resultado === 'usuario_ja_cadastrado') {
                alert(retorno.detalhes);
            } else if(checkbox == false) {
                alert('Concorde com os termos de compromisso!')
            } else if(retorno.resultado ==='pequeno'){
                alert(retorno.detalhes)
            } else {
                alert(retorno.detalhes);
                window.location.assign('/main');
            };
        },
        error: function() {
            alert("Erro ao contatar backend!")
        }
    })}

// Cria a função do login
function login() {
    // Pega os dados do formulario
    var log_email = document.getElementById('loginEmail').value;
    var log_senha = document.getElementById('loginSenha').value;
    var filtragem = (log_email + log_senha).toLowerCase();
    var filterlink = ( log_email + log_senha).toLowerCase();
    var meuip = sessionStorage.getItem('meuip');

    if (log_email == '' || log_senha == '') {
        alert('Dá de fazer login vazio não cria {BLOQUEIO ANTI PAULO ATIVADO}')
        document.location.reload(true);
    } else if (filterlink.includes('www.' || filterlink.includes('.com') || filterlink.includes('http') || filterlink.includes('https://') || filterlink.includes('.br')) ) { 
        alert('Não insere link onde não pode seu pilantra #### BLOQUEIO ANTI PAULO');
        document.location.reload(true);
    }else if(filtragem.includes('<') == true || filtragem.includes('/') == true || filtragem.includes('script') == true || filtragem.includes('alert') || filtragem.includes('drop'))  {
        alert('ta inserindo bosta ai ne {PAULO SAI FORA} #### PROTEÇÃO ANTI PAULO ATIVADA');
        window.location.reload(true);
    } else { 
        // Coloca os dados em JSON para enviar para o backend
        var dados = JSON.stringify({email: log_email, senha: log_senha})
        // Faz o envio via AJAX
        $.ajax({
            url: `http://${meuip}:5000/login`, // Chama a rota de login
            type: 'POST', // Requisição do tipo POST
            contentType: 'text/plain', // Content-type
            dataType: 'json', // Tipo de dado enviado (Em JSON)
            xhrFields: { withCredentials: true }, // Não sei o que é
            data: dados, // Dados enviados
            // Se os dados forem enviados
            success: function(retorno) { // Vai criar uma função
                if (retorno.resultado == "ok") { // se o resultado for positivo
                    sessionStorage.setItem('email',retorno.email); 
                    sessionStorage.setItem('nome',retorno.nome);
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
}

function inserirConteudo() {
    var cont_usuario = sessionStorage.getItem('email');
    var cont_materia = document.getElementById('conteudoDisciplina').value;
    var cont_titulo = document.getElementById('conteudoTitulo').value;
    var cont_conteudo = document.getElementById('conteudoTexto').value;
    var cont_fontes = document.getElementById('conteudoReferencias').value;
    var checkbox = document.getElementById('conteudoConcordar').checked;
    var meuip = sessionStorage.getItem('meuip');

    var filtragem = (cont_materia + cont_titulo + cont_conteudo + cont_fontes).toLowerCase()
    var filterlink = ( cont_titulo + cont_conteudo).toLowerCase();

        if (cont_materia == '' || cont_titulo == '' || cont_conteudo == '' || cont_fontes == '') {
            alert('Dá de cadastrar conteudo vazio não cria {BLOQUEIO ANTI PAULO ATIVADO}');
            document.location.reload(true);
        } 

        else if (filterlink.includes('www.' || filterlink.includes('.com') || filterlink.includes('http') || filterlink.includes('https://') || filterlink.includes('.br')) ) { 
            alert('Não insere link onde não pode seu pilantra #### BLOQUEIO ANTI PAULO');
            document.location.reload(true);
        } 
        
        else if(filtragem.includes('<') == true || filterlink.includes('/') == true || filtragem.includes('script') == true || filtragem.includes('alert') || filtragem.includes('drop') || filtragem.includes('js') || filtragem.includes('select'))  {
            alert('ta inserindo bosta ai ne {PAULO SAI FORA} #### PROTEÇÃO ANTI PAULO ATIVADA');
            window.location.reload(true);
        } 
        
        else if(checkbox == false) {
            alert('Concorda com os termos ai miseravi, vai espalhar fake news nao')
        } 
        
        else {  
            // Dados em JSON
            var dados = JSON.stringify({usuario: cont_usuario, materia: cont_materia, titulo: cont_titulo, conteudo: cont_conteudo, fontes: cont_fontes})
                $.ajax({
                url: `http://${meuip}:5000/inserir_conteudo`,
                type: 'POST',
                contentType: 'application/json',
                dataType: 'json',
                data: dados,
                success: function() {
                    alert("Dados enviados com sucesso!");
                    window.location.assign('/');
                },
                error: function() {
                    alert("Erro ao contatar backend!")
                }
            })
}}

function exibirDados() {
    document.getElementById('perfilNome').innerHTML = "Nome: " + sessionStorage.getItem('nome');
    document.getElementById('perfilEmail').innerHTML = "Email: " + sessionStorage.getItem('email');
}

function sair() {
    sessionStorage.clear();
    window.location.assign('/');
}


function exibirBotao() {
    if(sessionStorage.getItem('email') == undefined){
        document.getElementById('botaoCadastro').style.display = 'inherit';
    } else {
        document.getElementById('botaoPerfil').style.display = 'inherit';
        document.getElementById('botaoInserir').style.display = 'inherit';
    }
}
