'''
Make a logo for code club.

Created by: Benjamin Metha
Last Updated: Aug 03, 2023
'''

import matplotlib.pyplot as plt
import numpy as np

C = np.array([
[1,1,1,1,1],
[1,0,0,0,0],
[1,0,0,0,0],
[1,0,0,0,0],
[1,1,1,1,1]
])

flag = np.zeros((9,9))

flag[1:6,1:6] += C

flag[3:8, 3:8] += C

plt.imshow(flag)
plt.show()