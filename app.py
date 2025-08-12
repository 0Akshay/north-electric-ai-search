from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import uvicorn
import datetime
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount the static directory to serve HTML, CSS, and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates folder
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/ping")
async def ping():
    return JSONResponse({"ok": True, "message": "pong from FastAPI on LAN"})

# Optional: run if executed directly
if __name__ == "__main__":
    # Default port 8000 — bind to 0.0.0.0 so other devices on LAN can access
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
