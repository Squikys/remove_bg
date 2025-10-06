import gc
import io
import logging
from fastapi import APIRouter, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse
from handler.remover import remover
remove_router=APIRouter(prefix="/api")


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

@remove_router.post("/remove")
async def remove(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Not an image")
    try:
        logger.info("Getting Image .........")
        img= await file.read()
        logger.info("Processing .........")
        removed_bg = remover(img)
        return StreamingResponse(
                io.BytesIO(removed_bg),
                media_type="image/png",
                headers={
                "Cache-Control": "no-cache",
                "Connection": "close"
            })
    finally:
        if img is not None:
            del img
        gc.collect()
    
@remove_router.get("/test")
def test():
    return {"test":"passed"}