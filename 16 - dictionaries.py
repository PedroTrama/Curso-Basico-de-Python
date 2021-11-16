monthConversions = {                            #tudo qdentro das chaves que segue esse padrao esta no dicionario
    "Jan": "Janeiro",                           #as chaves podem ser numeros tbm (ate sem as aspas)
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro",
}                                               #fim do dicionario

print(monthConversions)                         #printa eles em ordm
print(monthConversions["Nov"])                  #damos a chave e ele printa o valor associado aa chave (da erro se n tiver a chave)
print(monthConversions.get("Nov"))              #Assim, damos a chave e
print(monthConversions.get("Luv"))              #se NAO TIVER A CHAVE ele mostra que nao existe escrevendo NONE
print(monthConversions.get("Luv", "Invalido"))  #podemos ate nomear o erro