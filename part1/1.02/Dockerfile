FROM node:16

LABEL maintainer="marko.tuononen@gmail.com"

RUN useradd --create-home appuser
WORKDIR /home/appuser

ADD package*.json /home/appuser/
RUN npm install

USER appuser
ADD server.js /home/appuser/

EXPOSE 8000
CMD ["node", "server.js"]
