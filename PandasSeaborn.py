# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:49:59 2021

@author: diren
"""

import pandas as pd
import seaborn as sns

data_spotify = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv")

print(data_spotify.head(15))

print("Describe")
print(data_spotify.describe())

print("Describe -specific")
print(data_spotify.describe()['acousticness'])

print("info")
print(data_spotify.info())

print("MEAN -energy")
print(data_spotify['energy'].mean())

print("MEDIAN -energy")
print(data_spotify['energy'].median())

print("MODE -energy")
print(data_spotify['track_artist'].mode())

print("MODE -energy")
print(data_spotify['track_artist'].mode())

print("STANDARD DEVIATION -energy")
print(data_spotify['energy'].std())


#task4

#sns.countplot(y="track_album_name", data=data_spotify.iloc[0:10])#iloc

#data_spotify.energy.hist(bins=50)

#sns.scatterplot(data=data_spotify, x="valence", y="acousticness")

sns.pairplot(data_spotify)

