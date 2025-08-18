import requests
from bs4 import BeautifulSoup
import pandas as pd

import nltk
import textstat
from textblob import TextBlob

import re
from connection import inserir_content_tech
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
        "subjetividade": round(subjetividade, 3)
    }

url = "https://www.alura.com.br/empresas/artigos/tendencias-tech-2025?srsltid=AfmBOorTUjmlg_HgHICmsI6k_WNMKhE9e50nysJSAUNIE23yooqb34CV"
#url alura
def get_content(url,tag):
    # Faz a requisição HTTP
    response = requests.get(url)
    paragraphs = []
    # Verifica se a requisição deu certo
    if response.status_code == 200:
        # Extrai o conteúdo HTML
        soup = BeautifulSoup(response.text, "html.parser")
        # with open("pagina.html", "w", encoding="utf-8") as f:
        #     f.write(str(soup))
        # print("Soup:" , soup)

        # elementos_strong = soup.find_all("strong")

        # print("Conteúdo entre <strong>:</n>")
        # for i, elem in enumerate(elementos_strong, start=1):
        #     texto = elem.get_text(strip=True)
        #     if texto:  # Ignorar vazio
        #         print(f"{i}. {texto}")
        
        # # Procura por todos os títulos de notícia
        # titulos = soup.find_all("h2")  # Geralmente títulos estão em <h2>

        # print("Títulos encontrados:\n")
        # for i, titulo in enumerate(titulos, start=1):
        #     texto = titulo.get_text(strip=True)
        #     if texto:  # Ignorar elementos vazios
        #         print(f"{i}. {texto}")

        ps = soup.find_all(tag)  

        print("P encontrados:\n")
        for i, p in enumerate(ps, start=1):
            texto = p.get_text(strip=True)
            if texto:  # Ignorar elementos vazios
                print(f"{i}. {texto}")
                metricas = calcular_metricas(texto)
                metricas["frases"] = texto
                metricas["url"] = url
                response = inserir_content_tech(metricas)
                print("Response:", response)
                paragraphs.append(metricas)
                #paragraphs.append(texto)
        return paragraphs
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return []

paragraphs = get_content(url=url,tag="p")

print("Estamos aqui")

# df = pd.DataFrame(paragraphs)

new_url = "https://www.cnnbrasil.com.br/tecnologia/sxsw-2025-conheca-as-10-tecnologias-que-devem-revolucionar-o-mundo/"
#url cnn
new_content = get_content(url=new_url,tag="p")

# new_df = pd.DataFrame(new_content)

#url_olhar_digital
last_url = "https://olhardigital.com.br/2025/03/13/pro/as-10-tecnologias-que-vao-abalar-2025-segundo-o-mit/"
last_content = get_content(url=last_url,tag="p")


# last_df = pd.DataFrame(last_content)
#print(last_df)





