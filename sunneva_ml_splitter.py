import numpy as np
import pandas as pd
import os
import sys
import argparse
from sklearn.model_selection import train_test_split as tts

#   Script that takes a tab separated file (sunneva) and splits it into train val (8/2)

parser = argparse.ArgumentParser("sunneva_splitter")
parser.add_argument("filepath", help="Path to file for splitting")
args = parser.parse_args()

data = pd.read_csv(args.filepath, header=None, names=['transcript', 'wav_filename', 'length'], sep="\t")
data = data.drop('length', axis=1)

train, val = tts(data, test_size=0.2, random_state=42)

print("Train: " + str(len(train)))
print("Val: " + str(len(val)))

train.to_csv("metadata_train.txt", encoding='utf-8', index=None, header=False)
val.to_csv("metadata_val.txt", encoding='utf-8', index=None, header=False)
