from moviepy.editor import ColorClip, TextClip, CompositeVideoClip, concatenate_videoclips
from moviepy.video.fx.all import fadein
from moviepy.editor import *

# Dimensions de la vidéo
width, height = 720, 480

# --- Générer les vidéos colorées ---
video1 = ColorClip(size=(width, height), color=(255, 0, 0), duration=5)
video2 = ColorClip(size=(width, height), color=(0, 0, 255), duration=5)
video3 = ColorClip(size=(width, height), color=(0, 255, 0), duration=5)

# --- Animation 1 : Slide-in ---
def slide_in(get_frame, t):
    frame = get_frame(t)
    dx = width * (1 - min(t / 2, 1))  # Se déplace de droite à gauche en 2s
    return frame[:, int(dx):]

video1_animated = video1.fl(slide_in)

# --- Animation 2 : Fade-in ---
video3_animated = fadein(video3, 2)  # Opacité croissante sur 2s

# --- Animation 3 : Slide-in pour video2 ---
def slide_in_video2(get_frame, t):
    frame = get_frame(t)
    dx = width * (1 - min(t / 2, 1))  # Se déplace de droite à gauche en 2s
    return frame[:, int(dx):]

video2_animated = video2.fl(slide_in_video2)

# --- Page "THE END" ---
end_text = (TextClip("THE END", fontsize=100, color="white", font="Arial", size=(width, height))
            .set_duration(2))

end_background = ColorClip(size=(width, height), color=(0, 0, 0), duration=2)
end_clip = CompositeVideoClip([end_background, end_text.set_pos("center")])

# --- Vérification des durées ---
print(f"video1 duration: {video1_animated.duration}")
print(f"video2 duration: {video2_animated.duration}")
print(f"video3 duration: {video3_animated.duration}")
print(f"end_clip duration: {end_clip.duration}")

# --- Séquence finale ---
final_clip = concatenate_videoclips([
    video1_animated,
    video2_animated,  # Vidéo 2 avec animation
    video3_animated,
    end_clip
])

# Exporter la vidéo
final_clip.write_videofile("/Users/baptisteaudouin/Documents/GitHub/MON.2.1/Main/Montages/output_final.mp4", fps=24)
