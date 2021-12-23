
# pip install moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips

video_1 = VideoFileClip("test11.mp4")
video_2 = VideoFileClip("test11.mp4")
final_video= concatenate_videoclips([video_1, video_2])
#-- 비디오 갯수 상관없음
final_video.write_videofile("final_video.mp4")