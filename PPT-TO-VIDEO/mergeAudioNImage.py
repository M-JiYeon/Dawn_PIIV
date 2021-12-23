# pip install moviepy

from moviepy.editor import *

# 동영상 생성할 때 duration을 오디오 파일과 동일하게 설정

audio = AudioFileClip("./합성결과/testAudio.wav")

video = ImageClip('./test/슬라이드1.jpg',duration=audio.duration)
video = video.set_audio(audio)
video.write_videofile("test11.mp4",fps=24, codec="mpeg4")

# duration=AudioFileClip(file).duration