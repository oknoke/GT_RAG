FROM python:3.11-slim


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt
RUN pip installl --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 7860

CMD ["python", "main.py"]