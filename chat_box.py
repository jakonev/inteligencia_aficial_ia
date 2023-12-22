# import bs4 as bs
# pip install bs4
import urllib.request
import re
import nltk
import numpy as np
import random
import string
import spacy
spacy.__version__
nltk.download('punkt')

nltk.__version__

# !python3 -m spacy download pt

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')
dados = dados.read()
dados

dados_html = bs.BeautifulSoup(dados, 'lxml')
dados_html

paragrafos = dados_html.find_all('p')

len(paragrafos)


paragrafos[0]

paragrafos[0].text

conteudo = ''
for p in paragrafos:
  conteudo += p.text

  conteudo
print(conteudo)

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae')
textos_boas_vindas_respostas = ('hey', 'olá', 'opa', 'oi', 'bem-vindo', 'como você está?')

'olá tudo bem'.split()

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return random.choice(textos_boas_vindas_respostas)


responder_saudacao('olá tudo bem?')

from sklearn.metrics.pairwise import cosine_similarity
palavras_vetorizadas[0].todense()
cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[1])

cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas[3])

similaridade = cosine_similarity(palavras_vetorizadas[0], palavras_vetorizadas)
similaridade

similaridade.argsort()
i = similaridade.argsort()[0][-2]
i

i = i.flatten()
i

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



