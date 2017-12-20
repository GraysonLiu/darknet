import python.darknet
import os, sys

net = python.darknet.load_net("cfg/yolo.cfg", "weights/yolo.weights", 0)
meta = python.darknet.load_meta("cfg/coco.data")

folder = sys.argv[1]
print folder
files = os.listdir(folder)

for f in files:
    if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png"):
        print f
        path = os.path.join(folder, f)
        im = python.darknet.load_image(path, 0, 0)
        res = python.darknet.detect(net, meta, im)
        print res[:3]
