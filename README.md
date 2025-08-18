# web-crawling
web crawling

Linguagem: Python
Sistema Operacional: Windows
Banco de dados: Mysql

Instalações necessárias para a execução do projeto:

pip install bs4
pip install nltk
pip install textstat
pip install textblob
pip install mysql-connector-python


Motivo da escolha das bibliotecas utilizadas:


### 🟢 **BeautifulSoup**

* **Motivo da escolha**: É uma das bibliotecas mais simples e robustas para **web scraping e parsing de HTML**.
* **Função no projeto**: Extrair o conteúdo bruto dos artigos (título, parágrafos, links, etc.) a partir do HTML coletado.
---

### 🟢 **NLTK (Natural Language Toolkit)**

* **Motivo da escolha**: Biblioteca padrão para **processamento de linguagem natural** (NLP).
* **Função no projeto**:

  * Tokenizar textos em palavras e frases.
  * Remover pontuações.
  * Contar palavras curtas, longas e únicas.
---

### 🟢 **textstat**

* **Motivo da escolha**: Especializada em calcular **métricas de legibilidade**.
* **Função no projeto**: Gerar indicadores como:

  * Índice de Flesch
  * Flesch-Kincaid
  * SMOG
  * Coleman-Liau

---

### 🟢 **TextBlob**

* **Motivo da escolha**: Simples e eficaz para **análise de sentimento e subjetividade**.
* **Função no projeto**: Calcular sentimento positivo/negativo e subjetividade do texto.
---

### 🟢 **mysql-connector-python**

* **Motivo da escolha**: Conexão do python com Mysql para estruturaçõ dos dados.
* **Função no projeto**:

  * Criar a tabela `content_tech`.
  * Inserir artigos processados.
  * Implementar carga incremental (verificação por `url` + `frases`).
  * Garante persistência dos dados já processados.
  * Evita duplicidade.

---

✅ **Resumo da justificativa**:
Essas bibliotecas foram escolhidas porque, em conjunto, elas possibilitam:

* **Coleta** (BeautifulSoup)
* **Pré-processamento linguístico** (NLTK)
* **Métricas objetivas de legibilidade** (textstat)
* **Métricas subjetivas e emocionais** (TextBlob)
* **Persistência incremental confiável** (mysql-connector-python)

