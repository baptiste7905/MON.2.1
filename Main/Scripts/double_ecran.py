from moviepy.editor import *
from PIL import Image
Image.Resampling = Image.Resampling.LANCZOS  



intro = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/intro.mp4", audio=False).\
               subclip(0,15)

code = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/intro_code.mp4", audio=False).\
               margin(6, color=(255,255,255)).\
               margin(bottom=20, right=20, opacity=0).\
               set_pos('bottom')  

txt = (TextClip("Double écrans : vidéo intro avec le code correspondant",
	               color='yellow',fontsize=60)
                   .set_position(("center", 2 * code.h/10)))

final = CompositeVideoClip([intro,code,txt])
final.subclip(0,10).write_videofile("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/double_ecran.mp4",fps=24,codec='libx264')