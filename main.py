from ascii_artist import AsciiArtist
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

if __name__ == "__main__":
    artist = AsciiArtist()
    Tk().withdraw()
    # add label to tk window
    file_location = askopenfilename(title="Select image file to process")
    download_location = askdirectory(title="Select destination folder")
    txt_output = artist.resized(file_location)
    name = file_location.split("/")[-1].split(".")[0]
    with open(f"text_outputs/{name}.txt", "w") as f:
        for line in txt_output:
            f.write(''.join(line) + "\n")
