from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.text_splitter import CharacterTextSplitter

texto_base = """
Redes neurais artificiais são modelos computacionais inspirados no funcionamento do cérebro humano. 
Elas são compostas por camadas de neurônios artificiais que processam informações para aprender padrões a partir de dados. 
São amplamente usadas em tarefas de reconhecimento de voz, visão computacional, processamento de linguagem natural, entre outras.
"""

text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
chunks = text_splitter.split_text(texto_base)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

vectorstore = FAISS.from_texts(chunks, embeddings)

llm = Ollama(model="llama2")

retrieval_qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

def perguntar(pergunta):
    resposta = retrieval_qa.run(pergunta)
    return resposta

if __name__ == "__main__":
    pergunta_usuario = input("Digite sua pergunta: ")
    resposta = perguntar(pergunta_usuario)
    print("\nResposta:", resposta)