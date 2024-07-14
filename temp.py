import gradio as gr
from pytube import YouTube

def get_video_info(url):
    yt = YouTube(url)
    title = yt.title
    duration = yt.length  # duration in seconds
    thumbnail_url = yt.thumbnail_url

    # Convert duration from seconds to HH:MM:SS format
    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    return thumbnail_url, title, duration_str

# Define Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("Enter a YouTube URL to get the thumbnail, title, and duration of the video.")
    
    url_input = gr.Textbox(label="YouTube URL")
    thumbnail_output = gr.Image(label="Thumbnail", height=92, width=108)
    title_output = gr.Textbox(label="Title")
    duration_output = gr.Textbox(label="Duration")
    
    get_info_button = gr.Button("Get Video Info")
    
    get_info_button.click(fn=get_video_info, inputs=url_input, outputs=[thumbnail_output, title_output, duration_output])

demo.launch()
