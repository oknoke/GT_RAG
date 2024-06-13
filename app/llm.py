
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain import hub
from loguru import logger

template = """You are an assistant for question-answering tasks.
 Use the following pieces of retrieved context to answer the question. 
 If you don't know the answer  just say that you don't know.
Question: {question} 
Context: {context} 
Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
# Prompt

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")



def get_answer(messages):
    answer = llm.invoke(messages)
    logger.debug(f"llm answered  : answer.content {answer.content}")
    logger.debug(f"Tokens used : {answer.usage_metadata}")
    return answer.content