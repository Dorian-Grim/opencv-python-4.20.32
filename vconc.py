#dovadă că nu-s pleavă
import cv2, glob  #opencv-python==4.2.0.34
from pprint import pprint
def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC): 
      # take minimum width 
    w_max = max(img.shape[1] for img in img_list) 

    # resizing images 
   
    return cv2.vconcat([cv2.copyMakeBorder(img, 0, 0, 0, 0 if img.shape[1] == w_max else w_max - img.shape[1], cv2.BORDER_CONSTANT, value=[255,255,255]) for img in img_list])

cv2.imwrite("final.png", vconcat_resize([cv2.imread(file) if file.endswith(".png") else 0 for file in glob.glob('*.png')])) # write final photo