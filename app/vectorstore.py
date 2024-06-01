from loguru import logger
from app.embedding import get_embedding
from langchain_community.vectorstores import Chroma
vectorstore = Chroma(embedding_function=get_embedding())

def store_data(data):
    logger.debug(f"Storing New data : len(data) {len(data)}")
    vectorstore.add_documents(documents=data)
    logger.debug(f"Data stored")
    return True

def similiarity_search(query):
    logger.info(f"Vector Search : query '{query}'")
    res = vectorstore.similarity_search_with_relevance_scores(query=query,k=4,score_threshold=0.75)
    logger.info(f"Vector search result : len(res) {len(res)}")
    return res