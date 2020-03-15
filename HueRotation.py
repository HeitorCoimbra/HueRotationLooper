#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
import numpy as np
import colorsys
import imageio

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(image, hue_offset):
    img = image.convert('RGBA')
    
    arr = np.array(np.asarray(img).astype('float')) # convert RGBA image to float data
    r, g, b, a = np.rollaxis(arr, axis=-1)   # take each individual value to translate to hsv
    h, s, v = rgb_to_hsv(r, g, b)   # convert to hsv
    h = (h + hue_offset)    # add offset and take module 360 as to loop the hue back to 0
    r, g, b = hsv_to_rgb(h, s, v)   # back to rgba
    arr = np.dstack((r, g, b, a))   # back to float data
    
    new_img = Image.fromarray(arr.astype('uint8'), 'RGBA') # back to image

    return new_img

def build_image_array(filepath, n_frames):
    '''
        This function takes LONG.
        It may vary depending on the image size, total_frames and hardware.
        It'll take between 10 minutes and one hour if the total data to be processed is under 400MB.
        (total data = image size * n_frames)
    '''
    
    im = Image.open(filepath)

    images = []
    step_size = int(np.ceil(1000/n_frames))
    print('Step size:', step_size)
    for i in range(0, 1000, step_size):
        rotated_hue_image = shift_hue(im, i/1000.0)
        
        print(i)
        
        images.append(rotated_hue_image)
    return images


def write_and_save_video(images, filepath='video.avi', framerate=15):
    writer = imageio.get_writer(filepath, fps=framerate)

    for image in images:
        writer.append_data(np.asarray(image).astype(np.uint8))
    writer.close()
    
def main():
    filepath = r'path\to\image.png' # Replace this
    destination_filepath = 'path\to\save\video.avi' # and this
    image_array = build_image_array(filepath, 180)
    write_and_save_video(image_array, filepath=destination_filepath, framerate=30)
    
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




