import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://tempo.cptec.inpe.br/pr/maringa")
bs = BeautifulSoup(html, 'html.parser')
#print(bs)
lista, lista2 = [], []
dicionario = {}

linhas = bs.find_all('div', {'class':'previsao text-center'})
for item in linhas:
    lista.append(item.text)
    #print(type(item.text))
    #texto = item.text
    #tratamento = texto.split("\n")
    #for t in tratamento:
    #    print(t.split("/"))
    #print(tratamento.split(","))
   #if "-" in item:
    #print(texto)
    lista = lista[0].split("\n")

    for indice, valor in enumerate(lista):
        if valor != "":
            lista2.append(valor)
            #print(valor)
            tag = valor
            for i in range(len(lista2)):
                if tag == "Temperatura":
                    dicionario["Temperatura maxima"] = lista[indice+1]
                    dicionario["Temperatura minima"] = lista[indice+2]
                if ":" in tag:
                    dicionario["Nascer do sol"] = lista[indice-4]
                    dicionario["Pôr do sol"] = lista[indice]
                print(tag)
                #if isinstance(tag, int):
                #else:
                #    tags = []
                #    for t in dicionario:
                #        if tag != dicionario[t]:
                #            tags.append(tag)
                #    for tg in tags:
                #        dicionario[tg] = lista[indice+1]

    with open("tempo.json", "w", encoding='utf-8') as tempo:
        json.dump(dicionario, tempo, ensure_ascii=False, indent = 2)