from skimage import color
import scipy.misc
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import matplotlib.pyplot as plt
import sys


"""
Runs KMeans Algorithm with size_palette clusters on rasterized image 
and returns palette of centroids. 
"""
def getKMeansPalette(raster, size_palette):
  print raster


def main():

  """
  if not specified, use peacock.jpg as source, flowers.jpg as dest, and palette of
  size 5.
  """

  DEFAULT_SRC_PATH = "images/peacock.jpg"
  DEFAULT_DEST_PATH = "images/flowers.jpg"
  DEFAULT_SIZE_PALETTE = 5

  raster_src = scipy.misc.imread("images/" + sys.argv[2] if len(sys.argv) > 1 else
                                  DEFAULT_SRC_PATH)
  raster_dest = scipy.misc.imread("images/" + sys.argv[2] if len(sys.argv) > 1 else
                                  DEFAULT_DEST_PATH)
  size_palette = sys.argv[3] if len(sys.argv) != 0 else DEFAULT_SIZE_PALETTE

  src_palette_KMeans = getKMeansPalette(raster_src, size_palette)


if __name__ == "__main__":
  main()

