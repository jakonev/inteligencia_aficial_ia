import random
import re
import string
# pip install bs4
import urllib.request

import bs4 as bs
import nltk
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

spacy.__version__

nltk.download('punkt')

nltk.__version__

# !python3 -m spacy download pt

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')
dados = dados.read()
dados

dados_html = bs.BeautifulSoup(dados, 'lxml')
# dados_html

paragrafos = dados_html.find_all('p')

len(paragrafos)

paragrafos[0]

paragrafos[0].text

conteudo = ''
for p in paragrafos:
    conteudo += p.text

    conteudo

conteudo = conteudo.lower()
conteudo

lista_sentencas = nltk.sent_tokenize(conteudo)

pln = spacy.load('pt_core_news_sm')

stop_words = spacy.lang.pt.stop_words.STOP_WORDS

b = string.punctuation


def preprocessamento(texto):
    # URLs
    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)

    # Espaços em branco
    texto = re.sub(r" +", ' ', texto)

    documento = pln(texto)
    lista = []
    for token in documento:
        lista.append(token.lemma_)

    lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in string.punctuation]
    lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

    return lista


texto_teste = 'https://www.iaexpert.com.br ' + lista_sentencas[0]

resultado = preprocessamento(texto_teste)

lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
    lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))

for _ in range(5):
    i = random.randint(0, len(lista_sentencas) - 1)
    lista_sentencas[i]
    lista_sentencas_preprocessada[i]
    print('-----')

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae', 'diga', 'ok', 'fala', 'brother', 'brow', 'firmeza', 'topa')
textos_boas_vindas_respostas = (
'hey, como posso ajudar?', 'olá, como posso ajudar?', 'oi, como posso ajudar?', 'digo, oi, posso ajudar',
'olá suas perguntas são valiosas', 'oi, quer saber mais sobre IA', 'hey, digite sua dúvida')
textos_saida = ('sair', 'tchau', 'exit', 'esc', 'fui', 'desligar', 'off')

'olá tudo bem'.split()


def responder_saudacao(texto):
    for palavra in texto.split():
        if palavra.lower() in textos_boas_vindas_entrada:
            return random.choice(textos_boas_vindas_respostas)


responder_saudacao('olá tudo bem?')
frases_teste = lista_sentencas_preprocessada[:3]
frases_teste.append(frases_teste[0])
vetores_palavras = TfidfVectorizer()
palavras_vetorizadas = vetores_palavras.fit_transform(frases_teste)


# print(vetores_palavras.get_feature_names_out())

def responder(texto_usuario):
    resposta_chatbot = ''
    lista_sentencas_preprocessada.append(texto_usuario)
    tfidf = TfidfVectorizer()
    palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_preprocessada)
    similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)
    indice_sentenca = similaridade.argsort()[0][-2]
    vetor_similar = similaridade.flatten()
    vetor_similar.sort()
    vetor_encontrado = vetor_similar[-2]
    if (vetor_encontrado == 0):
        resposta_chatbot = resposta_chatbot + 'Desculpe, mas não entendi!'
        return resposta_chatbot
    else:
        resposta_chatbot = resposta_chatbot + lista_sentencas[indice_sentenca]
        return resposta_chatbot


continuar = True
print('Olá, sou um chatbot e vou responder perguntas sobre inteligência artificial: ')
while (continuar == True):
    texto_usuario = input()
    texto_usuario = texto_usuario.lower()
    if (texto_usuario != 'sair'):
        if (responder_saudacao(texto_usuario) != None):
            print('Chatbot: ' + responder_saudacao(texto_usuario))
        else:
            print('Chatbot: ')
            print(responder(preprocessamento(texto_usuario)))
            lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
    else:
        continuar = False
        print('Chatbot: Até breve!')
