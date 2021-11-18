from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://tempo.cptec.inpe.br/pr/maringa")
bs = BeautifulSoup(html, 'html.parser')
#print(bs)

linhas = bs.find_all('div', {'class':'previsao text-center'})
for item in linhas:
    #print(type(item.text))
    texto = item.text
    tratamento = texto.split("\n")
    for t in tratamento:
        print(t.split("/"))
    #print(tratamento.split(","))
   #if "-" in item:
