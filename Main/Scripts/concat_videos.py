from moviepy.editor import *

intro = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/intro.mp4")
text_animation_base = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/text_animation_base.mp4")
text_animation_avance = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/text_animation_avance.mp4")


# Concaténer les vidéos
final_clip = concatenate_videoclips([intro, text_animation_base, text_animation_avance])

# Sauvegarder la vidéo finale
final_clip.write_videofile('/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/final_video.mp4', codec='libx264')