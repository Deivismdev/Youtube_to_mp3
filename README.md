# Youtube_to_mp3

A GUI program for easy downloading videos from youtube and saving them as mp3's <br />
Made using python, pytube and tkinter. <br />

## How to use?
Just paste url's in the textbox, separated by spaces or new lines and click Download  <br />

## Example:
Clicking Download button without pasting any url's or pasting url's not from youtube videos will result in a message showing up "PASTE URL'S FROM YOUTUBE":  <br />
<img src="Images\image-1.png"/> <br />
Example of one of the ways to paste url's<br />
<img src="Images\image0.png"/> <br />
After clicking Download, files will be downloaded and saved into a directory named "downloaded files" in the same directory where program is located<br />
NOTE: program might freeze up while files are being downloaded. Work in progress!<br />
<img src="Images\image1.png"/> <br />

## Having errors?
Make sure to have pytube and tkinter installed 
<pre><code>pip install pytube 
pip install tkinter 
</code></pre>
Do not skip the first line when pasting url's
## Program crashing?
I know :( <br />
Work in progress... <br /> 
For now try not to drag the window while downloading<br />

## Future updates
* Ability to choose where files will be saved <br />
* Ability to choose between downloading mp3's and mp4's (or both) <br />
* <span style="color:green">Downloading files in parallel (DONE!)<br /></span>
* Progress bar <br />
* Fix crashing when dragging the window <br />