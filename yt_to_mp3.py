import os
import tkinter as tk
from tkinter.constants import END
from pytube import YouTube
import threading
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import re

#TODO: add button to select quality
# also could rewrite all this to use oop... but eehh..

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
default_download_dir = os.path.join(desktop_path, 'downloaded_from_yt')

if not os.path.exists(default_download_dir):
    os.makedirs(default_download_dir)

destination = default_download_dir

# Puts input from textbox to a list
def convert_input_to_list():
    all_urls = textBox.get('1.0',END).strip().split('\n')
    if not all_urls[0]:
        label_status.config(text='PASTE URL\'S', bg='#ff9999')
        return []
    else:
        # TODO: this looks stupid
        valid_urls = [url for url in all_urls if is_youtube_url(url)]
        invalid_urls = [url for url in all_urls if not is_youtube_url(url)]

        # TODO: i don't like this, maybe color ignored links red in the textbox?
        if invalid_urls:
            messagebox.showwarning("Invalid URLs", f"Some URLs are invalid and will be ignored:\n{invalid_urls}")
        
        return valid_urls

def is_youtube_url(url):
    return re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', url) is not None

# Downloads the video
def download(url):
    try:
        label_status.config(text='DOWNLOADING...', bg='#FFFF00')
        progress_bar.start()
        video = YouTube(url)
        if download_type.get() == "audio":
            stream = video.streams.filter(only_audio=True).first()
        elif download_type.get() == "video":
            stream = video.streams.filter(progressive=True).order_by('resolution').desc().first()
        else:  # audio+video
            stream = video.streams.filter(progressive=True).order_by('resolution').desc().first()

        if not os.path.exists(destination):
            os.makedirs(destination)
        
        outfile = stream.download(output_path=destination)
        
        if download_type.get() == "audio":
            base, _ = os.path.splitext(outfile)
            new_file = base + '.mp3'
            if not os.path.exists(new_file):
                os.rename(outfile, new_file)

    except Exception as e:
        label_status.config(text="PASTE URL'S FROM YOUTUBE", bg='#ff9999')
        print(e)

    label_status.config(text='DOWNLOAD COMPLETE', bg='#4bc449')
    progress_bar.stop()

# Creates thread for each url
# TODO: this feels wrong...
def create_threads(urls):
    try:
        for url in urls:
            downloadThread=threading.Thread(target=lambda:download(url))
            downloadThread.start()
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')

def choose_destination():
    global destination
    selected_destination = filedialog.askdirectory()
    if selected_destination:
        destination = selected_destination
        destination_label.config(text=f'Directory: {destination}')
    else:
        destination = default_download_dir
        destination_label.config(text=f'Directory: {default_download_dir}')


window = tk.Tk()
window.title("Youtube to mp3")
window.geometry('600x300')
window.minsize(590,300)
window.iconbitmap('Images\icon.ico')

download_type = tk.StringVar(value="audio+video")

# Instruction label
instruction_label = tk.Label(window, text=f'Paste URLs below, seperated by new lines or spaces',font=('century gothic',10))
instruction_label.grid(row=0,column=0, sticky=tk.N,columnspan=3)

# Textbox for pasting url's
textBox = tk.Text(window)
textBox.grid(row=1,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Status / instruction / error label
label_status = tk.Label(window, font=('century gothic',10))
label_status.grid(row=2,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Download type buttons
audio_button = tk.Radiobutton(window, text="Audio", variable=download_type, value="audio", font=('century gothic', 10))
audio_button.grid(row=3, column=0, sticky=tk.N, columnspan=1)

audio_video_button = tk.Radiobutton(window, text="Audio + Video", variable=download_type, value="audio+video", font=('century gothic', 10))
audio_video_button.grid(row=3, column=1, sticky=tk.N, columnspan=1)

video_button = tk.Radiobutton(window, text="Video", variable=download_type, value="video", font=('century gothic', 10))
video_button.grid(row=3, column=2, sticky=tk.N, columnspan=1)

# Destination label
destination_label =  tk.Label(window, text=f'Files will be saved: {destination}',font=('century gothic',10))
destination_label.grid(row=4,column=0, sticky=tk.N,columnspan=3)

#change destination
change_destination_button = tk.Button(text='Change destination',font=('century gothic',9), command=choose_destination)
change_destination_button.grid(row=5,column=0, sticky=(tk.N, tk.S, tk.E, tk.W), columnspan=4)

# Download button
# TODO: button should call download(), convert_input_to_list() and thread stuff should be called from download()
# also check if lambda is necessary here...
download_button = tk.Button(text='Download', font=('century gothic',15), command=lambda:create_threads(convert_input_to_list())) 
download_button.grid(row=6,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Progress bar
s = ttk.Style()
s.theme_use('clam')
progress_bar = ttk.Progressbar(window,mode='indeterminate')        
progress_bar.grid(row=7, column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)    

# Scaling with window
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(1, weight=1)

window.mainloop()
