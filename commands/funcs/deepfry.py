import cv2
import numpy as np

# deepfry it
def fryImage(img):
    """
    Passes the image path, opens it with OpenCV and returns the image with drastic posterization
    :param imagePath: string | imagePath | Full image path
    """
    imageStart = cv2.imread(img)
    return badPosterize(imageStart)

def badPosterize(imageNormal):
    """
    Posterize the image through a color list, diving it and making a pallete.
    Finally, applying to the image and returning the image with a the new pallete
    :param imageNormal: CV opened image | imageNormal | The normal image opened with OpenCV
    """
    colorList = np.arange(0, 256)
    colorDivider = np.linspace(0, 255,3)[1]
    colorQuantization = np.int0(np.linspace(0, 255, 2))
    colorLevels = np.clip(np.int0(colorList/colorDivider), 0, 1)
    colorPalette = colorQuantization[colorLevels]
    return colorPalette[imageNormal]

def final(img):
    imageOpen = cv2.imread(img)
    imageFry = badPosterize(imageOpen)
    cv2.imwrite('assets/images/deepfry/deepfried.png', imageFry, [int(cv2.IMWRITE_JPEG_QUALITY), 0])
