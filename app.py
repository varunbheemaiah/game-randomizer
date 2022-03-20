from app import app
import uvicorn

print("RUNNING")
uvicorn.run(app, host="0.0.0.0", port=8000)
	