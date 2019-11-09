We have done some data cleaning, so that we can work with
the RAVDESS and Berlin dataset. Both datasets used the filename
to store information such as the emotion, actor and gender of
the speaker in each audio track. We had to read these different
formats and extract the information into a common structure. We also
extracted the mfcc of each audio track and saved the new data structures
with the mfcc and standardadized features into a binary file in numpy format
for fast loading.


