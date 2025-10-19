from rembg import remove
from PIL import Image
import io
import gc

def remover(image:bytes)->io.BytesIO:
    img = None
    output = None
    buffer = None
    
    try:
        img = Image.open(io.BytesIO(image))
        output = remove(img)
        buffer = io.BytesIO()
        output.save(buffer, format="PNG")
        buffer.seek(0)
        result = buffer.getvalue()
        return result
        
    finally:
        if img is not None:
            img.close()
            del img
        if output is not None:
            output.close()
            del output
        if buffer is not None:
            buffer.close()
            del buffer
        gc.collect()
