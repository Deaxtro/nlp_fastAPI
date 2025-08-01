FROM public.ecr.aws/lambda/python:3.10

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt && python -m textblob.download_corpora
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]