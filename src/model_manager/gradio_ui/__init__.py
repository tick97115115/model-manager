import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Local"):
        with gr.Row():
            search_text = gr.Textbox(label="Search Bar")
    with gr.Tab("CivitAI"):
        gr.Text("Tiger")
    greetings = gr.Text("Hello!")

