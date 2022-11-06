function exibirDados() {
    document.getElementById('perfilNome').innerHTML = "Nome: " + sessionStorage.getItem('nome');
    document.getElementById('perfilEmail').innerHTML = "Email: " + sessionStorage.getItem('email');
}
function sair() {
    sessionStorage.clear();
    window.location.assign('/');
}
