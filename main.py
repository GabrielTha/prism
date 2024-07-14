import gradio as gr
import os

from src.interface.source_selector_tabs_ui import source_selector_tabs_ui
from src.interface.stems_separation_tabs_ui import stems_separation_tabs_ui

from src.functions.utils import update_state

def get_folder_size_and_zip_count(path):
    total_size = 0
    zip_count = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
            if filename.endswith('.zip'):
                zip_count += 1

    total_size_gb = round(total_size / (1024 ** 3), 3)  
    return f"{total_size_gb} GB", f"{zip_count}"

# Create a Gradio block
with gr.Blocks() as app:

    state = gr.State({
        "id": "none",
        "source": "none", 
        "file_name": "none", 
        "input_path": "none", 
        "output_path": "none"
    }) 
    
    # Debug Section
    with gr.Accordion("DEBUG", open=False):
        temp_size = gr.Textbox(value=get_folder_size_and_zip_count("./temp")[0], interactive=False, label="Size of Temporary Files")
        zip_count = gr.Textbox(value=get_folder_size_and_zip_count("./temp")[1], interactive=False, label="Number of Extractions Realized")
        output = gr.JSON(label="State Verbose")
        state.change(fn=lambda x: x, inputs=state, outputs=output)

    # Header Row
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("# Source Selector")
        with gr.Column(scale=8, visible=False):
            gr.Markdown("# -")
        with gr.Column(scale=0.3):
            custom_html = gr.HTML("""
            <div style="display: flex; justify-content: flex-end;">
            <button id="custom_btn" class="lg secondary svelte-cmf5ev" onclick="location.reload();">
                New Extraction
            </button>
            </div>
            """)

    markdown_active_source = gr.Markdown("### No Source Selected")
    
    # Source Selector Tabs
    source_selector_tabs_ui(state, markdown_active_source)
    
    gr.Markdown("---")
    gr.Markdown("# Stem Extraction")

    # Stem Separation Tabs
    stems_separation_tabs_ui(state)

# Launch the interface
app.launch()
