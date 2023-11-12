from os import walk
import random
import cv2
from ffpyplayer.player import MediaPlayer


BACKGROUNDVIDEOS_FOLDER = "backgroundvideos"


def pickRandomVideo():
	filenames = next(walk(BACKGROUNDVIDEOS_FOLDER), (None, None, []))[2]
	bgVid = random.choice(filenames)
	cap = cv2.VideoCapture(BACKGROUNDVIDEOS_FOLDER+'/'+bgVid)
	return cap
