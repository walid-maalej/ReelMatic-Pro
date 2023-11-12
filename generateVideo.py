import cv2
from backgroundvideos import *
import imutils
from ffpyplayer.player import MediaPlayer

def generateVideo(video,videoLength,paragraph1,paragraph2,transitionSecound):
	

	FPS = int(video.get(cv2.CAP_PROP_FPS))
	FRAMEWIDTH = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
	FRAMEHEIGHT = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
	FRAME_COUNT = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
	VIDEO_LENGTH = videoLength
	OUTPUT_FPS = int(FRAME_COUNT/VIDEO_LENGTH)
	OUTPUT_PATH = "generatedVideos/"

	# PARAGRAPH POSITION
	STARTHEIGHT = random.randint(int(FRAMEHEIGHT*0.3), int(FRAMEHEIGHT*0.7))
	STARTWIDTH = int(FRAMEWIDTH *0.1)






	out = cv2.VideoWriter(OUTPUT_PATH+'noAudio.mp4', cv2.VideoWriter_fourcc(*"mp4v"), OUTPUT_FPS , (FRAMEWIDTH,FRAMEHEIGHT))






	def addText(cv2,text,font,lineNumber):
		textsize = cv2.getTextSize(text, font, 1.7, 2)[0]
		cv2.putText(frame,
	                text, 
	                (STARTWIDTH , STARTHEIGHT + (lineNumber)*textsize[1]) , 
					font, 1, 
					(255, 255, 255), 
					1, 
					cv2.LINE_AA)



	def addParagraph(video,cv2,font,paragraph,start_finish):
		if video.get(cv2.CAP_PROP_POS_FRAMES) > OUTPUT_FPS* start_finish[0] and video.get(cv2.CAP_PROP_POS_FRAMES) < OUTPUT_FPS * start_finish[1] :
			for i in range(len(paragraph)):
				addText(cv2,paragraph[i],font,i)
			


	while(video.isOpened()):

		ret, frame = video.read()	#READ VIDEO FRAMES
	#	audio_frame, val = player.get_frame()	#READ AUDIO FRAMES

		if ret == True :
			frame = imutils.resize(frame, width = FRAMEWIDTH, height = FRAMEHEIGHT)


			start_finish = (0,transitionSecound)
			addParagraph(video,cv2,cv2.FONT_HERSHEY_COMPLEX_SMALL,paragraph1,start_finish)

			start_finish = (transitionSecound,videoLength)
			addParagraph(video,cv2,cv2.FONT_HERSHEY_COMPLEX_SMALL,paragraph2,start_finish)
			

			out.write(frame)

			cv2.imshow('generatedVideo',frame)

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		else:
			break



	out.release()
	video.release()
	cv2.destroyAllWindows()




