#dovadă că nu-s pleavă
import os, cv2  #opencv-python==4.20.0.32
from pprint import pprint
def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC): 
      # take minimum width 
    w_max = max(img.shape[1] for img in img_list) 
    w_min = min(img.shape[1] for img in img_list) 
    white = [255,255,255]

    # resizing images 
    im_list_rewrite = []
    for img in img_list:
        im_list_rewrite.append(cv2.copyMakeBorder(img,0,0,0,0 if img.shape[1] == w_max else w_max,cv2.BORDER_CONSTANT,value=white))
    # im_list_rewrite = [cv2.copyMakeBorder(img,0,0,0,0 if (img2.shape[1] == w_max for img in img_list) else w_max,cv2.BORDER_CONSTANT,value=white) for img in img_list]
    # im_list_resize = [cv2.resize(img, (w_max, int(img.shape[0] * w_max / img.shape[1])), interpolation = interpolation) for img in im_list_rewrite] 
    # return final image 
    return cv2.vconcat(im_list_rewrite)

x = [cv2.imread(file) if file.endswith(".png") else 0 for file in os.listdir()]
while 0 in x: x.remove(0)
vconcat_resize(x)