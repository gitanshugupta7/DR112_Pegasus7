import os
from PIL import Image
import detect_labels
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def resize_image(unique_id):
    path1 = "C:/Users/GITANSHU/DjangoAPI/Pothole_Backend_Kolkata_Vision/media/"+unique_id+".png"
    img = Image.open(path1) # image extension *.png,*.jpg
    new_width  = 640
    new_height = 480
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    path2 = "C:/Users/GITANSHU/DjangoAPI/Pothole_Backend_Kolkata_Vision/media/"+unique_id+"-resized.png"
    img.save(path2) # format

    p = detect_labels.detect_web(path2)
    os.remove(path2)
    return p