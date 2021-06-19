#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import csv
import pandas as pd
import sys

labels_dict = []
data = []
sentence = []
label_list = []
assert len(sys.argv) == 3, "usage: python ner_prep.py <原始文件路径> <保存路径> "

file_path = sys.argv[1]
save_name = sys.argv[2]


with codecs.open(file_path, "r", "utf-8") as f:
    for line in f:
        if line.strip() != "":
            tmp= line.strip().split("\t")
            if tmp[0] not in labels_dict:
                labels_dict.append(tmp[0])
            data.append((tmp[1], tmp[0]))
        else:
            continue

with open("%s.tsv" % save_name, "w") as f:
    for ex in data:
        s = ex[0]
        l = ex[1]
        f.write(s+"\t"+l+"\n")

if save_name.find("train.tsv") > -1:
    with open("label.txt", "w") as f:
        for k in labels_dict:
            f.write(k+"\n")