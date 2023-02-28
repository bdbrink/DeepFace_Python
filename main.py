# /usr/bin/env python3

import os
import shutil
from deepface import DeepFace

data_dir = "faces"
smallest_distance = None

#for directory in os.listdir(data_dir):
    #first_file = os.listdir(os.path.join(data_dir, directory))[0]
    #shutil.copyfile(os.path.join(data_dir, directory, first_file), os.path.join("samples", f"{directory}".jpg))

result = DeepFace.verify("faces/billy_bur.jpeg", "samples/bill_bur.jpeg")
print(result)

## need data set for this guy
#for file in os.listdir("Samples"):
    #if file.endswith(".jpg"):
        #result = DeepFace.verify("person1.png", f"samples/{file}")