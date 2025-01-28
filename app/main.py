from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],
    # # allow_headers=["*"],  # Allows all headers
)

@app.get("/info")
async def read_root():
    return {
        "email": "dubemnwabuisi@gmail.com",
        "timestamp": datetime.now().isoformat(),
        "github_url": "https://github.com/yourusername/your-repo"
    }