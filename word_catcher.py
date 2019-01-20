import sys
from os import listdir
import os
import pysrt
from moviepy.editor import VideoFileClip as vfc 
from moviepy.editor import concatenate_videoclips

def generate_video(video_file, sub_file):
	print("----------------------------------")
	print("| Searching in movie " + video_file)
	one_second = pysrt.SubRipTime.from_string('00:00:01,000')
	videoclip = vfc(video_file)
	sub = pysrt.open(sub_file)

	final_clip = videoclip.subclip('00:00:00','00:00:00')

	counter = 0
	for x in sub:
		if word in x.text.lower():
			counter+=1
			print("----")
			print('| found something === ' + str(counter))
			print('| ' + x.text)
			start = x.start - one_second 
			end = x.end + one_second
			clip = videoclip.subclip(str(start), str(end))
			final_clip = concatenate_videoclips([final_clip, clip])
	print("++++++++++++++++++++++++++")
	print("")
	## FOR DEBUGGING PURPOSES TO SEE THE VIDEO QUALITY OF EACH CLIP
	# final_clip.write_videofile(output_folder + video_file + "__" + word + ".mp4", write_logfile=True)
	if counter > 0:
		return final_clip
	else:
		return None


word = sys.argv[1]
output_folder = "output/"
input_folder = "input/"
files = listdir(input_folder)
clips = []

for video_file in files:
	if video_file[-4:len(video_file)] in [".mp4"]:
		video_file = input_folder + video_file
		sub_file   = video_file[0:len(video_file)-4] + ".srt"
		print(" analyzing video : " + video_file + " srt:" + sub_file)
		movie_clip = generate_video(os.path.abspath(video_file),os.path.abspath(sub_file))
		if movie_clip:
			# print(" appending generated clip from movie " + video_file + " to the final movie")
			clips.append(movie_clip)

if len(clips) > 0:
	final_movie = concatenate_videoclips(clips,method='compose')
	final_movie.write_videofile(output_folder + word + ".mp4")

