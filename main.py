from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils import get_code, Description

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Welcome to DSMATICS!"

@app.post("/icd10")
def get_code(payload: Description):
    if len(payload.description) > 0:
        text = payload.description
        codes = get_code(text)
        return {'ICD-10_Code': codes}
    else:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Empty descriptions not acceptable...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)



