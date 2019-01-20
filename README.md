This is a small project to help a friend learn English. 

The goal was to collect a few favorite movies of a person along with their subtitles. A person can specify a word (or phrase) to search in the subtitles and then the script will cut out these scenes and generate a short video which contains the scenes with the searched word. 

installation 
run python3.6 setup.py install

this will install pysrt and moviepy

how to use: 
python word_catcher "the search word"

Output of the script - a video file will be placed in the *output/* folder in the same location as the script. 

All the input files (movies and their subs) should be located in the *input/* folder.
All the movies should have naming format: 
movie_name.mp4
The subtitle file should have the same name as the movie file but with .srt ending:
movie_name.srt


Possible implementations:

1. Telegram bot which will spit out a small video clip with the searched word

2. Add some features like maximum length of the clip (should not be longer than 20 seconds)
2.1 Maybe possibility to specify movie by name of movie set by genre.