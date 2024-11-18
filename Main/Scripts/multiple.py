from moviepy.editor import VideoFileClip, clips_array, vfx
clip1 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/code.mp4").subclip(0,10) # add 10px contour
clip2 = clip1.fx( vfx.mirror_x)
clip3 = clip1.fx( vfx.mirror_y)
clip4 = clip2.fx( vfx.mirror_y)

final_clip = clips_array([[clip1,clip2],
                          [clip3,clip4]])

final_clip.write_videofile("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/multiple.mp4")