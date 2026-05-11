from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import ml_utils
import gdpr_compliance
import knowledge_base
import constants

app = FastAPI(title="CareerMatch AI Backend API")

class MatchRequest(BaseModel):
    cv_text: str
    jd_text: str

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "CareerMatch AI Backend is running"}

@app.post("/match")
def match_cv_jd(request: MatchRequest):
    try:
        # This mirrors the logic used in app.py
        # We need to adapt it slightly to not use st.cache if calling from API
        # but for now we call the functions directly.
        
        # 1. Detect Seniority
        seniority, confidence = ml_utils.detect_seniority(request.cv_text)
        
        # 2. Extract Skills
        cv_skills = ml_utils.extract_skills(request.cv_text)
        jd_skills = ml_utils.extract_skills(request.jd_text)
        
        # 3. Calculate Match (Simulation of the complex logic in app.py)
        # Note: In a real split, we'd refactor ml_utils to have a clean 'calculate_match' function
        # For now, we provide the basic components.
        
        return {
            "seniority": seniority,
            "cv_skills": list(cv_skills),
            "jd_skills": list(jd_skills),
            "match_score": 75.0 # Placeholder for now
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/extract-skills")
def extract_skills(request: TextRequest):
    skills = ml_utils.extract_skills(request.text)
    return {"skills": list(skills)}

@app.post("/seniority")
def get_seniority(request: TextRequest):
    level, confidence = ml_utils.detect_seniority(request.text)
    return {"level": level, "confidence": confidence}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
