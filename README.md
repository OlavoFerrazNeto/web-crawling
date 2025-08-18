# 📌 Web Crawling e Análise de Texto

Projeto de **web crawling** e **análise de textos** com **persistência em banco de dados MySQL**.
O objetivo é coletar artigos da web, extrair o conteúdo em granularidade de frases, calcular métricas linguísticas e sentimentais e armazenar em banco de forma incremental (sem duplicações).

---

## 🛠️ Tecnologias utilizadas

* **Linguagem**: Python
* **Banco de dados**: MySQL
* **Sistema Operacional**: Realizado no Windows,

### Bibliotecas

* [BeautifulSoup4] → Parsing HTML e extração de conteúdo
* [NLTK] → Tokenização, análise de frases e palavras
* [textstat]→ Métricas de legibilidade
* [TextBlob] → Análise de sentimento e subjetividade
* [mysql-connector-python]→ Conexão com MySQL

---

## 📂 Estrutura do Projeto

```
web-crawling/
│
├── handler.py         # Orquestra o fluxo: scraping, cálculo de métricas e inserção no banco
├── connection.py      # Conexão com MySQL, criação da tabela, inserção incremental e leitura
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```

### 🔹 **handler.py**

* `calcular_metricas(texto)` → Calcula todas as métricas linguísticas e sentimentais.
* `get_content(url, tag)` → Faz scraping da URL, extrai parágrafos e insere no banco de forma incremental.

### 🔹 **connection.py**

* `conectar_mysql()` → Cria conexão com MySQL.
* `fechar_conexao(conexao)` → Fecha a conexão.
* `criar_tabela()` → Cria tabela `content_tech` se não existir.
* `inserir_content_tech(dados)` → Insere dados incrementalmente (verificando `url` + `frases`).
* `ler_todos_content_tech()` → Lê todos os registros da tabela.

---

## ⚙️ Instalação

### Clone o repositório

```bash
git clone https://github.com/OlavoFerrazNeto/web-crawling.git
cd web-crawling
```

### Crie um ambiente virtual

Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

Conteúdo de `requirements.txt`:

```
bs4
nltk
textstat
textblob
mysql-connector-python
```

### Configure o banco MySQL

Criação do banco mysql:

```sql
CREATE DATABASE database_on_case;
```

Configure o usuário e senha em `connection.py`.

Criação da tabela content_tech:
Execução da função criar_tabela do arquivo connection.py

### Execução do projeto

```bash
python handler.py
```

---

## Decisões tomadas

1. **Coleta de dados**: Optei pelo **BeautifulSoup** por ser simples e eficaz em parsing HTML.
2. **Processamento NLP**: Utilizei **NLTK** para tokenização e contagem de palavras/frases.
3. **Métricas de legibilidade**: Adicionei **textstat** por ser especializado nesses cálculos.
4. **Sentimento e subjetividade**: Escolhi **TextBlob** por oferecer API simples para análise emocional.
5. **Persistência incremental**: Usei `mysql-connector-python` para garantir que `url + frases` sejam únicos e evitar duplicações.
6. **Granularidade**: Decidi salvar os artigos em **frases**, pois facilita análises detalhadas.

---

## Métricas de Performance

* **Tempo médio de processamento por artigo**: \~2-4 segundos (dependendo do tamanho do texto).
* **Carga incremental**: Evita duplicações e mantém o banco sempre atualizado.
* **Escalabilidade**:

  * Em cenários maiores, recomenda-se:

    * Uso de **fila (RabbitMQ, Kafka)** para distribuir scraping.
    * **Paralelismo** com `asyncio` ou `multiprocessing`. Com o objetivo de executar várias tarefas ao mesmo tempo.
    * **Armazenamento distribuído** (PostgreSQL, BigQuery ou Data Lake).
    * **Agendador** (Cron) para rodar em um horário programado.

---

## Conclusão geral

Esse projeto permite:
- Coleta automatizada de artigos.
-Processamento linguístico e sentimental.
-Armazenamento incremental em banco MySQL.
-Pronto para consultas analíticas e escalável para cenários maiores.


