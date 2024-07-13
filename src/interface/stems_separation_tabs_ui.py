import gradio as gr
import os
import shutil
from ..functions.demucs_fn import run_separation, zip_output_folder, provide_download_link

def get_audio_files(directory):
    return [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith((".mp3", ".wav"))]

def handle_separation_and_zip(state, separation_type, model):
    state.update({"type": separation_type, "model": model})
    state["pre_zip_path"] = f"./temp/{state['file_name'][:25]}_{model}_{state['id'][:5]}".replace(" ", "_")

    result, out_path = run_separation(state)
    if "Separation complete" in result:
        shutil.copytree(f"{state['output_path']}/{model}/{state['file_name']}", state["pre_zip_path"], dirs_exist_ok=True)
        shutil.rmtree(state['output_path'])
        zip_file = zip_output_folder(state["pre_zip_path"])
        download_file = provide_download_link(zip_file)
        if download_file:
            return '<div style="background-color: lightgreen; color: darkgreen; padding: 10px;">Stem separation completed!</div>', gr.File(visible=True, value=download_file)
        else:
            return result, gr.HTML("Error creating zip file.")
    return result, gr.HTML("")

def show_audio_elements(state):
    audio_files = get_audio_files(state["pre_zip_path"])
    updates = [gr.update(visible=True, value=audio_files[i], label=os.path.splitext(os.path.basename(audio_files[i]))[0]) for i in range(len(audio_files))]
    updates += [gr.update(visible=False)] * (4 - len(audio_files))  # Hide remaining players if less than 4 files
    return updates

def stems_separation_tabs_ui(state):
    with gr.Tabs() as source_tabs:
        with gr.TabItem("Demucs"):
            gr.Markdown("## Upload and Separate Audio")
            with gr.Row():
                type_dropdown = gr.Dropdown(["Vocal + Instrumental", "Vocals + Drums + Bass + Others"], label="Type")
                model_dropdown = gr.Dropdown(["htdemucs", "htdemucs_ft", "htdemucs_6s", "hdemucs_mmi", "mdx", "mdx_extra", "mdx_q", "mdx_extra_q", "SIG"], label="Model")

            separate_button = gr.Button("Separate Stems")
            separate_result = gr.Markdown()
            download_link_ZIP = gr.File(visible=False)

            separate_button.click(
                fn=handle_separation_and_zip,
                inputs=[state, type_dropdown, model_dropdown],
                outputs=[separate_result, download_link_ZIP]
            )

            audio_players = [gr.Audio(visible=False) for _ in range(4)]
            download_link_ZIP.change(
                fn=show_audio_elements,
                inputs=[state],
                outputs=audio_players
            )

            for audio_player in audio_players:
                gr.Column(audio_player)

