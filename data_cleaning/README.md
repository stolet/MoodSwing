Nov 8, 2019 Progress Report

Data:
We have done some data exploration along the lines of strucutre,
lenght of audio samples, and distrubtion. The data has gone through
cleaning, so that we can work withthe RAVDESS and Berlin dataset.

Both datasets used the filename to encode various like emotion, actor and gender.

    Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
    Vocal channel (01 = speech, 02 = song).
    Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
    Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
    Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
    Repetition (01 = 1st repetition, 02 = 2nd repetition).
    Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).

We had to read these different formats and extract the information into a common structure. We also
extracted the MFCC of each audio track and saved the new data structures
with the MFCC and standardized features into a binary file in numpy format
for fast loading. The data then is parsed into X and y for simple analysis
of the MFCC to do classifcation of emotion so we can explore the model's
responsiveness to changing of features. The data is then brought into a PyTorch dataloader
for batching and randomization.

Model: 
A CNN based classication model is used for training and inference, but this is not
fully completed yet. We hope to get the CNN quickly finished so we can proceed to style
transfer.

