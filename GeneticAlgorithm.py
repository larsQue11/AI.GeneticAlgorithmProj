# https://www.youtube.com/watch?v=nrKjSeoc7fc
# https://stackoverflow.com/questions/44497352/printing-colors-on-screen-in-python
# https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python

#Load target image and store the RGBA data

#Set up genetic information

#Determine fitness criteria.
    #Percent correct
    #

from PIL import Image
import numpy as np

class Pixel():

    def __init__(self,RGBA):
        if isinstance(RGBA,list):
            self.red = RGBA[0]
            self.green = RGBA[1]
            self.blue = RGBA[2]
            self.alpha = RGBA[3]
            self.binary = self.toBinary()
        elif isinstance(RGBA,str):
            self.red = RGBA[:8]
            self.green = RGBA[8:16]
            self.blue = RGBA[16:24]
            self.alpha = RGBA[24:]
            self.binary = RGBA

    def toBinary(self):

        return bin(self.red)[2:] + bin(self.green)[2:] + bin(self.blue)[2:] + bin(self.alpha)[2:]

    #mutate the RGB string through a bite flip at a random position
    def mutate(self):

        indexOfBitFlip = np.random.randint(16)
        if self.binary[indexOfBitFlip] == 1:
            self.binary[indexOfBitFlip] = 0
        else:
            self.binary[indexOfBitFlip] = 1

# class myImage():

#     def __init__(self):

'''
1: create random image pool
2: find fitness of each pixel
3: find total fitness of each image
4: create an image from all the best pixels
5: rest of pool generated through crossover
'''

#crossover of the parent genes, returns to children: 1 where the first parent's genes are first and another
#where the second parent's genes are first
# def crossover(parent1Genes, parent2Genes):
    
#     genes1 = parent1Genes[:]
#     genes2 = parent2Genes[:]
    
#     DNAchildA = parent1Genes + parent2Genes
#     DNAchildB = parent2Genes + parent1Genes

#     childA = Game(DNAchildA)
#     childB = Game(DNAchildB)

    # return childA, childB

# 

def main():
    
    #Pixel dimensions(widthxheight): 480x451
    targetImage = Image.open('KSULogoProcessed.png')
    # targetImage.save('test.png')
    pixels = list(targetImage.getdata())
    width, height = targetImage.size
    
    print(len(pixels))
    narr = np.reshape(pixels,(width,height))
    for x in range(width):
        for y in range(height):
            currentColor = img.getpixel((x,y))
            if currentColor == (177,179,179):
                # change to white if not desired color
                img.putpixel((x,y), (255, 255, 255))
    # narr = np.array([[pixels[px] for px in range(h,height+h)] for h in range(width)], dtype=np.uint8)
    # listOfPixels = np.array([[Pixel(pixels[i]) for i in range(j,width + j)] for j in range(height)])
    # pixels = np.array([[[255, 255, 255, 255], [0, 0, 0, 255]], [[0, 0, 0, 255], [255, 255, 255, 255]]], dtype=np.uint8)
    # pixels = np.transpose(pixels,(1, 0, 2))

    # im = Image.fromarray(np.transpose(narr,(1, 0, 2)), 'RGB')
    # im.save('test.png')

    


if __name__ == "__main__":
    main()