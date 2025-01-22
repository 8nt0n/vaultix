from pathlib import Path

from lib_ffmpegUtils import get_video_length
from lib_ollamaUtils import *
from lib_imdb import *
from lib_movieJSUtils import *

from imdb import IMDb
import ollama
import re
import os

    #---------------------------------------------------------------------------#
    #                                                                           #
    #                             Extract Metadata                              #
    #                                                                           #
    #---------------------------------------------------------------------------#



#make some space
print()
print()

Uploader = input("Uploader: ")
moviesAdded = 0
moviesRefreshed = 0
moviesSkipped = 0


while True: #TODO
    Public = input("Public (y/n): ")

    if Public == "y":
        Public = "public"
        break
    elif Public == "n":
        Public = "private"
        break
    else:
        print("Answer has to be y/n")

#-----------------------------------------Setup llama3.2:1b-----------------------------------------#

init = ollama_init()


#-----------------------------------------get all .mp4 files from DIRECTORY and extract title with ollama-----------------------------------------#
DIRECTORY = 'D:/teststreamedv2'
DIR_len = len(DIRECTORY) +1
DIRECTORY = Path(DIRECTORY)

mp4_files = DIRECTORY.rglob('*.mp4')

print("+------------------------Movies------------------------+")
# Print the .mp4 files
for mp4_file in mp4_files:
    #print path to .mp4
    Path = str(mp4_file)
    file = Path[DIR_len:]
    print("path " + Path)

    #final movie title btw
    Title = ollama_prompt(file)
    print("Title:" + Title)

    #length of video
    Duration = get_video_length(Path)
    print(Duration)



    #-------------------------------get description, Rating, Tags from IMDB-----------------------#

    if Title != "main" and Title != "Main":
        # Create an instance of IMDb
        ia = IMDb()

        movies = ia.search_movie(Title) #returns all the movies imdb knows under that title

        if movies:

            # Get the first search result (most relevant)
            movie_id = movies[0].movieID
            movie = ia.get_movie(movie_id)
            Title = movie.get('title', 'N/A')
            print("new Title: " + Title)

            # Fetch and print the description
            Description = movie.get('plot outline', 'Description not available.')
            print(f"Description: {Description}")

            rating = movie.get('rating', '-1')

            genres = movie.get('genres', [])

            print(genres)
            print(rating)
        else:
            print("Movie not found!")
            Description = f'didnt find a movie named {Title} on IMDB'
            rating = -1
            genres = []
    else:
        print("no description for main.mp4")
        Description = "main.mp4"
        rating = -1
        genres = []

    rating = str(rating)

    #-------Lookup the last movie Id that has been given-------#

    with open("Movie.id", "r") as file:
        Last_id = file.read()
        Id = "M" + str(int(Last_id) + 1)
        print(Id)

    with open("Movie.id", "w") as file:
        file.write(str(int(Last_id)+1))



    #--------------Create folder / meta file for movie--------------#

    folderName = re.sub(r"[^\w\-]", "", Title.replace(" ", "")) #remove stupid shit from title 
    
    
    if os.path.isdir("../@media/movies/" +  folderName):
        with open("../@media/movies/" +  folderName + "/info.streamed", "r") as file:
            next(file)
            Original_Path = file.readline()[:-1]
        
        if Path == Original_Path:
            moviesSkipped += 1
            continue
        
        else:
            while os.path.isdir("../@media/movies/" +  folderName):
                folderName = folderName + "_copy"


    os.mkdir("../@media/movies/" + folderName) 


    with open(f"../@media/movies/{folderName}/info.streamed", "w") as file:
        file.write(Title + "\n")
        file.write(Path + "\n")
        file.write(Duration + "\n")
        file.write(Description + "\n")
        file.write(Id + "\n\n")

        file.write(Public + "\n")
        file.write(Uploader + "\n")
        file.write(rating + "\n")
        file.write(str(genres) + "\n")

        moviesAdded += 1
        
    #--------------try to download the cover of the movie------------------#

    if download_movie_thumbnail(Title, "../@media/movies/" + folderName + "/cover.jpg") == 1:
        print("downloaded cover image from imdb")
    else:
        print("failed to download cover image from imdb")

    print("")




#---------------------------------------------------------------------------#
#                                                                           #
#                             Make movies.js                                #
#                                                                           #
#---------------------------------------------------------------------------#


prepare_movieJS()

try:
    # Get all items in the directory
    for item in os.listdir("../@media/movies/"):
        # Construct the full path
        item_path = os.path.join("../@media/movies/", item)
        # Check if the item is a folder-
        if os.path.isdir(item_path):
            add_to_movieJS(item_path)
except PermissionError:
    print("You do not have permission to access this directory.")

close_movieJS()

print(f"Added {moviesAdded} Movies from {DIRECTORY}")
print(f"Skipped {moviesSkipped} Movies {DIRECTORY}")
print(f"Refreshed Information about {moviesRefreshed} Movies")