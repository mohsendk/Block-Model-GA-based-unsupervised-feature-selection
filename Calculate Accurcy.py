# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXtwahxW4pc1uvpOipFgqFeIoSj4qNmR
"""

# Section 5.3 .... accuracy for d = [16 364 128 200 600] for block model with lowest RRE
import csv
import numpy as np
import sklearn.preprocessing
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import mutual_info_score , adjusted_mutual_info_score
file2 = open("/content/dataset/BlogCatalog_Attributes.csv")
data2 = csv.reader(file2)
st = []
for m in data2:
    st.append(m)
file2.close()
lbl = np.genfromtxt(('/content/labels.csv'),delimiter=',')
lbl = lbl.astype(np.int32)
st = np.array(st)
st = st.astype(np.int64)
AccV = []
MILwVec = []
d = np.array([16,64,128,200,600])
file = open('/content/ours_blogcatalog_r.csv')
data = csv.reader(file)
r = []
for rL in data:
    r.append(rL)
file.close()
r2 = [float(r[i][0]) for i in range(0,len(r))]
r2 = np.array(r2)
r_Srt = np.sort(r2)[::-1]

for j in d:  
  cnt = 0;
  indx = [];
  while True:
    index1 = np.where(r2 == r_Srt[cnt])
    for i in range(0,len(index1)):
        indx.append(index1[i][0])
    if cnt == j:
      break
    cnt = cnt + 1;
  indx = np.array(indx)
  indx = indx.astype(np.int64)
  indx = indx[:j]
  st2 = st[:,indx]
  st2 = st2.astype(np.float64)
  sklearn.preprocessing.normalize(st2, norm='l2', axis=1, copy=False, return_norm=False)
  kmeans = sklearn.cluster.KMeans(n_clusters=6, init='k-means++', n_init=20, max_iter=300, tol=0.0001, verbose=0, random_state=None, copy_x=True, algorithm='elkan').fit(st2)
  Lb = kmeans.labels_
  AC = acc(lbl,Lb)
  # MILw = mutual_info_score(lbl, Lb, contingency=None)
  MILw = adjusted_mutual_info_score(lbl, Lb, average_method='arithmetic')
  MILwVec.append(MILw)
  AccV.append(AC)
AccV = np.array(AccV)
MILwVec = np.array(MILwVec)
AccV = 100*AccV