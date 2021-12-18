FROM ubuntu:20.04
EXPOSE 8000

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

ENV HOME /home
COPY app.py     /home/app.py   
COPY models     /home/models   
COPY rest       /home/rest     
COPY services   /home/services 
COPY static     /home/static   
COPY templates  /home/templates
COPY tests      /home/tests    
COPY views      /home/views
COPY requirements.txt /home/requirements.txt
STOPSIGNAL SIGTERM
WORKDIR /home

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
CMD ["tests/test_project.py"]