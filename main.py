# /usr/bin/env python3

import os
import shutil
from deepface import DeepFace

data_dir = "faces"

for directory in os.listdir(data_dir):
    first_file = os.listdir(os.path.join(data_dir, directory))[0]
    shutil.copyfile(os.path.join(data_dir, directory, first_file), os.path.join("Samples", f"{directory}".jpg))