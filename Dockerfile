FROM python:3.9
WORKDIR /usr/src/app

COPY requirements/prod.txt ./
RUN pip install --no-cache-dir -r prod.txt

COPY . .

CMD [ "python", "src/prod.py" ]
