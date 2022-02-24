FROM python
WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

RUN . /code/ 


EXPOSE 8080