import os
import tkinter as tk
from tkinter.constants import END, NORMAL
from pytube import YouTube


# Future plans for this program:
# Ability to choose where files will be saved
# Ability to choose between downloading mp3's and mp4's (or both?)
# Downloading files in parallel

# Progress bar
# Nicer scalling
# Nicer UI / UI customization


def convertTextToList():
    all_urls = textBox.get('1.0',END).strip().split('\n')
    if(all_urls[0]) == '': # checks if textBox is empty (not perfect since first line can be skipped) maybe fix this
        label_status.config(text='PASTE URL\'S', bg='#ff9999')
        return
    download_button.config(state=NORMAL)
    return all_urls


def download(all_urls):
    try:
        for url in all_urls:
            video = YouTube(url)
            video = video.streams.get_by_itag(251)
            print(url + " " + str(video.filesize))
            outfile = video.download()

            base, ext = os.path.splitext(outfile)
            new_file = base + '.mp3'
            if not(os.path.exists(new_file)):
                os.rename(outfile, new_file)
                
        label_status.config(text='DOWNLOAD COMPLETE!', bg='#4bc449')
    except Exception:
        label_status.config(text='PASTE URL\'S FROM YOUTUBE', bg='#ff9999')
        # maybe parse text to check what url is pasted (parse_url() from urllib.parse import urlparse)

window = tk.Tk()
window.title("Youtube download")
window.geometry('450x300')

# #button for downloading mp4 (video & audio)
# checkbutton_mp4 = tk.Checkbutton(window,text='mp4', anchor=tk.W, indicatoron=0,padx=7)
# checkbutton_mp4.grid(row=0,column=2)

# #button for downloading mp3 (audio)
# checkbutton_mp3 = tk.Checkbutton(window, text='mp3', anchor=tk.W, indicatoron=0, padx=7)
# checkbutton_mp3.grid(row=0,column=3)

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
download_button = tk.Button(text='Download', font=('century gothic',15), command=lambda:download(convertTextToList()))
download_button.grid(row=3,column=0,sticky=(tk.N, tk.S, tk.E, tk.W),columnspan=3)

# scaling with window
window.columnconfigure(1, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(1, weight=1)

window.mainloop()

