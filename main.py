
from dotenv import load_dotenv
load_dotenv()
import app as functions

import gradio as gr
from dotenv import load_dotenv
load_dotenv()

def predict(message, history):
    if len(message.get("files"))!=0:
        paths = message.get("files")
        files_data = functions.load_files(paths)
        split_docs = functions.split_documents(files_data)
        functions.store_data(split_docs)
    context = functions.similiarity_search(message["text"])
    answer = functions.get_answer(context, message["text"])

    return answer

gr.ChatInterface(predict,
                 multimodal=True).launch()