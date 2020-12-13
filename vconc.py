#dovadă că nu-s pleavă
import os, cv2, glob  #opencv-python==4.2.0.34
from pprint import pprint
def vconcat_resize(img_list,interpolation=cv2.INTER_CUBIC): 
      # take minimum width 
    padding = 15
    
    img_list_with_emoji = [] 
    i = 0
    for img in img_list:
        char = chr(i + 97)
        emoji = cv2.imread("emojis/regional_indicator_"+char + ".png")
        temp = hconcat_resize([emoji, img])
        img_list_with_emoji.append(temp)
        i += 1
    w_max = max(img.shape[1] for img in img_list_with_emoji) + padding    
    r = cv2.vconcat([cv2.copyMakeBorder(img, 8, 8, padding, padding if img.shape[1] == w_max else w_max - img.shape[1], cv2.BORDER_CONSTANT, value=[255,255,255]) for img in img_list_with_emoji])
    return r
def hconcat_resize(img_list,interpolation=cv2.INTER_CUBIC): 
    # take minimum hights 
    h_min = min(img.shape[0] for img in img_list) 
      
    # image resizing  
    im_list_resize = [cv2.resize(img,(int(img.shape[1] * h_min / img.shape[0]),h_min), interpolation= interpolation)for img in img_list] 
      
    # return final image 
    return cv2.hconcat(im_list_resize) 
final = 'final.png'
try: os.remove(final) 
except: pass
cv2.imwrite(final, vconcat_resize([cv2.imread(file) for file in glob.glob('*.png', recursive=False)])) # write final photo