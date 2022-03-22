import cv2 as cv
import numpy as np

image = cv.imread('puzzle-piece-transparent.png')

cv.imshow('Image', image)

grey = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

blur = cv.GaussianBlur(grey,(5,5),0)

# thresh = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
ret, thresh = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow('Threshold', thresh)


edged = cv.Canny(thresh.copy(), 100, 200)

cv.imshow('Edges', edged)


cv.waitKey(0)

cv.destroyAllWindows()