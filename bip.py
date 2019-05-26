from PIL import Image
import os

def process(filepath, filename):
    filename = filename[:-4]
    print(filename)
    image = Image.open(filepath)
    width, height = image.size
    image.thumbnail((width / 2 , height / 2), Image.ANTIALIAS)
    outputDir = os.getcwd() + "/output/"
    image.save(outputDir + filename + ".png", "PNG")



if __name__ == '__main__':
    dir = "/input"
    for filename in os.listdir(os.getcwd() + dir):
        process(os.getcwd() + dir + "/" + filename, filename)