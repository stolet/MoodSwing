# converts wave files to mel spectrograms and vice versa
from PIL import Image
from typing import Tuple

import librosa
import numpy as np
import os

TARGET_AUDIO_EXT = ".WAV"


def img_to_audio(fp: str, sr: int, write_path=None) -> np.ndarray:
    im = Image.open(fp).convert('L')
    im_np = np.array(im).astype('float64')
    print(im_np.shape)
    audio = librosa.feature.inverse.mel_to_audio(im_np)
    if write_path:
        librosa.output.write_wav(write_path, audio, sr)
    return audio


# converts all pngs in directory recursively to be audio
def convert_all_audio(style_path='cyclegan-qp/samples/na'):
    for root, dirs, files in os.walk(style_path):
        for filename in files:
            name_without_ext = os.path.splitext(filename)[0]
            img_path = os.path.join(root, filename)
            print(img_path)
            img_to_audio(img_path, sr=48000,
                         write_path=os.path.join(root, name_without_ext + TARGET_AUDIO_EXT))


convert_all_audio()
