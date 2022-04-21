import os

from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
async def main():
    file_name = "project5_fileDownload.py"
    # DEPENDS ON WHERE YOUR FILE LOCATES
    file_path = os.getcwd() + "/" + file_name
    return FileResponse(
        path=file_path, media_type="application/octet-stream", filename=file_name
    )


# pip install aiofiles
