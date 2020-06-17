FROM ubuntu:16.04
RUN apt-get -y update 
Run apt-get -y upgrade 
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install flask pymongo
RUN mkdir /movies
RUN mkdir -p /movies/templates
COPY movies.py /movies/movies.py
ADD templates /movies/templates
EXPOSE 5000
WORKDIR /movies
ENTRYPOINT ["python3","-u","movies.py"]
