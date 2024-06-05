import asyncio
from concurrent.futures import ThreadPoolExecutor
from langchain_community.document_loaders import PyPDFLoader,TextLoader,UnstructuredFileLoader
from loguru import logger



def load_files(paths):

    data =[]
    for path in paths:
        if path.endswith(".pdf"):
            logger.debug(f"Loading PDF : {paths}")
            data.extend(PyPDFLoader(path).load())
        else:
            logger.debug(f"Loading files : {paths}")
            data.extend(UnstructuredFileLoader(path).load())
    return data