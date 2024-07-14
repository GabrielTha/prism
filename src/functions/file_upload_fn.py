import gradio as gr
from .utils import copy_and_delete_file, generate_random_string, update_state
import os

def file_uploader(file, state):
    if file.name.endswith(('.mp3', '.wav')):


        filename_with_extension = os.path.basename(file.name)
        internal_file_name, _ = os.path.splitext(filename_with_extension)
        id = generate_random_string()
        state.update({
            "source": "upload", 
            "id":id, 
            "file_name": internal_file_name,
            "input_path": file.name,
            "output_path": f"./temp/{id}/"
        })

        upload_status = '<div style="background-color: lightgreen; color: darkgreen; padding: 10px;">File uploaded successfully!</div>'
        markdown_content = "### Uploaded File Source Selected"
        return markdown_content, state, gr.HTML(value=upload_status, visible=True), gr.update(visible=True, value=file.name), gr.update(interactive=True)
    else:
        upload_status = '<div style="background-color: lightcoral; color: darkred; padding: 10px;">Error: Only MP3 and WAV files are allowed.</div>'
        markdown_content = "### No Source Selected"
        return markdown_content, state, gr.HTML(upload_status), gr.update(visible=False), gr.update(interactive=True)
    

def file_clear(state):
    state.update({
        "source": "none", 
        "id":"none", 
        "file_name": "none",
        "input_path": "none",
        "output_path": "none"
    })

    markdown_content = "### No Source Selected"
    return markdown_content, state, gr.HTML(visible=False), gr.update(visible=False), gr.update(interactive=True)