import sys

from DotToDot import makeDotToDot, makeMaxSizeDot

MAX_DOTS_IN_IMAGE = 800

arguments = len(sys.argv)

if arguments > 1:
    fullFilePath = sys.argv[1]
    makeDotToDot(fullFilePath, MAX_DOTS_IN_IMAGE)
    # makeMaxSizeDot(fullFilePath, MAX_DOTS_IN_IMAGE)
else:
    print( 'Please supply an image as an arguments')
