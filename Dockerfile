# basic python image
FROM nikolaik/python-nodejs:latest


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy over the api
COPY ./edge-api /usr/src/app/edge-api

# copy over the ui
COPY ./edge-ui /usr/src/app/edge-ui

# build the ui
RUN cd edge-ui && npm install && npm run build && cd ..

# copy the models over too 
COPY ./models /usr/src/app/models

# install the python requirements
RUN cd edge-api && pip install --no-cache-dir -r requirements.txt



# run the server
CMD [ "python", "./edge-api/server.py" ]


