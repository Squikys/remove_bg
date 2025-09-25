from fastapi import FastAPI
from router.remove_router import remove_router
app=FastAPI()

@app.get("/")
def ping():
    return{"pong"}
app.include_router(router=remove_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000, log_level="info",
                workers=1, timeout_keep_alive=5) 