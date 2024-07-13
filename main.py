import gradio as gr

from src.interface.source_selector_tabs_ui import source_selector_tabs_ui
from src.interface.stems_separation_tabs_ui import stems_separation_tabs_ui

def refresh_page():
    # This function doesn't need to do anything
    pass

# Create a Gradio block
with gr.Blocks() as app:
    state = gr.State({"source": "none", "file_name":"none", "input_path": "none", "output_path": "none"})  # Initialize the global state with default value
    
    js_reload = """
        location.reload();
    """

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("# Source Selector")
        with gr.Column(scale=8, visible=False):
            gr.Markdown("# -")
        with gr.Column(scale=0.3):
            # new_extraction_btn = gr.Button(value="New Extraction", icon="https://cdn-icons-png.flaticon.com/512/10695/10695869.png", elem_id="greet_button")
            custom_html = gr.HTML("""
            <div style="display: flex; justify-content: flex-end;">
            <button id="custom_btn" class="lg secondary svelte-cmf5ev" onclick="location.reload();">
                New Extraction
            </button>
            </div>
            """)

    # custom_html = gr.HTML("""
    # <button id="custom_btn" onclick="location.reload();">Click me to refresh the page</button>
    # """)
    
    markdown_active_source = gr.Markdown("### No Source Selected")

    active_tab = gr.State(value="Greet")
    # Create tabs
    source_selector_tabs_ui(state,markdown_active_source)
    
    gr.Markdown("---")
    gr.Markdown("# Stem Extraction")

    stems_separation_tabs_ui(state)

# Launch the interface
app.launch()
