from flask import Flask,render_template, request,redirect,url_for
from generateVideo import *
from addAudio import *
import os
import sys

app = Flask(__name__ , static_folder="outputVideos")

@app.route('/generateVideoForm')
def generateVideoForm():
	return render_template('form.html')


@app.route('/generateVideo',methods = ['POST', 'GET'])
def generateVideo1():
	if request.method == 'POST':
		paragraph1 = []
		paragraph2 = []
		paragraphs = request.form['paragraphs']
		lines = paragraphs.splitlines()
		index = 0
		for i in range(len(lines)):
			if lines[i] != '':
				paragraph1.append(lines[i])
			else:
				index = i
				break			

		for i in range(index+1,len(lines)):
			paragraph2.append(lines[i])

		video = pickRandomVideo()
		audio , length , transitionSecound = pickRandomAudio()
	
		generateVideo(video,int(length),paragraph1,paragraph2,int(transitionSecound))
		addAudio(audio,paragraph1[0])

		return redirect(url_for('showVideo', videoName=paragraph1[0]))

	else:
		return redirect(url_for('generateVideoForm'))


@app.route('/showVideo/<string:videoName>')
def showVideo(videoName):
	return render_template('vodoe.html',videoName = videoName+".mp4",vid = videoName)


@app.route('/deleteVideo/<string:vid>')
def deleteVideo(vid):
	try:
		os.remove(app.root_path+"/outputVideos/"+vid+".mp4")
	except OSError as e:
		print(e, file=sys.stderr)
	
		return 'error'
	else:
		return redirect(url_for('generateVideoForm'))


if __name__ == '__main__':
    app.run(debug = True)