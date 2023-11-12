from generateVideo import *
from addAudio import *
import csv


video = pickRandomVideo()
audio , length , transitionSecound = pickRandomAudio()

paragraph1 = []
paragraph2 = []

with open("quote.txt", 'r', encoding = 'utf-8') as f:
	lines = f.read().splitlines()
	index = 0
	for i in range(len(lines)):
		if lines[i] != '':
			paragraph1.append(lines[i])
		else:
			index = i
			break			

	for i in range(index+1,len(lines)):
		paragraph2.append(lines[i])
	

f.close()
generateVideo(video,int(length),paragraph1,paragraph2,int(transitionSecound))
addAudio(audio,paragraph1[0])



