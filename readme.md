# Hello Reader
This was created with the help of a tutorial ([link](https://youtu.be/F4nwRQPXD8w)). But their code isn't working for some reason, as of the time of writing - Django has never supported WebSocket connections using the runserver command out of the box. It has always required an additional server or middleware to handle WebSocket connections.

*UPDATE!: Their code didn't work because of the channels version, you can change it to 3.0.5, and it'll work, all the latests versions work with Daphne.*

This project uses Daphne instead of runserver. Daphne is a production-ready ASGI server for Django, so it is designed to work with Django web applications.

To start:
```sh
cd chat-app
# create virtual environment
py -m venv venv
# activate 
venv\Scripts\activate
# install requirements and dependencies
pip install -r requirements.txt
# start server
daphne core.asgi:application

```