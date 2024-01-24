FROM python:3.11

WORKDIR /mdt/run

COPY . .
RUN pip install --upgrade pip \
    && pip install -i https://pypi.douban.com/simple/ -r requirements.txt \
    && chmod +x entrypoint.sh

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0"]
EXPOSE 8000