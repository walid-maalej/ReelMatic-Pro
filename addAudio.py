import moviepy.editor as mp
from os import walk
import random



AUDIO_FOLDER = "audio"
OUTPUT_FOLDER = "outputVideos"

def pickRandomAudio():
	filenames = next(walk(AUDIO_FOLDER), (None, None, []))[2]
	rndAudio = random.choice(filenames)
	transitionSecound = rndAudio.split('.')[0].split(' ')[-1]
	audio = mp.AudioFileClip(AUDIO_FOLDER+"/"+rndAudio)

	return audio,audio.duration,transitionSecound



def addAudio(audio,outputName):
	video1 = mp.VideoFileClip("generatedVideos/noAudio.mp4")
	final = video1.set_audio(audio)
	final.write_videofile(OUTPUT_FOLDER+"/"+str(outputName)+".mp4")
