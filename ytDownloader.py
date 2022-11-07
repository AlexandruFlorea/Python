from pytube import YouTube
from sys import argv

# we take the link from the command prompt and download the video
# link = argv[1]
link = input("Paste the link to the video: ")
# argv takes all the things you input in the command line while running this program
# the first item is always the program name, while argv[1] take the first argument we input (the link)
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('./')
