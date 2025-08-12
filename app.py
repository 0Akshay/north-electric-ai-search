from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Page Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/faqs", response_class=HTMLResponse)
async def faqs(request: Request):
    return templates.TemplateResponse("faqs.html", {"request": request})

@app.get("/guides", response_class=HTMLResponse)
async def guides(request: Request):
    return templates.TemplateResponse("guides.html", {"request": request})

@app.get("/rates", response_class=HTMLResponse)
async def rates(request: Request):
    return templates.TemplateResponse("rates.html", {"request": request})

@app.get("/policies", response_class=HTMLResponse)
async def policies(request: Request):
    return templates.TemplateResponse("policies.html", {"request": request})

@app.get("/news", response_class=HTMLResponse)
async def news(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})

@app.get("/billing", response_class=HTMLResponse)
async def billing(request: Request):
    return templates.TemplateResponse("billing.html", {"request": request})

@app.get("/ai-search", response_class=HTMLResponse)
async def ai_search(request: Request):
    return templates.TemplateResponse("ai-search.html", {"request": request})

# API Routes
@app.get("/api/ping")
async def ping():
    return JSONResponse({"ok": True, "message": "pong from FastAPI on LAN"})

# Run app
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
