from fastapi import APIRouter,Request, File
from handler.remover import remover
remove_router=APIRouter(prefix="/api")

@remove_router.post("/remove")
def remove(req:Request,image:File):
    remover(img=image)
    pass

@remove_router.get("/test")
def test():
    return {"test":"passed"}