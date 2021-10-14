FROM python:3.9
RUN apt-get update
RUN apt-get install git
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /root/.ssh/
ADD id_rsa /root/.ssh/id_rsa
ADD known_hosts /root/.ssh/known_hosts
RUN chmod 700 /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/known_hosts
RUN chown -R root:root /root/.ssh
#RUN touch /root/.ssh/known_hosts
#RUN ssh-keyscan bitbucket.org >> /root/.ssh/known_hosts
RUN mkdir /code
WORKDIR /code

COPY . .
ENTRYPOINT ["python3", "main.py"]
