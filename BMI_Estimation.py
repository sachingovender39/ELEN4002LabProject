# USAGE
# python object_size.py --width 0.955

import argparse
import csv
import cv2
import numpy as np
from initialise import CLASS_NAMES, color, config
from referenceObject import findReferenceObject as findRef
import binaryMask
import os
from mrcnn import model as modellib
from mrcnn import visualize

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--width", type=float, required=True,
	help="width of the left-most object in the image (in meters)")
ap.add_argument("-v", "--visualise", type=int, required=False,
	help="show all images etc.")
ap.add_argument("-m", "--mask", type=int, required=False,
	help="show masks on images etc.")
args = vars(ap.parse_args())

csvFile = open('person.csv', 'w')

# print("[INFO] loading Mask R-CNN model...")
# model = modellib.MaskRCNN(mode="inference", config=config, model_dir="logs")
# model.load_weights("mask_rcnn_coco.h5", by_name=True)

for filename in os.listdir('images'):
	if os.path.isdir('images/' + filename):
		continue

	image = cv2.imread('images/' + filename)
	clone = image.copy()
	# # convert to rgb image for model
	# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	# # perform forward pass of the network
	# print("[INFO] making predictions with Mask R-CNN...")
	# r = model.detect([image], verbose=1)[0]

	# # loop over of the detected object's bounding boxes and masks
	# for i in range(0, r["rois"].shape[0]):
	# 	# extract the class ID and mask
	# 	classID = r["class_ids"][i]
	# 	# ignore all non-people objects
	# 	if CLASS_NAMES[classID] != 'person':
	# 		continue
		
	# 	mask = r["masks"][:, :, i]
	# 	# visualize the pixel-wise mask of the object
	# 	image = visualize.apply_mask(image, mask, color, alpha=0.5)
	# 	# convert the image to BGR for OpenCV use
	# 	image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
		
	# 	(startY, startX, endY, endX) = r["rois"][i]
	# 	# extract the ROI of the image
	# 	roi = clone[startY:endY, startX:endX]
	# 	visMask = (mask * 255).astype("uint8")
	# 	# instance = cv2.bitwise_and(roi, roi, mask=visMask)
	# 	break
	pixelsPerMetric = findRef(clone, args["width"], args["visualise"], args["mask"])
	
	# thickness = [sum(row)/(255*pixelsPerMetric) for row in binImage]
	# thickness = [thickness[index] for index in np.nonzero(thickness)[0]]
	# thickness.insert(0, len(thickness)/pixelsPerMetric)
	# print(thickness)

	# 	writer = csv.writer(csvFile)
	# 	writer.writerows(map(lambda x: [x], thickness))
	# 	csvFile.write('END\n')

	# cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)
	# cv2.imshow("ROI", roi)
	# cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
	# cv2.imshow("Mask", visMask)
	# # cv2.namedWindow("Segmented", cv2.WINDOW_NORMAL)
	# # cv2.imshow("Segmented", instance)
	# cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
	# cv2.imshow("Output", image)

csvFile.close()
