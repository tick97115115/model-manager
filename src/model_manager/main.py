from fastapi import FastAPI
from model_manager.config import Settings, check_settings, load_settings
import gradio as gr
from model_manager.gradio_ui import demo
import uvicorn
from .config import init

app = FastAPI()
app = gr.mount_gradio_app(app, demo, '/gradio')

def init():
    pass

@app.get('/test')
async def test():
    return {'message': 'hello, world'}


if __name__ == "__main__":
    init()
    uvicorn.run("main:app")
    