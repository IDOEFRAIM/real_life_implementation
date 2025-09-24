import gradio as gr
def greet(name):
    return 'hello' + name


demo = gr.Interface(fn=greet,
inputs=["text","checkbox;gr.Slider(0,100)"],
output="text")

demo.lauch()