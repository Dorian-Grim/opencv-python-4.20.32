#dovadă că nu-s pleavă
import os, cv2, glob  #opencv-python==4.2.0.34
from pprint import pprint
def vconcat_resize(img_list, interpolation=cv2.INTER_CUBIC): 
      # take minimum width 
    padding = 8
    w_max = max(img.shape[1] for img in img_list) + padding

    # resizing images 
    r = cv2.vconcat([cv2.copyMakeBorder(img, padding, padding, padding, padding if img.shape[1] == w_max else w_max - img.shape[1], cv2.BORDER_CONSTANT, value=[255,255,255]) for img in img_list])
    return r
final = 'final.png'
try: os.remove(final) 
except: pass
cv2.imwrite(final, vconcat_resize([cv2.imread(file) for file in glob.glob('*.png')])) # write final photo