#1.Importation des vidéos

from moviepy.editor import *

fond_noir = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/fond_noir.mp4").subclip(5,20)
#code_flouté_intro = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4").rotate(180)
#librairie_1 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#texte_2 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#texte_anim_3 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#video_anim_4 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#video_anim_5 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#video_anim_6 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#video_anim_7 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")
#video_anim_8 = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/video_1_chaussure.mp4")


#Ajout titre sur le fond noir
titre_intro = (TextClip("MON 2.1 : Automatisation de montages vidéos avec python", 
                        fontsize=70, color='white', 
                        size=(fond_noir.w - 100, None))  
             .set_position("center")
             .set_start(5)
             .set_duration(5)
             .crossfadein(1.5)   
             .crossfadeout(1.5))

sous_titre_intro = (TextClip("Baptiste Audouin", 
                            fontsize=70, color='white')
            .set_position(("center", 6 * fond_noir.h/10))
            .set_start(7)
            .set_duration(3)
            .crossfadein(1.5)   
            .crossfadeout(1.5))

#Ajout du titre
intro = CompositeVideoClip([fond_noir, titre_intro, sous_titre_intro]).subclip(3,13) 
intro.write_videofile("intro.mp4",fps=25)