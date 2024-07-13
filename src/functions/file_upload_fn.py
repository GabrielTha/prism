import gradio as gr
from .utils import copy_and_delete_file, generate_random_string
import os

def file_uploader(file, state):
    if file.name.endswith(('.mp3', '.wav')):
        state["source"] = "upload"

        filename_with_extension = os.path.basename(file.name)
        state["file_name"], _ = os.path.splitext(filename_with_extension)
        state["id"] = generate_random_string()
        state["input_path"] = file.name
        state["output_path"] = f"./temp/{state['id']}/"
        upload_status = '<div style="background-color: lightgreen; color: darkgreen; padding: 10px;">File uploaded successfully!</div>'
        markdown_content = "### Uploaded File Source Selected"
        return markdown_content, state, gr.HTML(upload_status), gr.update(visible=True, value=file.name)
    else:
        upload_status = '<div style="background-color: lightcoral; color: darkred; padding: 10px;">Error: Only MP3 and WAV files are allowed.</div>'
        markdown_content = "### No Source Selected"
        return markdown_content, state, gr.HTML(upload_status), gr.update(visible=False)