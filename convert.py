# converts wave files to spectrograms
from PIL import Image
from typing import Tuple


import librosa
import soundfile as sf
import numpy as np
import os

SRC_PATH = "cyclegan-qp/samples/na/rec/"
TARGET_PATH = "cyclegan-qp/samples/audio/"
TARGET_IMG_EXT = ".wav"  # PIL auto makes the file based on extension type


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


def demo():
    import tempfile
    img_contents, sr = audio_to_img('../data/ravdess/Actor_01/03-01-01-01-01-01-01.wav')  # neut
    #     img_contents, sr = audio_to_img('../data/ravdess/Actor_01/03-01-05-01-01-01-01.wav')
    fp_img = '/tmp/dump.png'
    save_image(img_contents, fp_img)
    audio = img_to_audio(fp_img, sr, write_path=None)
    #     print(audio.shape)
    return display.Audio(audio, rate=sr)


demo()
