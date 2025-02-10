# %%
import os
import cv2
import numpy as np
import matplotlib
import scipy
import mahotas
import skimage
import sklearn

print(os.getcwd())
print(cv2.__version__)
print(np.__version__)
print(matplotlib.__version__)
print(scipy.__version__)
print(mahotas.__version__)
# print(skimage.__version__)
print(sklearn.__version__)
# %%
im = cv2.imread('images/surrey-logo.png', flags=cv2.IMREAD_COLOR)
if im is None:
    print("Could not open or find the image")
else:
    cv2.imshow('Deer Image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('images/out.jpg', im)
# %%
