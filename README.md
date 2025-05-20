# vb_faiss

Projeto simples de sistema de recuperação de informações utilizando embeddings de texto e banco vetorial FAISS, integrando modelos Ollama (`mxbai-embed-large` para embeddings e `llama2` para geração de respostas). Desenvolvido para Tópicos Avançados em Sistemas para Internet I.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com/) instalado e configurado localmente
- Git

---

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/ollama-embeddings-projeto.git
cd ollama-embeddings-projeto
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
```
No Powershell, ative seu ambiente virtual

```bash
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Execução

### 1. Inicie o Ollama

Certifique-se de que o Ollama esteja rodando antes de executar o script!

```bash
ollama run llama2
```

### 2. Em outro terminal, execute o script

```bash
python vb_faiss.py
```

### 3. Interaja com o sistema

Digite sua pergunta quando solicitado no terminal. O sistema retornará a resposta baseada no conteúdo do texto base usando o sistema de recuperação vetorial.


## Descrição do Projeto

- O texto base é dividido em chunks (pedaços menores).

- Cada chunk gera um vetor de embedding com o modelo mxbai-embed-large.

- Os embeddings são armazenados no banco vetorial FAISS.

- O modelo llama2 recebe a pergunta do usuário, converte em embedding, e recupera os chunks mais relevantes.

- Por fim, o modelo responde com base nesses chunks, gerando respostas contextualizadas.
