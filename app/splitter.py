from langchain.text_splitter import RecursiveCharacterTextSplitter
from loguru import logger

def split_documents(blog_docs):
    logger.debug(f"Splitting documents : {len(blog_docs)}")
    # Create a RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=300,
        chunk_overlap=50)

    # Make splits
    splits = text_splitter.split_documents(blog_docs)
    logger.debug(f"Splitted into : {len(splits)}")
    return splits
