from PIL import Image, ImageOps

class AsciiArtist:

    def __init__(self):
        self.canvas = None
        self.chars = ' _.,-=+:;cba!?0123456789$W#@Ñ'
        self.chars = self.chars[::-1]

    def _one_to_one_from_file(self, filename:str) -> list[list[str]]:
        try:
            img = Image.open(filename)
            img = ImageOps.grayscale(img)
        except:
            print('File not found')
            return
        return self._one_to_one_from_image(img)

    def _one_to_one_from_image(self, image=Image) -> list[list[str]]:
        width, height = image.size
        pixels = image.load()
        for i in range(height):
            row = []
            for j in range(width):
                val = pixels[j, i]
                row.append(self.chars[int(val / 256 * len(self.chars))])
            self.canvas.append(row)
        return self.canvas

    def one_to_one(self, filename=None, image=None) -> list[list[str]]:
        if bool(filename) == bool(image):
            raise ValueError('Must provide exactly one of filename or pixels')
        self.canvas = []
        if filename:
            return self._one_to_one_from_file(filename)
        return self._one_to_one_from_image(image)

    def resized(self, filename:str, width:int=None, height:int=None) -> list[list[str]]:
        if bool(width) != bool(height):
            raise ValueError('Must provide both or neither of width and height')
        try:
            img = Image.open(filename)
            img = ImageOps.grayscale(img)
            w = int((width or 100) * (2.35))
            img = img.resize((w, height or 100))
        except:
            print('File not found')
            return
        return self.one_to_one(image=img)