from pytube import YouTube
url="https://www.youtube.com/watch?v=gs6EIdfa1sU&t=2881s"
youtube_video=YouTube(url)
print("TITRE "+youtube_video.title)
print("Nombre de Vues: "+str(youtube_video.views))

#print("STREAMS")
#for stream in youtube_video.streams.fmt_streams:
 #   print(" ",stream)

stream=youtube_video.streams.get_by_itag(17)
print("Telechargement........")
stream.download()
print("OK")