from PIL import Image
import numpy as np

def main():
    
    #Pixel dimensions(widthxheight): 480x451
    img = Image.open('KSU_LogoNoAlpha.png')
    width, height = img.size

    for x in range(width):
        for y in range(height):
            currentColor = img.getpixel((x,y))
            if currentColor == (177,179,179):
                # change to white if not desired color
                img.putpixel((x,y), (255, 255, 255))
            elif currentColor == (225,226,226):
                img.putpixel((x,y), (255, 255, 255))
            elif currentColor == (196,198,198):
                img.putpixel((x,y), (255, 255, 255))


    img.save("ProcessedLogo.png")

    # pixels = list(img.getdata())
    # print(pixels)
    # print(type(pixels))
    # for i in range(img.size[0]): # for every pixel:
    #     for j in range(img.size[1]):
    #         if pixels[i][j] != (0, 0, 0) or (255, 255, 255) or (177, 179, 179):
    #             # change to black if not red
    #             pixels[i][j] = (255, 255, 255)

    

    # listOfPixels = np.array([[Pixel(pixels[i]) for i in range(j,width + j)] for j in range(height)])
    # pixels = np.array([[[255, 255, 255, 255], [0, 0, 0, 255]], [[0, 0, 0, 255], [255, 255, 255, 255]]], dtype=np.uint8)
    # pixels = np.transpose(pixels,(1, 0, 2))
    # print(pixels)
    # print(np.shape(pixels))
    # editedImg = Image.fromarray(pixels, 'RGB')
    # editedImg.save('ProcessedKSULogo.png')

    


if __name__ == "__main__":
    main()