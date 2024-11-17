# Bibliothèque

from moviepy.editor import *

# Chargement de la video

fond_noir = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/fond_noir.mp4").subclip(5,20)

#Ajout titres
 
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


# Ajout sommaire

sommaire_text = TextClip("""
Sommaire :
    
    1. Intégration de textes
    
    2. Animation des textes
    
    3. Animations de vidéos
""", fontsize=70, color='white', size=(1280 - 200, None), align="West")

def scrolling_position(t):
    return ("center", 720 + sommaire_text.h - (t * 200)) 

# Ajouter l'animation
sommaire_clip = sommaire_text.set_position(scrolling_position).set_duration(10).set_start(10)

# Compilation
intro = CompositeVideoClip([fond_noir, titre_intro, sous_titre_intro, sommaire_clip]).subclip(3,20) 

# Export
intro.write_videofile("intro.mp4", fps=24)