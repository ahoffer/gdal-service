# set base image
FROM osgeo/gdal:ubuntu-small-3.3.1

# install pip
RUN apt install -y python3-pip

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
#COPY src/ .
#COPY test/resources/ ./test/resources/

EXPOSE 5000

# command to run on container start
CMD [ "python", "./server.py" ]