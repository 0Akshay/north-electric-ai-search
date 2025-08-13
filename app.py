from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routers import pages, search, messages  # import our router

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include router
app.include_router(pages.router)
app.include_router(search.router)
app.include_router(messages.router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)
