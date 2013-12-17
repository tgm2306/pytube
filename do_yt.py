
from pytube import YouTube

# not necessary, just for demo purposes
from pprint import pprint

yt = YouTube()

# Set the video URL.
yt.url = "http://www.youtube.com/watch?v=1pq7hzRPU_4"

# Once set, you can see all the codec and quality options YouTube has made
# available for the perticular video by printing videos.

pprint(yt.videos)

# get the smallest vesrion of mp4
vid = yt.filter('mp4')[0]
vid.download('/Users/toby/Desktop')





