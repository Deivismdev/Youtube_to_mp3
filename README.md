# Youtube_to_mp3

A GUI program for easy downloading videos from youtube and saving them as mp3's <br />
Made using python, pytube and tkinter. <br />

## How to use?
Just paste url's in the textbox, separated by spaces or new lines and click Download button  <br />

## Example:
Running the program<br />
<img src="Images\image0.png"/> <br />
Clicking Download button without pasting any url's or pasting url's not from youtube videos will result in a message showing up "PASTE URL'S FROM YOUTUBE":  <br />
<img src="Images\image-1.png"/> <br />
Pasting url's and clicking Download button will result in a message showing up "DOWNLOADING..." and progress bar moving<br />
<img src="Images\image1.png"/> <br />
Files will be downloaded and saved into a directory named "downloaded files" in the same directory where program is located<br />
<img src="Images\image3.png"/> <br />

## Having errors when running the code?
Make sure to have pytube and tkinter installed 
<pre><code>pip install pytube 
pip install tkinter 
</code></pre>


## Future updates
* Ability to choose where files will be saved <br />
* Ability to choose between downloading mp3's and mp4's (or both) <br />
* <span style="color:green">Downloading files in parallel (DONE!)<br /></span>
* <span style="color:yellow"> Progress bar (kinda done)<br />
* <span style="color:green">Fix crashing when dragging the window (DONE!) <br /></span>

## Change log
2021-09-22 v1.0 <br />
First release  <br />
2021-09-22 v1.1 <br />
Downloaded mp3's are now saved into a separate directory. Code clean up  <br />
2021-09-27 v1.2 <br />
Videos download faster using multithreading. Program still crashes because Tkinter is single-threaded :(.<br />
2021-10-06 v2.0 <br />
Reimplimented multithreading (correctly this time), downloading is fast and program no longer crashes! Added progress bar + label to indicate downloading process. New logo.