import gradio as gr

def youtube_ui():
    gr.Markdown("## Youtube High Quality Downloader")
    # search_query = gr.Textbox(label="Search Query")
    # search_button = gr.Button("Search")
    # video_titles_dropdown = gr.Dropdown(choices=[], label="Select Video")
    # output_path = gr.Textbox(label="Output Folder Path")
    # download_button = gr.Button("Download MP3")
    # result = gr.Textbox(label="Result")
    # video_titles_state = gr.State([])
    # video_urls_state = gr.State([])

    # def search_and_update(query):
    #     titles, urls = search_youtube(query)
    #     return update_video_list(titles, urls) + (titles,)

    # search_button.click(
    #     search_and_update,
    #     inputs=[search_query],
    #     outputs=[video_titles_dropdown, video_urls_state, video_titles_state]
    # )

    # download_button.click(
    #     download_selected_video,
    #     inputs=[video_titles_dropdown, video_titles_state, video_urls_state, output_path],
    #     outputs=result
    # )