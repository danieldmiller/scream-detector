#!/usr/local/bin/python2
from sys import argv
import numpy as np
import subprocess
import pyaudio
import wave
import random
import time

from pyAudioAnalysis import audioTrainTest as aT
isSignificant = 0.8 #try different values.

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file" + str(time.time()) + ".wav"

audio = pyaudio.PyAudio()

#start recording
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("recording..")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)
print("finished recording")

#stop recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# P: list of probabilities
Result, P, classNames = aT.fileClassification(WAVE_OUTPUT_FILENAME, "svmModel", "svm")
#winner = np.argmax(P) #pick the result with the highest probability value.

print("scream levels: " + str(P[0]))

# is the highest value found above the isSignificant threshhold? 
if P[0] > isSignificant :
	#execute bash command like "python3 send_sms.py [matchRate (0-1)]
	subprocess.call(["python3", "send_sms.py", str(P[0])])

	print("File: " +WAVE_OUTPUT_FILENAME + " is in category: " + classNames[0] + ", with probability: " + str(P[0]))
else:
	print("Can't classify sound: " + str(P))
