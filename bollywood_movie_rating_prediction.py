#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:22:51 2018

@author: tapan
"""


import pandas as pd
import numpy as np

from sklearn import linear_model
from sklearn import tree
import matplotlib.pyplot as plt


df_movie = pd.read_csv('BollywoodMovieDetail.csv')
df_actor = pd.read_csv('BollywoodActorRanking.csv')
df_director = pd.read_csv('BollywoodDirectorRanking.csv')




# Dropping Unused columns 
df_movie.drop(columns=['imdbId', 'title', 'releaseYear', 'releaseDate'],axis=1, inplace=True)

df_movie.fillna("", inplace=True)


categorical_features = ["genre"]
df_movie = pd.get_dummies(df_movie, columns=categorical_features)




#output = []
#
#
#for index, row in df_movie.iterrows():
##   print ("{}: {}".format(index, row['genre'].split('|')))
#   words = row['genre'].split('|')
#   for gener in words:
#        if gener not in output and gener == '':
##            print(gener)
#            output.append(gener.strip())
#            
##for eachItem in list(set(output)):
##    if eachItem != '':
##        df_movie["g.{}".format(eachItem)] = 1
#        
#
##print(list(set(output)))
#        
#for index, row in df_movie.iterrows():
#    if '|' in row['genre']:
#        print("{}: {}".format(index, row['genre'].split('|')))
#        words = row['genre'].split('|')
##        print(words)
##        for gener_new in words:
##            if gener_new not in words:
##                df_movie["g.{}".format(gener_new.strip())] = 0
#    else:
#        print("{}:: {}".format(index, row['genre']))
#        for eachSingleItem in list(set(output)):
#            if row['genre'] != '':
#                df_movie["g.{}".format(row['genre'])] = 1
#        
#        
#        
        
        
        
        
        
        
        
        