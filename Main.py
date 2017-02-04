import sys
import time
import copy
import itertools
from PIL import Image

import cv2

# from SegmentImage import SegmentImage
# from SegmentHoleFilling import SegmentHoleFilling
# from SegmentCenterRemoval import SegmentCenterRemoval
# from TraceFollower import TraceFollower
# from TraceConnecter import TraceConnecter
# from IntermediateImage import IntermediateImage
# from OutputImage import OutputImage

from EdgeDetector import EdgeDetector

arguments = len(sys.argv)

if arguments > 1:
    if arguments == 2:
        fileName = "simple.jpg"
    else:
        fileName = sys.argv[2]

    similarity = int(sys.argv[1])
else:
    fileName = "simple.jpg"
    similarity = 40

# Canny Method:
edgeDetector = EdgeDetector(fileName)
edges = edgeDetector.chooseCannyImage(5)
cv2.imwrite("out.jpg", edges)

# Segment Method:
'''
imageData = Image.open(fileName)
width = imageData.width
height = imageData.height

segmentImage = SegmentImage(fileName, similarity)

start = time.clock()
segments = segmentImage.getSegments()
end = time.clock()
print ("---- Segmentation time : " + str(end - start) + " ----")

holeFilling = SegmentHoleFilling(segments, width, height)
start = time.clock()
filledSegments = holeFilling.getFilledSegments()
end = time.clock()
print ("---- Hole fill time : " + str(end - start) + " ----")

intermediate = IntermediateImage(filledSegments, width, height)
intermediate.colorLargestSegments()
intermediate.showImage()
intermediate.saveImage("segments.jpg")

centerRemover = SegmentCenterRemoval(filledSegments, width, height)

start = time.clock()
outlines = centerRemover.getSegmentOutlines()
end = time.clock()
print ("---- Center removal time : " + str(end - start) + " ----")

intermediate = IntermediateImage(outlines, width, height)
intermediate.colorLargestSegments()
intermediate.showImage()

traceFollower = TraceFollower(outlines, width, height)

start = time.clock()
dottedSegments = traceFollower.getDottedSegments()
end = time.clock()
print ("---- Defining points time : " + str(end - start) + " ----")

connecter = TraceConnecter(dottedSegments, width, height)
points = connecter.getConnectedTraces()

print ("---- Points in image: " + str(len(points)) + " ----")
out = OutputImage(points, (width, height), True)
out.showImage()
out.saveImage()


#cornerImage = copy.copy(image)
#cornerImage.plotAllSegmentCorners(segmentCorners)
#cornerImage.imageData.save("out_corners.jpg")
'''
