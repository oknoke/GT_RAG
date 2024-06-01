from langchain_openai import OpenAIEmbeddings
def get_embedding():
    embeddings = OpenAIEmbeddings()
    return embeddings