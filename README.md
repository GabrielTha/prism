

<div style="text-align: center;">
    <img src="https://i.ibb.co/mBPbgQx/prism-logo.png" alt="drawing" width="200"/>
</div>


# Prism App

This project is a [Gradio](https://github.com/gradio-app/gradio) and [Demucs](https://github.com/facebookresearch/demucs)-based web application for extracting stems (vocals, drums, bass, etc.) from audio files. It uses the Demucs model for stem separation and integrates YouTube-DL for downloading audio directly from YouTube. The application allows users to upload audio files or provide YouTube links for processing.

# Installation

To run this project, you need to have Python 3 installed. Install the required dependencies using pip:

```bash
pip3 install -r requirements.txt
```

# Running the Application

To start the Gradio application, navigate to the project directory and run the following command:
```bash
python3 main.py
```

This will start a local web server and provide you with a URL to access the application in your web browser.

# File Structure
main.py: The main entry point for the Gradio application.
clear_temp.py: A script to clear temporary files.
temp.py: Temporary file handling.
src/: Contains the core functionalities and interface elements.
functions/: Directory with the functions for Demucs, file upload, and YouTube download.
interface/: Directory with the UI components for Gradio.

# Contributing
If you want to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue on the GitHub repository.
