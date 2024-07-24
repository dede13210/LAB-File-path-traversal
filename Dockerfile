FROM alpine:3.7
RUN apk update --no-cache && apk add python3 python3-dev py3-pip bash
COPY . /lab
WORKDIR /lab/app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "api_server.py" ]