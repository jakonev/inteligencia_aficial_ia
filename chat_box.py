import re
# pip install bs4
import urllib.request

import bs4 as bs
import nltk
from numpy.random import choice
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# import spacy
# pip install spacy

# spacy.__version__
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

lista_sentencas = nltk.sent_tokenize(conteudo)


# nlp = spacy.load("pt_core_news_sm")

#
# stop_words = spacy.lang.pt.stop_words.STOP_WORDS
# # pontuações que o modelo irá ignorar
# stop_punct = string.punctuation
def preprocessamento(texto):  # preparando o texto para ser processado pelo spacy
    # tirar urls
    texto = re.sub(r"https?://[A-Za-z0-9./]+", ' ', texto)
    # tirar espaços em branco
    texto = re.sub(r" +", ' ', texto)
    # tirar radical (lematização)
    documento = texto
    input_user = ['porra']

    input_user = [palavra for palavra in input_user]
    input_user = ' '.join([str(elemento) for elemento in input_user if not elemento.isdigit()])
    return input_user

    return input_user


# guardar as sentenças que serão pré-processadas pela função em uma lista
lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
    lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae')
textos_boas_vindas_respostas = ('hey, como posso ajudar?', 'olá, como posso ajudar?', 'oi, como posso ajudar?')
textos_saida = ('sair', 'tchau', 'exit', 'esc')


def responder_saudacao(texto):
    for palavra in texto.split():
        if palavra.lower() in textos_boas_vindas_entrada:
            return choice(textos_boas_vindas_respostas)


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
        resposta_chatbot = 'Desculpe, mas não entendi!'

        return resposta_chatbot
    else:
        resposta_chatbot = lista_sentencas[indice_sentenca]

        return resposta_chatbot


while True:
    texto_usuario = input('Usuário: ').lower()
    if texto_usuario not in textos_saida:
        if responder_saudacao(texto_usuario) != None:
            print('Chatbot:', responder_saudacao(texto_usuario))
        else:
            print('Chatbot:', responder(preprocessamento(texto_usuario)))
            lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
    else:
        print('Chatbot: Até breve!')
        break
# TODO: importar a merda do spcacy ver https://github.com/HerikMuller2002/Estudo-Chatbots/blob/c991cd4052a18e1ccbe592634fb3434fb2723f97/chat%20base/app.py#L63