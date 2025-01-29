from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from datetime import datetime

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origin
    allow_credentials=True,
    allow_methods=["GET"],
)

@app.get("/")
async def root():
    return RedirectResponse(url="/info")

@app.get("/info")
async def get_info():
    current_datetime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "email": "dubemnwabuisi@gmail.com",
        "current_datetime": current_datetime,
        "github_url": "https://github.com/Celnet-hub/hng12-pub-api"
    }