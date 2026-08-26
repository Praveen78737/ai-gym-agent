from fastapi import FastAPI

app = FastAPI(title="AI Gym Assistant")


@app.get("/")
def home():
    return {
        "message": "AI Gym Assistant is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }