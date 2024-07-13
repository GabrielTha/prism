import gradio as gr

from src.interface.source_selector_tabs_ui import source_selector_tabs_ui
from src.interface.stems_separation_tabs_ui import stems_separation_tabs_ui

# Create a Gradio block
with gr.Blocks() as app:
    state = gr.State({"source": "none", "file_name":"none", "input_path": "none", "output_path": "none"})  # Initialize the global state with default value
    gr.Markdown("# Source Selector")
    markdown_active_source = gr.Markdown("### No Source Selected")

    active_tab = gr.State(value="Greet")
    # Create tabs
    source_selector_tabs_ui(state,markdown_active_source)
    
    gr.Markdown("---")
    gr.Markdown("# Stem Extraction")

    stems_separation_tabs_ui(state)

# Launch the interface
app.launch()
