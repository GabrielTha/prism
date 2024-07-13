
import os
import demucs.separate
import io
from pathlib import Path
import select
from shutil import rmtree, make_archive
import subprocess as sp
import sys
from typing import Dict, Tuple, Optional, IO


# Customize the following options!
model = "mdx"
extensions = ["mp3", "wav", "ogg", "flac"]  # we will look for all those file types.
#two_stems = None   # only separate one stems from the rest, for instance
two_stems = "vocals"

# Options for the output audio.
mp3 = True
mp3_rate = 320

    
def find_files(in_path):
    out = []
    for file in Path(in_path).iterdir():
        if file.suffix.lower().lstrip(".") in extensions:
            out.append(file)
    return out


def copy_process_streams(process: sp.Popen):
    def raw(stream: Optional[IO[bytes]]) -> IO[bytes]:
        assert stream is not None
        if isinstance(stream, io.BufferedIOBase):
            stream = stream.raw
        return stream

    p_stdout, p_stderr = raw(process.stdout), raw(process.stderr)
    stream_by_fd: Dict[int, Tuple[IO[bytes], io.StringIO, IO[str]]] = {
        p_stdout.fileno(): (p_stdout, sys.stdout),
        p_stderr.fileno(): (p_stderr, sys.stderr),
    }
    fds = list(stream_by_fd.keys())

    while fds:
        # `select` syscall will wait until one of the file descriptors has content.
        ready, _, _ = select.select(fds, [], [])
        for fd in ready:
            p_stream, std = stream_by_fd[fd]
            raw_buf = p_stream.read(2 ** 16)
            if not raw_buf:
                fds.remove(fd)
                continue
            buf = raw_buf.decode()
            std.write(buf)
            std.flush()

def separate(state):
    inp = state["input_path"]
    outp = state["output_path"]

    model = state["model"]

    if(state["type"] == "Vocal + Instrumental"):
        two_stems = "vocals"
    else:
        two_stems = None

    cmd = ["python3", "-m", "demucs.separate", "-o", str(outp), "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    if two_stems is not None:
        cmd += [f"--two-stems={two_stems}"]
    if os.path.isdir(inp):
        files = [str(f) for f in find_files(inp)]
    else:
        files = [inp]
    if not files:
        print(f"No valid audio files in {inp}")
        return
    print("Going to separate the files:")
    print('\n'.join(files))
    print("With command: ", " ".join(cmd))
    p = sp.Popen(cmd + files, stdout=sp.PIPE, stderr=sp.PIPE)
    copy_process_streams(p)
    p.wait()
    if p.returncode != 0:
        print("Command failed, something went wrong.")
        
def run_separation(state):
    if state["source"] == "upload" and state["input_path"] != "none":
        separate(state)
        return "Separation complete!", state["output_path"]
    else:
        return "No file uploaded or file path invalid."

def zip_output_folder(out_path):
    zip_file = make_archive(out_path, 'zip', out_path)
    return zip_file

def provide_download_link(zip_file):
    if os.path.exists(zip_file):
        return zip_file
    else:
        return None