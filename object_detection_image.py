'''
for windows
'''
import numpy as np
import time
import cv2
image = cv2.imread('test/ambulance.jpg')
classes = "yolo custom/classes.names"
with open(classes, 'r') as f:
    LABELS = [line.strip() for line in f.readlines()]
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
	dtype="uint8")
print("[INFO]: Loading image...")
net = cv2.dnn.readNet("yolo custom/yolov3_custom_last.weights","yolo custom/yolov3_custom.cfg")
try:
	(H, W) = image.shape[:2]
	print("[INFO]: Detecting object from image...")
except Exception as inst:
	print('[INFO]: Got Error while loading image:',inst)
	raise SystemExit()

ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
	swapRB=True, crop=False)
net.setInput(blob)
start = time.time()
layerOutputs = net.forward(ln)
end = time.time()
print("[INFO]: YOLO took {:.6f} seconds".format(end - start))
boxes = []
confidences = []
classIDs = []
for output in layerOutputs:
	for detection in output:
		scores = detection[5:]
		classID = np.argmax(scores)
		confidence = scores[classID]
		if confidence > 0.4:
			box = detection[0:4] * np.array([W, H, W, H])
			(centerX, centerY, width, height) = box.astype("int")
			x = int(centerX - (width / 2))
			y = int(centerY - (height / 2))
			boxes.append([x, y, int(width), int(height)])
			confidences.append(float(confidence))
			classIDs.append(classID)
idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.4,0.4)
if len(idxs) > 0:
	for i in idxs.flatten():
		(x, y) = (boxes[i][0], boxes[i][1])
		(w, h) = (boxes[i][2], boxes[i][3])
		color = [int(c) for c in COLORS[classIDs[i]]]
		cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
		text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
		cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, color, 2)
cv2.imwrite("output/output.jpg".format(i+1), image)
cv2.imshow("Image", image)
cv2.waitKey(0)