import os
from fastapi import FastAPI
from router.remove_router import remove_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()
port = int(os.environ.get("PORT", 8080))
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=remove_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info",
                workers=1, timeout_keep_alive=5) 
