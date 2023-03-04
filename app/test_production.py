from app.main import app, BASE_DIR, UPLOAD_DIR, get_settings

from fastapi.testclient import TestClient
from PIL import Image, ImageChops
import shutil
import httpx

import time
import io

client = TestClient(app)
settings = get_settings()
# doing this because the project is not deployed to AWS
settings.app_auth_token_prod = settings.app_auth_token
# endpoint will be different after deployemt
ENDPOINT = "http://127.0.0.1:8000/"

def test_get_home():
    response = httpx.get(ENDPOINT)
    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
    assert response.text != "<h1>Hello world!</h1>"


def test_invalid_file_upload_error():
    response = httpx.post(ENDPOINT)
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]


def test_prediction_upload():
    image_saved_path = BASE_DIR / "images"

    for path in image_saved_path.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None
        response = httpx.post(ENDPOINT, files={"file":open(path, 'rb')},
                               headers={"Authorization": f"Token {settings.app_auth_token_prod}"}
                               )
        if img is None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            data = response.json()
            assert len(data.keys()) == 2


def test_prediction_upload_missing_headers():
    img_saved_path = BASE_DIR / "images"
    for path in img_saved_path.glob("*"):
        response = httpx.post(ENDPOINT,
            files={"file": open(path, 'rb')}
        )
        assert response.status_code == 401


def test_echo_upload():
    image_saved_path = BASE_DIR / "images"
    for path in image_saved_path.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None
        response = httpx.post(ENDPOINT + "img-echo/", files={"file":open(path, 'rb')})
        if img is None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            r_stream = io.BytesIO(response.content)
            echo_img = Image.open(r_stream)
            flag = 1 if ImageChops.difference(echo_img, img).getbbox() == None else 0
            assert flag == 1

    # time.sleep(3)
    # shutil.rmtree(UPLOAD_DIR)