# /usr/bin/env python3

import os
import shutil
from deepface import DeepFace

data_dir = "faces"
smallest_distance = None

for file in os.listdir(data_dir):
    print(file)
    result = DeepFace.verify(f"faces/{file}", "samples/bill_bur.jpeg")
    print(result)

## need data set for this guy
#for file in os.listdir("Samples"):
    #if file.endswith(".jpg"):
        #result = DeepFace.verify("person1.png", f"samples/{file}")