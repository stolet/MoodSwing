from PIL import Image

import librosa
import numpy as np
import os

SRC_PATH = "data/ravdess"
TARGET_PATH = "data/ravdess2"
TARGET_IMG_EXT = ".PNG"  # PIL auto makes the file based on extension type


def image_loader(image_path: str) -> np.ndarray:
    audio, samp_rate = librosa.load(image_path, sr=None)
    stft = librosa.core.stft(audio)
    mag = np.abs(stft)  # magnitude
    print(mag.shape)
    return mag


# /data/ravdess/Actor_01/03-01-03-01-01-01-01.wav
for root, dirs, files in os.walk(SRC_PATH):
    for filename in files:
        image_np = image_loader(os.path.join(root, filename))
        image = Image.fromarray(image_np.astype('uint8'))

        # make folder
        emotion = filename.split('-')[2]
        folder_path = os.path.join(TARGET_PATH, emotion)
        os.makedirs(folder_path, exist_ok=True)

        # save
        name_without_ext = os.path.splitext(filename)[0]

        image.save(os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT))  # remove the extension
