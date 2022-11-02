function inserirConteudo() {
    cont_usuario = sessionStorage.getItem('email');
    cont_materia = document.getElementById('conteudoDisciplina').value;
    cont_titulo = document.getElementById('conteudoTitulo').value;
    cont_conteudo = document.getElementById('conteudoTexto').value;
    cont_fontes = document.getElementById('conteudoReferencias').value;
     
    var dados = JSON.stringify({usuario: cont_usuario, materia: cont_materia, titulo: cont_materia, conteudo: cont_conteudo, fontes: cont_fontes})

    console.log(dados)
    $.ajax({
        url: 'http://localhost:5000/inserir_conteudo',
        type: 'POST',
        contentType: 'application/json',
        dataType: 'json',
        data: dados,
        success: function() {
            alert("Dados enviados com sucesso!");
            window.location.assign('/index');
        },
        error: function() {
            alert("Erro ao contatar backend!")
        }
    })
}