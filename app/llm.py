
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain import hub
from loguru import logger

template = """You are an assistant for question-answering tasks.
 Use the following pieces of retrieved context to answer the question. 
 If you don't know the answer and the context does not has the precise answer, just say that you don't know.
Question: {question} 
Context: {context} 
Answer:
"""

prompt = ChatPromptTemplate.from_template(template)
# Prompt

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

chain = prompt | llm


def get_answer(context,question):
    logger.debug(f"llm query : question {question}")
    answer = chain.invoke({"context":context,"question":question})
    logger.debug(f"llm answered  : len(answer.content) {len(answer.content)}")
    return answer.content