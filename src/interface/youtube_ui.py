import gradio as gr
import yt_dlp
import os
from ..functions.youtube_fn import search_youtube, update_video_list, download_selected_video
from ..functions.utils import copy_and_delete_file, generate_random_string, update_state
from pytube import YouTube

def get_video_info(url):
    yt = YouTube(url)
    title = yt.title
    duration = yt.length 
    thumbnail_url = yt.thumbnail_url

    hours, remainder = divmod(duration, 3600)
    minutes, seconds = divmod(remainder, 60)
    duration_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    return thumbnail_url, title, duration_str, gr.update(visible=True)

def download_mp3(state, video_url, upload_status):

    id = generate_random_string()
    download_path = f"./temp/{id}"

    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    final_file_name = None

    def hook(d):
        nonlocal final_file_name
        if d['status'] == 'finished':
            final_file_name = d['filename'].replace('.webm', '.mp3') if d['filename'].endswith('.webm') else d['filename']

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'progress_hooks': [hook],
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    file_name_with_extension = os.path.basename(final_file_name)
    file_name, _ = os.path.splitext(file_name_with_extension)

    state.update({
        "source": "youtube", 
        "id":id, 
        "file_name": file_name,
        "input_path": final_file_name,
        "output_path": f"./temp/{id}/"
    })


    upload_status = '<div style="background-color: lightgreen; color: darkgreen; padding: 10px;">File loaded successfully!</div>'

    return state, upload_status

def youtube_ui(state):

    gr.Markdown("## Youtube Downloader")
    url_input = gr.Textbox(label="YouTube URL")
    with gr.Row(visible=False) as video_info:
        with gr.Column(scale=1):
            thumbnail_output = gr.Image(label="Thumbnail", height=192, width=308, interactive=False)
        with gr.Column(scale=4):
            title_output = gr.Textbox("Title", interactive=False)
            duration_output = gr.Textbox("Duration", interactive=False)

    upload_status = gr.HTML()
    search_button = gr.Button("Load")

    search_button.click(fn=get_video_info, inputs=url_input, outputs=[thumbnail_output, title_output, duration_output, video_info])
    search_button.click(fn=download_mp3, inputs=[state, url_input, upload_status], outputs=[state, upload_status])
