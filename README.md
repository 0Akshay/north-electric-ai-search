# North Electric: AI Search Website

This project is a web-based application built with **FastAPI**, **Jinja2 templates**, and **Bootstrap**, providing multiple static content pages and an AI-powered search interface.

## Tech Stack

- **Backend**: FastAPI
- **Templating**: Jinja2 (`Jinja2Templates`)
- **Frontend**: HTML5, Bootstrap 5, Custom CSS
- **JavaScript**: Vanilla JS for chat message handling

## Install
```bash
pip install -r requirements.txt
```

## Configure
Create a .env file and add the following key value pairs:
```env
ENDPOINT=<Azure search endpoint>
INDEX_NAME=<Name of the index on Azure>
ADMIN_KEY=<Azure service admin key>
```


## Run
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
or
```bash
run.bat
```

## Access from LAN
1. Find your local IP (ipconfig / ifconfig)
2. Open http://<your-ip>:8000 from another device on the same network
