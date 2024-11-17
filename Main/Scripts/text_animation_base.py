from moviepy.editor import TextClip, CompositeVideoClip
import numpy as np

# Dimensions de la vidéo
video_width, video_height = 1280, 720
duration = 3


# 1. Texte avec différentes tailles
titre = TextClip("Voici quelques options pour animer et styliser les textes avec Moviepy", fontsize=30, color='white').set_position(('center', 50)).set_duration(duration)
text_size = TextClip("Taille : Petit", fontsize=30, color='white').set_position(('center', 150)).set_duration(duration)
text_medium = TextClip("Taille : Moyen", fontsize=70, color='white').set_position(('center', 250)).set_duration(duration)
text_large = TextClip("Taille : Grand", fontsize=120, color='white').set_position(('center', 400)).set_duration(duration)

size_demo = CompositeVideoClip([titre, text_size, text_medium, text_large], size=(video_width, video_height)).set_duration(duration)

# 2. Texte avec différentes couleurs
text_red = TextClip("Rouge", fontsize=70, color='red').set_position(('center', 150)).set_duration(duration)
text_green = TextClip("Vert", fontsize=70, color='green').set_position(('center', 250)).set_duration(duration)
text_blue = TextClip("Bleu", fontsize=70, color='blue').set_position(('center', 350)).set_duration(duration)

color_demo = CompositeVideoClip([text_red, text_green, text_blue], size=(video_width, video_height)).set_duration(duration)

# 3. Texte animé (défilement horizontal)
def scroll_horizontal(t):
    return (video_width - t * 400, 'center')  # Le texte défile vers la gauche

scrolling_text = TextClip("Défilement horizontal", fontsize=70, color='white').set_duration(duration)
scroll_demo = scrolling_text.set_position(scroll_horizontal)

# 4. Texte animé (défilement vertical)
def scroll_vertical(t):
    return ('center', video_height - t * 400)  # Le texte défile vers le haut

scrolling_vertical_text = TextClip("Défilement vertical", fontsize=70, color='cyan').set_duration(duration)
vertical_scroll_demo = scrolling_vertical_text.set_position(scroll_vertical)

# 5. Texte animé (apparition en fondu)
fade_text = TextClip("Apparition en fondu", fontsize=70, color='magenta').set_position("center").fadein(3).set_duration(duration)

# Combiner les démonstrations
final_clip = CompositeVideoClip([
    CompositeVideoClip([size_demo]).set_start(0),
    CompositeVideoClip([color_demo]).set_start(duration),
    scroll_demo.set_start(duration * 2),
    vertical_scroll_demo.set_start(duration * 3),
    fade_text.set_start(duration * 4),
], size=(video_width, video_height)).set_duration(duration * 5) 


# Exporter la vidéo
final_clip.write_videofile("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/text_animation_base.mp4", fps=24)
