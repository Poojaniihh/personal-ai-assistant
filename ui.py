import gradio as gr

from app import execute_graph


def chat(query):
    return execute_graph(query)


ui = gr.Interface(
    fn=chat,
    inputs=[gr.Textbox(lines=2, placeholder="Anything  you  curious  about  today?...")],
    outputs=gr.Textbox(lines=10),
    title="Personal AI Assistant 🤖",
    description="Hey there ;) Your Personal Assistant is here Ask me anything",
)

ui.launch()




