FROM python:3.11


RUN pip install bs4
RUN pip install requests
RUN pip install lxml


RUN mkdir -p /home/app

COPY . /home/app

CMD python3 home/app/scrapping.py