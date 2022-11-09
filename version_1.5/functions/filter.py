from config import *

filtro = ('alert.','<script>','<','>','javascript',';','--',",","=","+",'/',"'",'"',"src=","admin'--"
            ,"or 1=1", "delete from user", "document.write","sessionStorage.","Window.","document.",'href=',"]>")


def filtro(email: str):
    for f in filtro: # laço de repetição que verifica se não há um texto suspeito de possuir injeção XSS ou SQL.
        if f in email:
            resposta = email.replace(f,'')
    if resposta == '' and len(resposta)<=4 or '@' not in resposta:
        resposta = None
    return resposta

a = 'pato<script>@g.c'

resposta = filtro(a)
print(resposta)