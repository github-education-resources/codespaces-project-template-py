from datetime import datetime
from os.path import dirname, abspath, join
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

app = FastAPI()
app.mount("/ui", StaticFiles(directory=static_path), name="ui")

class Body(BaseModel):
    strftime: str


@app.get('/')
def root():
    return FileResponse("static/index.html")


@app.post('/generate')
def generate(body: Body):
    """
    Generate the current time given a strftime template. For example:
    '%Y-%m-%dT%H:%M:%S.%f'
    """
    tmpl = body.strftime or '%Y-%m-%dT%H:%M:%S.%f'
    return {'date': datetime.now().strftime(tmpl)}
