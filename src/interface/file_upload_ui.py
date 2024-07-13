import gradio as gr
from ..functions.file_upload_fn import file_uploader

def file_upload_ui(state, markdown_active_source):
    gr.Markdown("## Upload Your File")
    file_input = gr.File(label="Upload your file", file_types=['.mp3', '.wav'])
    upload_status = gr.HTML()
    audio_player = gr.Audio(visible=False)

    file_input.change(
        fn=file_uploader,
        inputs=[file_input, state],
        outputs=[markdown_active_source, state, upload_status, audio_player]
    )