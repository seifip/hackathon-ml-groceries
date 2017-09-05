import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from pathlib import Path
import os 

p = Path(os.path.dirname(os.path.realpath(__file__)))
train_dir = p/'train_img'
Path.mkdir(p/'data', exist_ok=True)
data_dir = p/'data'
if Path.exists(train_dir):
    train_dir.rename(data_dir/'train')
train_dir = data_dir/'train'

Path.mkdir(data_dir/'validation', exist_ok=True)
validation_dir = data_dir/'validation'

''' X_train, X_test = train_test_split([x for x in train_dir.iterdir()], test_size=0.25, random_state=0)

for f in X_test:
    f.rename(data_dir/'validation'/f.name) '''

train_data = pd.read_csv(p/'train.csv')

train_files = [x for x in train_dir.iterdir()]
validation_files = [x for x in validation_dir.iterdir()]

''' labels = train_data['label'].unique()
for label in labels:
    Path.mkdir(train_dir/label, exist_ok=True)
    Path.mkdir(validation_dir/label, exist_ok=True) '''

for f in train_files:
    label = train_data[train_data['image_id'] == f.stem]['label'].values
    if len(label) > 0:
        f.rename(train_dir/label[0]/f.name)

for f in validation_files:
    label = train_data[train_data['image_id'] == f.stem]['label'].values
    if len(label) > 0:
        f.rename(validation_dir/label[0]/f.name)