#converts wave files to spectrograms
from PIL import Image

import librosa
import soundfile as sf
import numpy as np
import os

SRC_PATH = "cyclegan-qp/samples/na/rec/"
TARGET_PATH = "cyclegan-qp/samples/audio/"
TARGET_IMG_EXT = ".wav"  # PIL auto makes the file based on extension type


def image_loader(image_path: str) -> np.ndarray:

    audio, samp_rate = librosa.load(image_path, sr=None) #uses 2048 fft bins
    stft = librosa.core.stft(audio)
    mag = np.abs(stft).T  # magnitude, transpose since output would be 1025x310 otherwise
    print(mag.shape)
    return mag

def img2sound(fp):
    im = Image.open(fp).convert('L')
    im_np = np.array(im)
    audio = librosa.core.istft(im_np)
    # audio_file = open(TARGET_PATH + "sty.wav", "w+")
    #sf.write(TARGET_PATH + "sty.wav", audio, 48000)
    librosa.output.write_wav(TARGET_PATH + 'rec.wav', audio, 48000)
    # audio_file.close()


# /data/ravdess/Actor_01/03-01-03-01-01-01-01.wav
for root, dirs, files in os.walk(SRC_PATH):
    for filename in files:
        img_path = os.path.join(root, filename)
        print(img_path)
        sound = img2sound(img_path)
        # image_np = image_loader(os.path.join(root, filename))
        # image = Image.fromarray((image_np * 255).astype('uint8'))
        #
        # # make folder
        # emotion = filename.split('-')[2]
        # folder_path = os.path.join(TARGET_PATH, emotion)
        # os.makedirs(folder_path, exist_ok=True)

        # save
        # name_without_ext = os.path.splitext(filename)[0]
        #
        # image.save(os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT))  # remove the extension
