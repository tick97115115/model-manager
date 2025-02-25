from fastapi import FastAPI
from model_manager.settings import Settings, check_settings, load_settings
import gradio as gr
from model_manager.gradio_ui import demo
import uvicorn
from .settings import init

app = FastAPI()
app = gr.mount_gradio_app(app, demo, '/gradio')

@app.get('/test')
async def test():
    return {'message': 'hello, world'}


if __name__ == "__main__":
    init()
    uvicorn.run("main:app")
    