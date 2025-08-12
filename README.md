# North Electric: AI Search Website

This project is a web-based application built with **FastAPI**, **Jinja2 templates**, and **Bootstrap**, providing multiple static content pages and an AI-powered search interface.

## Tech Stack

- **Backend**: FastAPI
- **Templating**: Jinja2 (`Jinja2Templates`)
- **Frontend**: HTML5, Bootstrap 5, Custom CSS
- **JavaScript**: Vanilla JS for chat message handling

## Install
pip install -r requirements.txt

## Run
uvicorn app:app --host 0.0.0.0 --port 8000
or
run.bat

## Access from LAN
1. Find your local IP (ipconfig / ifconfig)
2. Open http://<your-ip>:8000 from another device on the same network
