# DocumentAnalysisAI

Sistema de análise inteligente de documentos PDF utilizando Retrieval-Augmented Generation (RAG), embeddings e modelos de linguagem.

O projeto permite enviar um documento PDF, realizar perguntas sobre seu conteúdo e receber respostas fundamentadas nos trechos recuperados, com referências ao documento e às páginas.

## Tecnologias

- Python
- Sentence Transformers
- ChromaDB
- Google Gemini
- pypdf
- Streamlit

## Arquitetura

1. O usuário envia um documento PDF.
2. O sistema extrai o texto e identifica as páginas.
3. O conteúdo é dividido em trechos com sobreposição.
4. Um modelo multilíngue gera embeddings dos trechos.
5. Os embeddings são armazenados no ChromaDB.
6. A pergunta é convertida em embedding e os trechos mais relevantes são recuperados.
7. O Gemini utiliza o contexto recuperado para gerar a resposta.
8. A interface apresenta a resposta e as fontes consultadas.

## Modelos utilizados

**Embeddings:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

**LLM:** Gemini 3.5 Flash-Lite, acessado pela API do Google.

## Funcionalidades

- Upload de documentos PDF.
- Extração de texto por página.
- Busca semântica com embeddings.
- Respostas em português utilizando RAG.
- Exibição dos trechos e páginas recuperadas.
- Identificação de perguntas sem informações suficientes no documento.

## Como executar

Recomenda-se Python 3.12.

Clone o repositório:

```bash
git clone https://github.com/felipemtrindade/DocumentAnalysisAI.git
cd DocumentAnalysisAI
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz:

```dotenv
GEMINI_API_KEY=sua_chave_aqui
```

A chave pode ser obtida no [Google AI Studio](https://aistudio.google.com/apikey).

Execute:

```bash
streamlit run app/streamlit_app.py
```

Acesse `http://localhost:8501`.

## Testes realizados

O sistema foi testado com um manual público de PDF/A contendo 13 páginas.

**Pergunta:** Como salvar um arquivo em PDF/A?

**Resultado:** o sistema recuperou instruções relacionadas ao Microsoft Word, LibreOffice e PDF Creator, apresentando referências às páginas utilizadas.

**Pergunta:** Quem é o presidente da Mongólia?

**Resultado:** o sistema informou que a informação não estava presente no documento.

Esses são testes manuais iniciais, não uma avaliação completa da qualidade das respostas.

## Limitações

- PDFs digitalizados sem texto selecionável ainda não são suportados.
- O projeto processa um documento por vez.
- A busca semântica pode não recuperar todos os trechos necessários para responder perguntas complexas.
- As referências apresentadas são provenientes dos trechos recuperados, mas ainda não existe validação automática de todas as afirmações geradas.
- O sistema depende de conexão com a internet e de acesso à API Gemini.
- O desempenho pode variar conforme o tamanho e a estrutura do PDF.

## Melhorias futuras

- Melhorar a divisão e recuperação dos trechos.
- Implementar testes automatizados para avaliar a recuperação de informações.
- Suportar múltiplos documentos.
- Adicionar OCR para PDFs digitalizados.
- Implementar validação das citações.
- Disponibilizar uma demonstração pública.