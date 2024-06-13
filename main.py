from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
from typing import Tuple
load_dotenv()
import app as functions
from loguru import logger
import sys
import os
import gradio as gr

template = """You are an assistant for question-answering tasks.
 If there is any additional context below you can use it to answer the question. 
 If you don't know the answer just say that you don't know.
Context: {context} 
"""

logger.remove()
logger.add(sys.stdout, level="DEBUG")
logger.add("app.log", level="DEBUG")
print("Logger initialized")

def is_image_file(path):
    _, ext = os.path.splitext(path)
    image_extensions = {'.png', '.jpg', '.jpeg',}
    return ext.lower() in image_extensions

def is_acceptable_file(path):
    _, ext = os.path.splitext(path)
    image_extensions = {'.pdf', ".xlsx",".csv",".docs",".docx",".text",".html"}
    return ext.lower() in image_extensions
def get_history(new,history):
    messages = []
    for i in history:
        if isinstance(i[0],tuple) and is_image_file(i[0][0]):
            messages.append(HumanMessage(content=[{"type":"image_url","image_url":i[0][0]},]))
        elif isinstance(i[0],str) and isinstance(i[1],str):
            messages.append(HumanMessage(content=i[0]))
            messages.append(AIMessage(content=i[1]))
    for i in new.get("files"):
        if is_image_file(i):
            messages.append(HumanMessage(content=[{"type":"image_url","image_url":i},]))
    messages.append(HumanMessage(content=new.get("text")))
    return messages

def predict(message, history):
    history_messages = get_history(message,history)

    if len(message.get("files"))!=0:
        paths = list(filter(is_acceptable_file, message.get("files")))
        if len(paths)>0:
            files_data = functions.load_files(paths)
            split_docs = functions.split_documents(files_data)
            functions.store_data(split_docs)
    context = functions.similiarity_search(message["text"])

    history_messages.insert(0,SystemMessage(content=template.format(context=context)))
    print(history_messages)
    logger.debug(f"LLM question : {history_messages[-1]}")
    answer = functions.get_answer(history_messages)

    return answer

gr.ChatInterface(predict,
                 multimodal=True).launch()