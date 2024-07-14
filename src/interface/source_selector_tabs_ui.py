import gradio as gr

from .file_upload_ui import file_upload_ui
from .youtube_ui import youtube_ui

def source_selector_tabs_ui(state, markdown_active_source):
    with gr.Tabs() as source_tabs:
            with gr.TabItem("File"):
                file_upload_ui(state, markdown_active_source)

            with gr.TabItem("Batch/Folder", visible=False):
                gr.Markdown("## To Be Done")

            with gr.TabItem("Youtube"):
                youtube_ui(state)
            
            with gr.TabItem("Soulseek", visible=False):
                gr.Markdown("## To Be Done")