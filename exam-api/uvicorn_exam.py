import uvicorn

from src.main import app

if __name__ == "__main__":
    uvicorn.run(app="src.main:app", host="0.0.0.0", port=8001, reload=True)