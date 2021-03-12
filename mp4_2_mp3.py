from pytube import Playlist
from moviepy.editor import *

link = "https://www.youtube.com/playlist?list=PL1t2499m7R04t1FknkaI6G7STUF3FI3bt"
p = Playlist(link)
parent_dir = r"C:\Users\jackd\Desktop\Fuckery\mp4"
bad_chars = ['/', "\\", ':', '*', '?', '"', '<', '>', '|', "'", "."]

#Output type
download_status = True
gif_status = False
mp3_status = False
delete_original = False

for video in p.videos:
    print(f'Downloading: {video.title}')
    # print(video.streams.all())
    if download_status:
        print("downloading ig")
        video.streams.filter(res="1080p").first().download(parent_dir)
    trackName = video.title
    for i in bad_chars:
        trackName = trackName.replace(i, '')
    mp4_file = r'C:\Users\jackd\Desktop\Fuckery\mp4\%s.mp4' % trackName
    mp3_file = r'C:\Users\jackd\Desktop\Fuckery\mp3\%s.mp3' % trackName
    gif_file = r'C:\Users\jackd\Desktop\Fuckery\gif\%s.gif' % trackName
    print(trackName)
    our_video = VideoFileClip(mp4_file)
    our_audio = our_video.audio

    if gif_status:
        our_video.write_gif(gif_file)

    if mp3_status:
        our_audio.write_audiofile(mp3_file)

    our_audio.close()
    our_video.close()

    if delete_original:
        os.remove(r'C:\Users\jackd\Desktop\Fuckery\mp4\%s.mp4' % trackName)

