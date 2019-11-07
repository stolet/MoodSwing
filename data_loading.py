import numpy as np
import pandas
import glob
import os

ravdess_path = "data/ravdess/"
berlin_path = "data/berlin/wav/"

class Dataset():
    def __init__(self, dataset_path):
        self.data = []
        self.dataset_path = dataset_path

    def load(self):
        # Counts number of files in directory
        n = self._get_num_files(self.dataset_path)
        self.data = np.array(n)
        for filename in glob.iglob(self.dataset_path + "**", recursive=True):
            if ".wav" in filename:
                print(filename)

    def _get_num_files(self, path):
        total = 0
        for root, dirs, files in os.walk(path):
            total += len(files)
        return total
 
class RavdessDataset(Dataset):
    def __init__(self):
        super(Dataset, self).__init__()

    def load(self):
        pass

class BerlinDataset(Dataset):
    def __init__(self):
        super(Dataset, self).__init__()

    def load(self):
        pass



if __name__ == "__main__":
    print("Loading le data")
    ravdess = Dataset(ravdess_path)
    ravdess.load()
    berlin = Dataset(berlin_path)
    berlin.load()
