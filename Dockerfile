FROM python:3.11-slim


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 7860

ENV GRADIO_SERVER_NAME="0.0.0.0"
ENV GRADIO_SERVER_PORT=7860
ENV PYTHONUNBUFFERED=1


CMD ["python", "main.py"]