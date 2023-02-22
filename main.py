import os
import pyautogui
from PIL import Image
import numpy as np
import time

# Set x, y, width, height of the region to capture
x, y, width, height = (166, 97, 1149-166,1307-97)

# Initialize previous_img variable with None
previous_img = None

# Initialize consecutive_same variable with 0
consecutive_same = 0
time.sleep(5)
i = 0
while True:
    # capture screen
    img = pyautogui.screenshot(region=(x, y, width, height))

    # Compare image with previous image
    if previous_img is not None and (np.array(img) == np.array(previous_img)).all():
        consecutive_same += 1
    else:
        consecutive_same = 0

    # Check if same image is captured 3 times consecutively
    if consecutive_same >= 5:
        break

    # create the "Desktop/test" folder if it doesn't exist
    save_path = os.path.join(os.path.expanduser("~"), "Desktop/ml1")
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # save image
    img.save(f'{save_path}/{i}.png')


    time.sleep(0.1)
    # press right arrow key after 1 second
    pyautogui.press('right')
    time.sleep(0.1)


    # update previous_img variable
    previous_img = img

    i += 1