#1.Importation de la vidéo

from moviepy.editor import *

clip = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
clip180 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4").rotate(180)
clip180.ipython_display(width=280) #fais une rotation de 180 degres

#Definition d'un titre
txt_clip = (TextClip("Partie 1", fontsize=70, color='white')
            .set_position("center")
            .set_start(5)
            .set_duration(2)
            .crossfadein(0.5)   # Fondu en entrée de 0.5 seconde
            .crossfadeout(0.5)) # Fondu en sortie de 0.5 seconde


#Ajout du titre
result = CompositeVideoClip([clip, txt_clip]) 
result.write_videofile("comment_video.mp4",fps=25)