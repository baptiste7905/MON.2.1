from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import numpy as np

# Charger la vidéo de fond
video_path = "fond_noir.mp4"
video_clip = VideoFileClip("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Videos/fond_noir.mp4")

# Dimensions de la vidéo (s'assurer que la taille de la vidéo correspond à celle de la vidéo de fond)
video_width, video_height = video_clip.size
duration = video_clip.duration  # Utiliser la durée de la vidéo de fond

# 1. Texte avec rotation fluide
def rotate_text(t):
    # Appliquer une rotation fluide en fonction du temps
    return 30 * np.sin(t * np.pi)  # Rotation fluide

rotated_text = TextClip("Rotation", fontsize=70, color='yellow').set_position("center").set_duration(duration)
rotated_text = rotated_text.fl_time(rotate_text)  # Utilisation de fl_time pour appliquer la rotation fluide

# 2. Texte avec effet de flash (modification de l'opacité)
def flash_effect(t):
    # Appliquer l'effet flash (changer l'opacité toutes les 0.5 secondes)
    return 1 if t % 0.5 < 0.25 else 0

flash_text = TextClip("Flash", fontsize=70, color='white').set_position("center").set_duration(duration)
flash_text = flash_text.fl_time(flash_effect)  # Utilisation de fl_time pour l'effet flash

# 3. Texte avec effet de rebond (mouvement sinusoïdal)
def bounce(t):
    # Mouvement sinusoïdal pour un effet de rebond
    y_pos = 200 + 50 * np.sin(2 * np.pi * t / duration)  # Oscillation verticale
    return ('center', y_pos)

bouncing_text = TextClip("Rebond", fontsize=70, color='pink').set_position("center").set_duration(duration)
bouncing_text = bouncing_text.fl_time(bounce)  # Utilisation de fl_time pour l'effet rebond

# Combiner la vidéo de fond avec les textes animés
final_clip = CompositeVideoClip([
    video_clip,  # Ajouter la vidéo de fond
    rotated_text.set_start(0),
    flash_text.set_start(0),
    bouncing_text.set_start(0),
], size=(video_width, video_height)).set_duration(duration)

# Exporter la vidéo finale avec les animations
final_clip.write_videofile("video_with_animations.mp4", fps=24)
