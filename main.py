from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import contacts, utils

app = FastAPI(title="Contacts API")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contacts.router, prefix="/api")
app.include_router(utils.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)