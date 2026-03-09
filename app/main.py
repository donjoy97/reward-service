from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse #return data in JSON format
from app.api.reward import router # imports  router 

app = FastAPI(title="Reward Decision Service") # heading to swagger

app.include_router(router)  # registering the end point


# error handling
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error", "details": str(exc)}
    )