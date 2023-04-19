from ascii_artist import AsciiArtist
from tkinter import Tk
from tkinter.filedialog import askopenfilename

if __name__ == "__main__":
    artist = AsciiArtist()
    Tk().withdraw()
    filename = askopenfilename()
    txt_output = artist.resized(filename)
    name = filename.split("/")[-1].split(".")[0]
    print(name)
    with open(f"text_outputs/{name}.txt", "w") as f:
        for line in txt_output:
            f.write(''.join(line) + "\n")
