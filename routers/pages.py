from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Page Routes
@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/faqs", response_class=HTMLResponse)
async def faqs(request: Request):
    return templates.TemplateResponse("faqs.html", {"request": request})

@router.get("/guides", response_class=HTMLResponse)
async def guides(request: Request):
    return templates.TemplateResponse("guides.html", {"request": request})

@router.get("/rates", response_class=HTMLResponse)
async def rates(request: Request):
    return templates.TemplateResponse("rates.html", {"request": request})

@router.get("/policies", response_class=HTMLResponse)
async def policies(request: Request):
    return templates.TemplateResponse("policies.html", {"request": request})

@router.get("/news", response_class=HTMLResponse)
async def news(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})

@router.get("/billing", response_class=HTMLResponse)
async def billing(request: Request):
    return templates.TemplateResponse("billing.html", {"request": request})

@router.get("/ai-chatbot", response_class=HTMLResponse)
async def ai_chatbot(request: Request):
    return templates.TemplateResponse("ai-chatbot.html", {"request": request})

# API Routes
@router.get("/api/ping")
async def ping():
    return JSONResponse({"ok": True, "message": "pong from FastAPI on LAN"})
