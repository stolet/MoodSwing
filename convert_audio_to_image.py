# converts wave files to mel spectrograms and vice versa
from PIL import Image
from typing import Tuple

import librosa
import numpy as np
import os

SRC_PATH = "data/ravdess"
TARGET_PATH = "data/ravdess2"
TARGET_IMG_EXT = ".PNG"  # PIL auto makes the file based on extension type


def audio_to_img(image_path: str) -> Tuple[np.ndarray, int]:
    y, sr = librosa.load(image_path, sr=None)  # uses 2048 fft bins
    mel = librosa.feature.melspectrogram(y)
    mel = np.abs(mel)
    mel *= 255 / mel.max()
    mel = mel.astype('uint8')
    return mel, sr


def img_to_audio(fp: str, sr: int, write_path=None) -> np.ndarray:
    im = Image.open(fp).convert('L')
    im_np = np.array(im).astype('float64')
    print(im_np.shape)
    audio = librosa.feature.inverse.mel_to_audio(im_np)
    if write_path:
        librosa.output.write_wav(write_path, audio, sr)
    return audio


def save_image(image_np: np.ndarray, save_path: str) -> None:
    image = Image.fromarray(image_np)
    image.save(save_path)


def demo_audio():
    import tempfile
    from IPython import display
    img_contents, sr = audio_to_img('../data/ravdess/Actor_01/03-01-01-01-01-01-01.wav')  # neut
    #     img_contents, sr = audio_to_img('../data/ravdess/Actor_01/03-01-05-01-01-01-01.wav')
    fp_img = '/tmp/dump.png'
    save_image(img_contents, fp_img)
    audio = img_to_audio(fp_img, sr, write_path=None)
    #     print(audio.shape)
    return display.Audio(audio, rate=sr)


def emotion_folders():
    # makes 01, 02, ..., 08 folders with training spectrograms
    # /data/ravdess/Actor_01/03-01-03-01-01-01-01.wav
    for root, dirs, files in os.walk(SRC_PATH):
        for filename in files:
            # make folder
            emotion = filename.split('-')[2]
            folder_path = os.path.join(TARGET_PATH, emotion)
            os.makedirs(folder_path, exist_ok=True)

            # save
            name_without_ext = os.path.splitext(filename)[0]

            img_contents, sr = audio_to_img(os.path.join(root, filename))
            save_image(img_contents,
                       os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT))  # remove the extension


# demo_audio()
emotion_folders()
