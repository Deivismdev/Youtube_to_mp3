# Youtube_downloader

A GUI program for easy downloading videos from youtube<br />
Made using python, pytube and tkinter. <br />

## Prerequisites

Make sure to have pytube and tkinter installed

<pre><code>pip install pytube 
pip install tkinter 
</code></pre>

## How to use?

Paste url's in the textbox, separated by spaces or new lines and click "Download" button.
<br />
By default Audio and Video will be downloaded, that can be changed by using radio buttons.
<br />
By default files will be saved on desktop in a folder "downloaded_from_yt", but that can be changed by clicking "Change destination" button.

## Demonstration:

<p align="center"> <img src="Images\image0.png"/></p>
<p align="center">User interface</p>
Clicking Download button without pasting any url's or pasting url's not from youtube videos will result in a message showing up "PASTE URL'S FROM YOUTUBE": <br /> <br />
<p align="center"> <img src="Images\image-1.png"/></p>
<p align="center">Clicking download without URL's</p>
Pasting url's and clicking Download button will result in a message showing up "DOWNLOADING..." and progress bar moving<br /> <br />
<p align="center"> <img src="Images\image1.png"/></p>
<p align="center">Download in progress</p>
Files will be downloaded and saved into a directory named "downloaded files" in the same directory where program is located<br /> <br />
<p align="center"> <img src="Images\image3.png"/> <br /></p>
<p align="center">Download complete</p>
