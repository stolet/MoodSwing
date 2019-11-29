from PIL import Image

import librosa
import numpy as np
import os

SRC_PATH = "data/ravdess"
TARGET_PATH = "data/ravdess2"
TARGET_IMG_EXT = ".PNG"  # PIL auto makes the file based on extension type


def image_loader(image_path: str) -> np.ndarray:
<<<<<<< Updated upstream
    audio, samp_rate = librosa.load(image_path, sr=None) #uses 2048 fft bins
=======
    audio, samp_rate = librosa.load(image_path, sr=None)  # uses 2048 fft bins
>>>>>>> Stashed changes
    stft = librosa.core.stft(audio)
    mag = np.abs(stft).T  # magnitude, transpose since output would be 1025x310 otherwise
    print(mag.shape)
    return mag


<<<<<<< Updated upstream
# /data/ravdess/Actor_01/03-01-03-01-01-01-01.wav
for root, dirs, files in os.walk(SRC_PATH):
    for filename in files:
        image_np = image_loader(os.path.join(root, filename))
        image = Image.fromarray((image_np * 255).astype('uint8'))

        # make folder
        emotion = filename.split('-')[2]
        folder_path = os.path.join(TARGET_PATH, emotion)
        os.makedirs(folder_path, exist_ok=True)

        # save
        name_without_ext = os.path.splitext(filename)[0]

        image.save(os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT))  # remove the extension
=======
def emotion_folders():
    # makes 01, 02, ..., 08 folders with training spectrograms
    # /data/ravdess/Actor_01/03-01-03-01-01-01-01.wav
    for root, dirs, files in os.walk(SRC_PATH):
        for filename in files:
            image_np = image_loader(os.path.join(root, filename))
            image = Image.fromarray((image_np * 255).astype('uint8'))

            # make folder
            emotion = filename.split('-')[2]
            folder_path = os.path.join(TARGET_PATH, emotion)
            os.makedirs(folder_path, exist_ok=True)

            # save
            name_without_ext = os.path.splitext(filename)[0]

            image.save(os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT))  # remove the extension


# split is 0.0 - 1.0, eg. 0.9 means 90% in test
def emotion_folders(split: float = 0.8):
    # makes 01_train, 01_test, ..., 08_train, 08_test folders with training spectrograms

    # ravdess2/01/03-01-03-01-01-01-01.wav
    for root, dirs, files in os.walk(TARGET_PATH):
        for dir in dirs:
            n = len(files)  # find num n of files in directory
            print(n)
            rand_idxs = np.random.permutation(n)  # make randomize list of n indexes

            # put first split% of indexes in set s
            train_len = int(n * split)
            test_idxs, train_idxs = np.array_split(rand_idxs, [train_len])
            train_set = set(train_idxs)

            train_path = os.path.join(root, dir + '_train')
            test_path = os.path.join(root, dir + '_test')
            os.makedirs(train_path, exist_ok=True)
            os.makedirs(test_path, exist_ok=True)
            for i, filename in enumerate(files):
                # if index in s, store in test folder

                image_np = image_loader(os.path.join(root, filename))
                image = Image.fromarray((image_np * 255).astype('uint8'))

                # make folder
                emotion = filename.split('-')[2]
                folder_path = os.path.join(TARGET_PATH, emotion)

                # save
                name_without_ext = os.path.splitext(filename)[0]

                path = os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT)
                if i in train_set:
                    path = os.path.join(folder_path, name_without_ext + TARGET_IMG_EXT)
                image.save(path)
>>>>>>> Stashed changes
