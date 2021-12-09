import json, re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def tempo():
    html = urlopen("https://tempo.cptec.inpe.br/pr/maringa")
    bs = BeautifulSoup(html, 'html.parser')

    linhas = bs.find_all('div', {'class':'previsao text-center'})
    data = ""
    #l = []
    for tag in linhas:
        dia = tag.findChildren("span", {"class": "font-weight-bold text-uppercase"})
        data = data + dia[0].text.replace("\n", "") + "\n"
        date = tag.findChildren("small")
        data = data + date[0].text.replace("\n", "")
        previsao = tag.findChildren("div", {"class": "text-center mt-2 ml-2"})
        if previsao[0].text.replace("\n", ""):
            data = data + "\n" + previsao[0].text.replace("\n", "")
        previsao = tag.findChildren("div", {"class": "text-center mt-2 ml-2"})
        data = data + "\n" + previsao[-2].text.replace("\n", "") + "\n"
        previsao = tag.findChildren("div", {"class": "text-center mt-2 ml-2"})
        data = data + previsao[-1].text.replace("\n", "") + "\n"
        temperatura = tag.findChildren("div", {"class": "d-flex flex-column"})
        data = data + temperatura[0].text.replace("\n", "") + "\n"
        temperatura = tag.findChildren("div", {"class": "d-flex flex-column"})
        data = data + temperatura[1].text.replace("\n", "") + "\n"
        sol = tag.findChildren("div", {"class": "d-flex flex-column nascer-por-sol"})
        sol = re.findall("[0-5][0-9]", sol[0].text)
        data = data + f"Nascer do sol {sol[0]}:{sol[1]}\nPôr do sol {sol[2]}:{sol[3]}\n\n"
        #l.append(data)

    #data = f"{dia[0].text}, {data[0].text}, {previsao[0].text}, {previsao[-1].text}, {previsao[-2].text}, {temperatura[0].text}, {temperatura[1].text}, nascer do sol {sol[0]}:{sol[1]} pôr do sol {sol[2]}:{sol[3]}"

    #print(data)
    #print(l)
    return data
#tempo()
    #with open("tempo.json", "w", encoding='utf-8') as tempo:
    #    json.dump(dicionario, tempo, ensure_ascii=False, indent = 2)
#f = "refrigerante"
#print(f[0:1])