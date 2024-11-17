from moviepy.editor import TextClip, CompositeVideoClip
import numpy as np

# Dimensions de la vidéo
video_width, video_height = 1280, 720
duration = 3  # Durée de chaque démonstration


# 1. Texte avec différentes tailles
titre = TextClip("Voici quelques options pour animer, styliser les textes avec Moviepy", fontsize=30, color='white').set_position(('center', 50)).set_duration(duration)
text_size = TextClip("Taille : Petit", fontsize=30, color='white').set_position(('center', 150)).set_duration(duration)
text_medium = TextClip("Taille : Moyen", fontsize=70, color='white').set_position(('center', 250)).set_duration(duration)
text_large = TextClip("Taille : Grand", fontsize=120, color='white').set_position(('center', 400)).set_duration(duration)

size_demo = CompositeVideoClip([titre, text_size, text_medium, text_large], size=(video_width, video_height)).set_duration(duration)

# 2. Texte avec différentes couleurs
text_red = TextClip("Rouge", fontsize=70, color='red').set_position((200, 150)).set_duration(duration)
text_green = TextClip("Vert", fontsize=70, color='green').set_position((200, 250)).set_duration(duration)
text_blue = TextClip("Bleu", fontsize=70, color='blue').set_position((200, 350)).set_duration(duration)

color_demo = CompositeVideoClip([text_red, text_green, text_blue], size=(video_width, video_height)).set_duration(duration)

# 3. Texte animé (défilement horizontal)
def scroll_horizontal(t):
    return (video_width - t * 300, 'center')  # Le texte défile vers la gauche

scrolling_text = TextClip("Défilement horizontal", fontsize=70, color='white').set_duration(duration)
scroll_demo = scrolling_text.set_position(scroll_horizontal)

# 4. Texte animé (défilement vertical)
def scroll_vertical(t):
    return ('center', video_height - t * 200)  # Le texte défile vers le haut

scrolling_vertical_text = TextClip("Défilement vertical", fontsize=70, color='cyan').set_duration(duration)
vertical_scroll_demo = scrolling_vertical_text.set_position(scroll_vertical)

# 5. Texte animé (apparition en fondu)
fade_text = TextClip("Apparition en fondu", fontsize=70, color='magenta').set_position("center").fadein(2).set_duration(duration)

# 6. Texte avec rotation (rotation fluide)
def rotate_text(t):
    return 30 * np.sin(t * np.pi)  # Faire tourner le texte de manière fluide

rotated_text = TextClip("Rotation", fontsize=70, color='yellow').set_position("center").set_duration(duration).fl_time(rotate_text)

# 7. Texte avec changement de couleur
def change_color(t):
    if t < 1:
        return 'red'
    elif t < 2:
        return 'green'
    else:
        return 'blue'

color_changing_text = TextClip("Changement de couleur", fontsize=70, color='white').set_position("center").set_duration(duration).fl_time(change_color)

# 8. Texte avec zoom
zoom_text = TextClip("Zoom", fontsize=70, color='purple').set_position("center").resize(lambda t: 1 + 0.5 * t).set_duration(duration)

# 9. Texte avec effet de flash (modification de l'opacité)
def flash_effect(t):
    return 1 if t % 0.5 < 0.25 else 0  # Flash toutes les 0.5 secondes

flash_text = TextClip("Flash", fontsize=70, color='white').set_position("center").set_duration(duration).fl_time(flash_effect)

# 10. Texte avec effet de rebond (mouvement sinusoïdal)
def bounce(t):
    y_pos = 200 + 50 * np.sin(2 * np.pi * t / duration)  # Oscillation sinusoïdale pour un effet de rebond
    return ('center', y_pos)

bouncing_text = TextClip("Rebond", fontsize=70, color='pink').set_position("center").set_duration(duration).fl_time(bounce)

# Combiner les démonstrations
final_clip = CompositeVideoClip([
    CompositeVideoClip([size_demo]).set_start(0),
    CompositeVideoClip([color_demo]).set_start(duration),
    scroll_demo.set_start(duration * 2),
    vertical_scroll_demo.set_start(duration * 3),
    fade_text.set_start(duration * 4),
    rotated_text.set_start(duration * 5),
    color_changing_text.set_start(duration * 6),
    zoom_text.set_start(duration * 7),
    flash_text.set_start(duration * 8),
    bouncing_text.set_start(duration * 9),
], size=(video_width, video_height)).set_duration(duration * 10)


# Exporter la vidéo
final_clip.write_videofile("text_demo_with_animations_corrected.mp4", fps=24)
