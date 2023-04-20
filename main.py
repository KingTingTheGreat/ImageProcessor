import os
from ascii_artist import AsciiArtist
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
from subprocess import Popen

def make_all():
    """ Make all the ascii art for all the images in the images folder """
    artist = AsciiArtist()
    for filename in os.listdir("images"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            txt_output = artist.resized(f"images/{filename}")
            with open(f"text_outputs/{filename.split('.')[0]}.txt", "w") as f:
                for line in txt_output:
                    f.write(''.join(line) + "\n")

if __name__ == "__main__":
    artist = AsciiArtist()
    Tk().withdraw()
    # add label to tk window
    file_location = askopenfilename(title="Select image file to process")
    # download_location = askdirectory(title="Select destination folder")
    download_location = "text_outputs"
    txt_output = artist.resized(file_location)
    name = file_location.split("/")[-1].split(".")[0]
    with open(f"text_outputs/{name}.txt", "w") as f:
        for line in txt_output:
            f.write(''.join(line) + "\n")
    Popen(f"notepad.exe text_outputs/{name}.txt")  
