FROM node:12.18.1-slim
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR /practica_creativa2/bookinfo/src/ratings
RUN mkdir /opt/microservices
RUN cp package.json /opt/microservices/
RUN cp ratings.js /opt/microservices/
WORKDIR /opt/microservices/
RUN npm install .
ENV SERVICE_VERSION v1
EXPOSE 9080
CMD ["node","/opt/microservices/ratings.js","9080"]

# docker build -t g29/ratings .