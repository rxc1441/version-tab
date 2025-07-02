# Requires google-genai via pip install google-genai
import os
import io
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

# --- IMPORTANT CHANGE FOR NEW SDK ---
# from google.generativeai import GenerativeModel # OLD
from google import genai # NEW SDK import

# Load environment variables from .env file
load_dotenv()

# Get your Gemini API key from environment variables
# The new SDK primarily looks for GOOGLE_API_KEY, but checking for GEMINI_API_KEY is good if that's what you used previously.
# You can also pass it explicitly to the Client constructor.
# It's highly recommended to use GOOGLE_API_KEY for consistency with the new SDK.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY (or GEMINI_API_KEY) not found in environment variables. Please set it in a .env file or directly.")

# --- Initialize the GenAI Client (NEW SDK way) ---
# The API key can be explicitly passed or picked up from GOOGLE_API_KEY env var
client = genai.Client(api_key=GOOGLE_API_KEY)

# Initialize FastAPI app
app = FastAPI()

# ... (CORS Configuration - remains the same) ...

# ... (Serve Static Files - remains the same) ...

# --- Gemini API Endpoints ---

@app.post("/generate_text/")
async def generate_text(prompt: dict):
    """Endpoint for text-only interactions with Gemini."""
    if not "text" in prompt or not prompt["text"]:
        raise HTTPException(status_code=400, detail="Text prompt is required.")
    
    try:
        # Access model via client.models (NEW SDK way)
        model = client.models.get("gemini-pro") # Use get() method
        response = model.generate_content(prompt["text"])
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_multimodal/")
async def generate_multimodal(
    prompt: str = Form(...),
    image: UploadFile = File(...)
):
    """Endpoint for multimodal interactions (text + image) with Gemini."""
    try:
        # Read the image bytes
        image_data = await image.read()
        pil_image = Image.open(io.BytesIO(image_data))

        # Use the multimodal model via client.models (NEW SDK way)
        model = client.models.get("gemini-pro-vision") # Use get() method
        contents = [prompt, pil_image]
        response = model.generate_content(contents)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health/")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "Gemini GUI backend is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

