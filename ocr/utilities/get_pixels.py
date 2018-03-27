#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This module will contain helper methods utilized by neural network"""

from PIL import Image
import numpy as np


def get_pixels(img):
    """This method takes image as an argument
    and convert it to bi-level format
    and return two dimensional array of 0,1
    where 0 - black 1 - white"""
    bw_img = img.convert('1')
    pix = np.array(bw_img, dtype=int)
    return pix


def resize_image(path, size=(16, 16)):
    """This method takes 2 arguments: path to the image
    and a tuple representing resolution of new image.
    It returns a new resized image object."""
    old_img = Image.open(path)
    new_img = old_img.resize(size, Image.LANCZOS)
    return new_img
