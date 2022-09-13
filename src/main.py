import fastapi as _fastapi
import fastapi.responses as _responses

app = _fastapi.FastAPI()

import services as _services


@app.get("/")
def route():
    return {"message": "Welcome to the amazing meme api"}


@app.get("/general-memes")
def get_general_memes():
    image_path = _services.select_random_image("memes")
    return _responses.FileResponse(image_path)


@app.post("/general-memes")
def create_general_memes(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("memes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="Incorrect file type")
    return _responses.FileResponse(file_path)


@app.get("/cat-memes")
def get_cat_memes():
    image_path = _services.select_random_image("Catmemes")
    return _responses.FileResponse(image_path)


@app.post("/cat-memes")
def create_cat_memes(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("Catmemes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="Incorrect file type")
    return _responses.FileResponse(file_path)


@app.get("/history-memes")
def get_history_memes():
    image_path = _services.select_random_image("HistoryMemes")
    return _responses.FileResponse(image_path)


@app.post("/history-memes")
def create_history_memes(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("HistoryMemes", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="Incorrect file type")
    return _responses.FileResponse(file_path)


@app.get("/polish-memes")
def get_polish_meme():
    image_path = _services.select_random_image("polishmeme")
    return _responses.FileResponse(image_path)


@app.post("/polish-memes")
def create_polish_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("polishmeme", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="Incorrect file type")
    return _responses.FileResponse(file_path)


@app.get("/programmer-memes")
def get_programmer_memes():
    image_path = _services.select_random_image("ProgrammerHumor")
    return _responses.FileResponse(image_path)


@app.post("/programmer-memes")
def create_programmer_memes(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_path = _services.upload_image("ProgrammerHumor", image)
    if file_path is None:
        return _fastapi.HTTPException(status_code=409, detail="Incorrect file type")
    return _responses.FileResponse(file_path)
