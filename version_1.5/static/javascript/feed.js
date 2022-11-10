function exibirFeed() {
    var meuip = sessionStorage.getItem('meuip');
    $.ajax({
        url: `http://${meuip}:5000/feedlistar`,
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(resposta) {
        for (let i = resposta.length-1; i >= 0; i--) {
            console.log('Ta pedindo')
            document.getElementById('conteudo').innerHTML += 
            `<div class="border border-info bg-dark bg-gradient p-3 rounded text-center text-light">
                <p>Matéria:  ${resposta[i].materia}</p> 
                <p>Titulo: ${resposta[i].titulo}</p>
                <p>Conteudo: ${resposta[i].conteudo}</p>
                <p>Fontes: ${resposta[i].fontes}</p>
                <p>Postado por <i>${resposta[i].usuario_email}</i></p>
            </div> <br>`
        }
    }
}