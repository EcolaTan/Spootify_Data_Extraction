import pandas as pd
import matplotlib.pyplot as plt

spotify= pd.read_csv("data.csv")
spotify = spotify.dropna() 
Region = spotify.groupby(by=["Region"])
Region = Region.get_group("ph")

mostStreamed = Region.groupby("Artist")["Streams"].sum().reset_index().sort_values('Streams',ascending=False) #sum the streams of the artist and sort from hi to low
mostStreamed['Streams'] = ['{:,.2f}Million'.format(x) for x in mostStreamed['Streams']/1000000] #format the streams to millions
mostStreamed = mostStreamed.head(20).reset_index() 
del mostStreamed["index"]
print(mostStreamed)

mostFrequent = Region['Track Name'].value_counts().reset_index().sort_index(ascending = True) #count how many times a track appear
mostFrequent.rename({'index': 'Track Name', 'Track Name': 'Occurences'}, axis=1, inplace=True) 
mostFrequent = mostFrequent.head(20)
#print(mostFrequent)

mostSongs = Region['Artist'].value_counts().reset_index().sort_index(ascending = True) #count how many times the song
mostSongs.rename({'index': 'Artist', 'Artist': 'Songs'}, axis=1, inplace=True)
mostSongs = mostSongs.head(20)
#print(mostSongs)

UniqueSongs = Region.groupby('Artist')['Track Name'].nunique().reset_index() #count unique tracks
UniqueSongs.rename({'Track Name': 'Songs'}, axis=1, inplace=True)
UniqueSongs = UniqueSongs.sort_values('Songs',ascending=False).reset_index(drop = True) #sort the tracks hi to low
UniqueSongs = UniqueSongs.head(20)
print(UniqueSongs)
UniqueSongs.plot.scatter(x = 'Artist', y = 'Songs', s = 10) #plot scatter
plt.tick_params(labelsize=6)
plt.show()

TopSongs = Region.groupby(['Artist','Track Name'],as_index=False)["Streams"].sum().reset_index().sort_values('Streams',ascending=False) #by streams while keeping the artist and track name col
TopSongs['Streams'] = ['{:,.2f}Million'.format(x) for x in TopSongs['Streams']/1000000] #change to million
TopSongs = TopSongs.head(20).reset_index()
del TopSongs["level_0"] #del unneccesrry cols
del TopSongs["index"]
print(TopSongs)
