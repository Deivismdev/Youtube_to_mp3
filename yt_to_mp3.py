import os
import tkinter as tk
from tkinter.constants import END
from pytube import YouTube
import threading
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import re

program_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(program_path)
download_dir = 'Downloaded files'

# creates directory for downloeded files
if not os.path.exists(download_dir):
    os.makedirs(download_dir)
os.chdir(download_dir)

# Puts input from textbox to a list
def convertInputToList():
    all_urls = textBox.get('1.0',END).strip().split('\n')
    if not all_urls[0]:
        label_status.config(text='PASTE URL\'S', bg='#ff9999')
        return []
    else:
        valid_urls = [url for url in all_urls if is_youtube_url(url)]
        invalid_urls = [url for url in all_urls if not is_youtube_url(url)]
        
        if invalid_urls:
            messagebox.showwarning("Invalid URLs", f"Some URLs are invalid and will be ignored:\n{invalid_urls}")
        
        return valid_urls

def is_youtube_url(url):
    return re.match(r'(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', url) is not None

# Downloads the video, changes extension to .mp3
def download(url):
    try:
        label_status.config(text='DOWNLOADING...', bg='#FFFF00')
        progress_bar.start()
        video = YouTube(url)
        video = video.streams.get_by_itag(251)
        outfile = video.download()
        base, _ = os.path.splitext(outfile)
        new_file = base + '.mp3'
        if not(os.path.exists(new_file)):
            os.rename(outfile, new_file)
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')

    label_status.config(text='DOWNLOAD COMPLETE', bg='#4bc449')
    progress_bar.stop()

# Creates thread for each url
def createThreads(urls):
    try:
        for url in urls:
            downloadThread=threading.Thread(target=lambda:download(url))
            downloadThread.start()
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')

def chooseDirectory():
    global download_dir
    directory = filedialog.askdirectory()
    if(directory!=''):
        download_dir = directory
        instruction_label.config(text=f'Directory: {download_dir}')
        os.chdir(download_dir)

print(download_dir)
window = tk.Tk()
window.title("Youtube to mp3")
window.geometry('600x300')
window.minsize(590,300)
window.iconbitmap('..\Images\icon.ico')

#Choose directory button
directory_button = tk.Button(text='Choose',font=('century gothic',9), command=chooseDirectory)
directory_button.grid(row=0,column=2, sticky=(tk.E))

# Instruction label
instruction_label = tk.Label(window, text=f'Directory: {download_dir} (in working directory)',font=('century gothic',10))
instruction_label.grid(row=0,column=1,columnspan=2)

# Textbox for pasting url's
textBox = tk.Text(window)
textBox.grid(row=1,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Status / instruction / error label
label_status = tk.Label(window, font=('century gothic',10))
label_status.grid(row=2,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Download button
download_button = tk.Button(text='Download', font=('century gothic',15), command=lambda:createThreads(convertInputToList())) 
download_button.grid(row=3,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# Progress bar
s = ttk.Style()
s.theme_use('clam')
progress_bar = ttk.Progressbar(window,mode='indeterminate')        
progress_bar.grid(row=4, column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)    

# Scaling with window
window.columnconfigure(1, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(1, weight=1)

window.mainloop()
print(download_dir)
