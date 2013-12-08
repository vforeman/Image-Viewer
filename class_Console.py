###################Console.py
####
####Test Image:	"C:\Users\user\Pictures\tongue.jpeg"
##############	tongue.jpeg
from PIL import Image
import os
import sys


def getFile():

    filename=''
    while not os.path.isfile(filename):
    	filename=raw_input("enter filename")
    	os.system('cls')
    return filename


    bl[b]
