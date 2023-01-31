FROM python:3.6 
ENV GROUP_NUMBER=0
RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
WORKDIR /practica_creativa2/bookinfo/src/productpage
RUN sed -i "s/urllib3==1.26.5/urllib3==1.24.3/g" requirements.txt
RUN python3 -m pip install -r requirements.txt
WORKDIR /practica_creativa2/bookinfo/src/productpage/productpage/templates/
EXPOSE 9080
CMD sed -i "s/Simple\sBookstore\sApp/g${GROUP_NUMBER}/g" index.html; \
    sed -i "s/Simple\sBookstore\sApp/g${GROUP_NUMBER}/g" productpage.html; \
    python3 /practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080

# docker build -t g29/product-page-mono .