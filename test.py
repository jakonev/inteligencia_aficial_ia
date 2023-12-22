import urllib.request

from chat_box import dados_html

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')
dados = dados.read()
dados
paragrafos = dados_html.find_all('p')

len(paragrafos)

paragrafos[0]

paragrafos[0].text

conteudo = ''
for p in paragrafos:
    conteudo += p.text

    conteudo
print(conteudo)
