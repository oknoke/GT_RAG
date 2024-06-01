import asyncio
from concurrent.futures import ThreadPoolExecutor
from langchain_community.document_loaders import UnstructuredFileLoader
from loguru import logger



def load_files(paths):
    logger.debug(f"Loading PDF : {paths}")
    data =[]
    for path in paths:
        data.extend(UnstructuredFileLoader(path).load())
    return data