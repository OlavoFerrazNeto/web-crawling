import requests
from bs4 import BeautifulSoup
import pandas as pd

import nltk
import textstat
from textblob import TextBlob

import re

nltk.download("punkt")
nltk.download("punkt_tab")  

def calcular_metricas(texto):
    # Tokenização
    palavras = nltk.word_tokenize(texto, language="portuguese")
    palavras_sem_pontuacao = [p for p in palavras if p.isalpha()]
    palavras_unicas = set(palavras_sem_pontuacao)
    frases = nltk.sent_tokenize(texto, language="portuguese")

    # Estrutura
    qtd_palavras = len(palavras_sem_pontuacao)
    qtd_frases = len(frases)
    qtd_caracteres = len(texto)
    media_palavras_frase = qtd_palavras / qtd_frases if qtd_frases else 0
    proporcao_unicas = len(palavras_unicas) / qtd_palavras if qtd_palavras else 0
    proporcao_maiusculas = sum(1 for c in texto if c.isupper()) / qtd_caracteres if qtd_caracteres else 0
    palavras_curtas = sum(1 for p in palavras_sem_pontuacao if len(p) <= 4)
    palavras_longas = sum(1 for p in palavras_sem_pontuacao if len(p) >= 7)

    # Legibilidade
    flesch = textstat.flesch_reading_ease(texto)
    flesch_kincaid = textstat.flesch_kincaid_grade(texto)
    smog = textstat.smog_index(texto)
    coleman_liau = textstat.coleman_liau_index(texto)

    # Sentimento e subjetividade
    sentimento = TextBlob(texto).sentiment.polarity
    subjetividade = TextBlob(texto).sentiment.subjectivity

    return {
        "quantidade_palavras": qtd_palavras,
        "qtd_frases": qtd_frases,
        "quantidade_caracteres": qtd_caracteres,
        "media_palavras_frase": round(media_palavras_frase, 2),
        "proporcao_unicas": round(proporcao_unicas, 3),
        "proporcao_maiusculas": round(proporcao_maiusculas, 3),
        "palavras_curtas": palavras_curtas,
        "palavras_longas": palavras_longas,
        "flesch": round(flesch, 2),
        "flesch_kincaid": round(flesch_kincaid, 2),
        "smog": round(smog, 2),
        "coleman_liau": round(coleman_liau, 2),
        "sentimento": round(sentimento, 3),
        "subjetividade": round(subjetividade, 3),
    }

# URL do site que vamos "raspar"
url = "https://www.alura.com.br/empresas/artigos/tendencias-tech-2025?srsltid=AfmBOorTUjmlg_HgHICmsI6k_WNMKhE9e50nysJSAUNIE23yooqb34CV"

# Faz a requisição HTTP
response = requests.get(url)
paragraphs = []
# Verifica se a requisição deu certo
if response.status_code == 200:
    # Extrai o conteúdo HTML
    soup = BeautifulSoup(response.text, "html.parser")
    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Soup:" , soup)

    elementos_strong = soup.find_all("strong")

    print("Conteúdo entre <strong>:</n>")
    for i, elem in enumerate(elementos_strong, start=1):
        texto = elem.get_text(strip=True)
        if texto:  # Ignorar vazio
            print(f"{i}. {texto}")
    
    # Procura por todos os títulos de notícia
    titulos = soup.find_all("h2")  # Geralmente títulos estão em <h2>

    print("Títulos encontrados:\n")
    for i, titulo in enumerate(titulos, start=1):
        texto = titulo.get_text(strip=True)
        if texto:  # Ignorar elementos vazios
            print(f"{i}. {texto}")

    ps = soup.find_all("p")  # Geralmente títulos estão em <h2>

    print("P encontrados:\n")
    for i, p in enumerate(ps, start=1):
        texto = p.get_text(strip=True)
        if texto:  # Ignorar elementos vazios
            print(f"{i}. {texto}")
            metricas = calcular_metricas(texto)
            metricas["frases"] = texto
            paragraphs.append(metricas)
            #paragraphs.append(texto)
else:
    print(f"Erro ao acessar a página: {response.status_code}")


print("Estamos aqui")
df = pd.DataFrame(paragraphs)
df["media_tamanho_palavra"] = df["quantidade_caracteres"] / df["quantidade_palavras"]

print(df)
