from moviepy.editor import *
from PIL import Image
Image.Resampling = Image.Resampling.LANCZOS  # Remplace ANTIALIAS

# UKULELE CLIP, OBTAINED BY CUTTING AND CROPPING
# RAW FOOTAGE

intro = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/intro.mp4", audio=False).\
               subclip(0,15)

w,h = moviesize = intro.size

# THE PIANO FOOTAGE IS DOWNSIZED, HAS A WHITE MARGIN, IS
# IN THE BOTTOM RIGHT CORNER 

from moviepy.editor import VideoFileClip

# Charger le clip "intro"
code = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/intro.mp4", audio=False).\
               subclip(0,15).\
               crop(0, 0, 72*5, 48*5).\
               margin(6, color=(255,255,255)).\
               margin(bottom=20, right=20, opacity=0).\
               set_pos(('right', 'bottom'))  # Placer à droite en bas



# A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

txt = TextClip("double écran", font='Amiri-regular',
	               color='white',fontsize=24)

txt_col = txt.on_color(size=(intro.w + txt.w,txt.h-10),
                  color=(0,0,0), pos=(6,'center'), col_opacity=0.6)




# FINAL ASSEMBLY
final = CompositeVideoClip([intro,code])
final.subclip(0,10).write_videofile("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/double_ecran.mp4",fps=24,codec='libx264')