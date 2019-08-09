import numpy as np
import pandas as pd
import os
import sys
import argparse
from sklearn.model_selection import train_test_split as tts

#   Script that takes a tab separated file (sunneva) and splits it into train, test and val (8/1/1)

parser = argparse.ArgumentParser("sunneva_splitter")
parser.add_argument("filepath", help="Path to file for splitting")
args = parser.parse_args()

data = pd.read_csv(args.filepath, header=None, names=['transcript', 'wav_filename', 'length'], sep="\t")
data = data.drop('length', axis=1)

train, rest = tts(data, test_size=0.2, random_state=42)
test, val = tts(rest, test_size=0.5, random_state=42)

print("Train: " + str(len(train)))
print("Test: " + str(len(test)))
print("Val: " + str(len(val)))

train.to_csv("s_train.tsv", encoding='utf-8', index=None, header=False)
test.to_csv("s_test.tsv", encoding='utf-8', index=None, header=False)
val.to_csv("s_val.tsv", encoding='utf-8', index=None, header=False)
