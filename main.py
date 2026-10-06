from fastapi import FastAPI

app=FastAPI(
    title="pincode lookup API",
    description="Auto fill city and state form India pincode during checkout"
)

@app.get("/")
def root():
    return{"message":"pincode lookup API"}