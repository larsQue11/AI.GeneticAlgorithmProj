# https://www.youtube.com/watch?v=nrKjSeoc7fc
# https://stackoverflow.com/questions/44497352/printing-colors-on-screen-in-python
# https://stackoverflow.com/questions/12187354/get-rgb-value-opencv-python

#Load target image and store the RGB data

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

    def mutate(self):

        self.binary
'''
1: create random image pool
2: find fitness of each pixel
3: find total fitness of each image
4: create an image from all the best pixels
5: rest of pool generated through crossover
'''

#crossover of the parent genes, returns to children: 1 where the first parent's genes are first and another
#where the second parent's genes are first
def crossover(parent1Genes, parent2Genes):
    
    genes1 = parent1Genes[:]
    genes2 = parent2Genes[:]
    
    DNAchildA = parent1Genes + parent2Genes
    DNAchildB = parent2Genes + parent1Genes

    childA = Game(DNAchildA)
    childB = Game(DNAchildB)

    return childA, childB

# targetImage.save('test.png')

def main():
    
    #Pixel dimensions(widthxheight): 480x451
    targetImage = Image.open('KSU_Logo.png')

    pixels = list(targetImage.getdata())
    width, height = targetImage.size
    
    listOfPixels = np.array([[Pixel(pixels[i]) for i in range(j,width + j)] for j in range(height)])

    # im = Image.fromarray(np.array([[(255,255,255,255),(0,0,0,0)],[(0,0,0,0),(255,255,255,255)]]).astype('uint8'), 'RGB')
    # im.save('testq.png')

    


if __name__ == "__main__":
    main()