#!/usr/bin/env python
height = [1.78 , 1.70 , 1.84 , 1.69 ]
weight = [68 , 55 , 70 , 55 ]
import numpy as np 
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np_weight / np_height ** 2
print(bmi[bmi > 20])
