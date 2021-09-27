import os
import tkinter as tk
from tkinter.constants import END, NORMAL
from pytube import YouTube
import concurrent.futures
import time

program_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(program_path)
download_dir = 'Downloaded files'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)
os.chdir(download_dir)

def convertTextToList():
    all_urls = textBox.get('1.0',END).strip().split('\n')
    if(all_urls[0]) == '': # checks if textBox is empty (not perfect since first line can be skipped) maybe fix this
        label_status.config(text='PASTE URL\'S', bg='#ff9999')
        return
    download_button.config(state=NORMAL)
    return all_urls

def download(url):
    try:
        video = YouTube(url)
        video = video.streams.get_by_itag(251)
        outfile = video.download()

        base, ext = os.path.splitext(outfile)
        new_file = base + '.mp3'
        if not(os.path.exists(new_file)):
            os.rename(outfile, new_file)
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')
    
# ay multithreading!
def executor():
    try:
        t1 = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(download, convertTextToList()) 
        t2 = time.perf_counter()
        print(f'Finished in {t2-t1} seconds')
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')

window = tk.Tk()
window.title("Youtube to mp3")
window.geometry('450x300')
window.iconbitmap('..\Images\icon.ico')

# instruction label
instruction_label = tk.Label(window, text='Paste URL\'s below: (separate with newlines or spaces)',font=('century gothic',10))
instruction_label.grid(row=0,column=0,columnspan=3)

# textbox for pasting url's
textBox = tk.Text(window)
textBox.grid(row=1,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# status / instruction / error label
label_status = tk.Label(window, font=('century gothic',10))
label_status.grid(row=2,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# download button
download_button = tk.Button(text='Download', font=('century gothic',15), command=executor)
download_button.grid(row=3,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# scaling with window
window.columnconfigure(1, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(1, weight=1)

window.mainloop()
