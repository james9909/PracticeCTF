from PIL import Image

WIDTH = 360
HEIGHT = 640
diff = Image.new("RGB", (WIDTH, HEIGHT), color=(255, 255, 255))
diff_pixels = diff.load()

for x in range(1, 607, 2):
    first = "images/image-%03d.png" % x
    second = "images/image-%03d.png" % (x+1)
    print first, second
    im1 = Image.open(first)
    im2 = Image.open(second)
    p1 = im1.load()
    p2 = im2.load()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if p1[x, y] != p2[x, y]:
                diff_pixels[x, y] = (0, 0, 0)

diff.save("diff.png")

"""
Watching the video reveals nothing immediately suspicious, so let's try analyzing the individual frames of the video.

We can get information about the avi file by running:
$ mplayer -vo null -ao null -frames 0 -identify kittycat.avi
...
ID_VIDEO_FORMAT=FFV1
ID_VIDEO_BITRATE=57118320
ID_VIDEO_WIDTH=360
ID_VIDEO_HEIGHT=640
ID_VIDEO_FPS=60.000
ID_VIDEO_ASPECT=0.0000
ID_START_TIME=0.00
ID_LENGTH=10.10
...

From this, we know that the video was recorded at 60 fps, and we can explode it into its individual frames
for further analysis.

$ mkdir images
$ ffmpeg -i kittycat.avi -r 60 -f image2 images/image-%03d.png

Scrolling through the images, it appears that every two frames are the same, but they actually differ by a few pixels
Drawing all the differences onto one image gives us the flag:

easyctf{$altY4_fL@gdUmp3R1no_Ripppp}
"""
