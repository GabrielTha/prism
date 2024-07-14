import gradio as gr
import yt_dlp
import os

def search_youtube(query):
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch5',
        'skip_download': True,
        'format': 'bestaudio/best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(query, download=False)
        videos = info_dict['entries']
        titles = [video['title'] for video in videos]
        video_urls = [video['webpage_url'] for video in videos]
    return titles, video_urls


def download_mp3(video_url, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    return os.path.join(output_path, os.path.basename(video_url) + '.mp3')

def update_video_list(titles, video_urls):
    return gr.update(choices=titles, value=None), video_urls

def download_selected_video(video_title, video_titles, video_urls):
    try:
        video_index = video_titles.index(video_title)
        video_url = video_urls[video_index]
        mp3_file = download_mp3(video_url, "./temp")
        return f"Downloaded MP3: {mp3_file}"
    except ValueError as e:
        return f"Error: {str(e)}"