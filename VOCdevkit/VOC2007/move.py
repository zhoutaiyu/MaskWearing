import os
import shutil

def changewh():
    img_dir = "D:/database/data1/VOCdevkit/VOC2007/JPEGImages/"
    des_dir = "D:/database/data1/VOCdevkit/VOC2007/Annotations1/"
    files = os.listdir(img_dir)
    for img_file in files:
        if os.path.isfile(os.path.join(img_dir, img_file)):
            ann = os.path.join(img_dir, img_file).replace("jpg", "xml").replace("JPEGImages", "Annotations")
            shutil.move(ann,des_dir)
changewh()
