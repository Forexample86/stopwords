FROM python:3

RUN mkdir /code
WORKDIR /code

COPY . /code/.ssh
RUN cd /code
RUN pip install -r requirements.txt
CMD ["ssh","-T","git@gitlab.com"]
ENTRYPOINT ["python3", "main.py"]
