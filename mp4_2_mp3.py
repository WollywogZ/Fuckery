from pytube import Playlist
from moviepy.editor import *

#CTGP Link: https://www.youtube.com/watch?v=vanomujXJ-4&list=PL1t2499m7R04t1FknkaI6G7STUF3FI3bt

link = "https://www.youtube.com/playlist?list=PL1t2499m7R04t1FknkaI6G7STUF3FI3bt"
p = Playlist(link)
parent_dir = r"C:\Users\jackd\Desktop\Fuckery\mp4"
bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", "."]

for video in p.videos:
    print("1.1")
    print(f'Downloading: {video.title}')
    video.streams.filter().first().download(parent_dir)
    trackName = video.title
    for i in bad_chars:
        trackName = trackName.replace(i, '')
    mp4_file = r'C:\Users\jackd\Desktop\Fuckery\mp4\%s.mp4' % trackName
    mp3_file = r'C:\Users\jackd\Desktop\Fuckery\mp3\%s.mp3' % trackName
    print(trackName)
    our_video = VideoFileClip(mp4_file)
    our_audio = our_video.audio
    our_audio.write_audiofile(mp3_file)
    our_audio.close()
    our_video.close()
    os.remove(r'C:\Users\jackd\Desktop\Fuckery\mp4\%s.mp4' % trackName)
