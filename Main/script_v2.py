from moviepy.editor import *

# Charger le clip vidéo principal
clip = VideoFileClip("code_recording.mp4").subclip(0, 10)  # Utilise les 10 premières secondes de la vidéo

# 1. Introduction avec un titre simple (5-10 secondes)
intro_text = (TextClip("Introduction à MoviePy", fontsize=70, color='white')
              .set_position("center")
              .set_duration(2)
              .crossfadein(0.5)
              .crossfadeout(0.5))

# 2. Ajout de texte animé (15 secondes)
text_clip = (TextClip("Ajout de texte et effets", fontsize=50, color='white')
             .set_position(lambda t: ('center', 500 - t * 100))  # Animation de montée
             .set_start(3)  # Démarre à 3 secondes
             .set_duration(2)
             .crossfadein(0.5)
             .crossfadeout(0.5))

# 3. Effet de transition et animation (15 secondes)
effect_text = (TextClip("Effet de transition et rotation", fontsize=50, color='yellow')
               .set_position("center")
               .set_start(6)
               .set_duration(2)
               .rotate(lambda t: t * 45)  # Rotation continue
               .crossfadein(0.5)
               .crossfadeout(0.5))

# 4. Ajout de musique (10 secondes)
# Charger un fichier audio et ajouter un fondu d'entrée et de sortie
#audio = AudioFileClip("musique.mp3").subclip(0, clip.duration).audio_fadein(1).audio_fadeout(1)
#clip = clip.set_audio(audio)

# 5. Conclusion et exportation (5-10 secondes)
conclusion_text = (TextClip("MoviePy - Montage Vidéo en Python", fontsize=70, color='lightblue')
                   .set_position("center")
                   .set_start(9)
                   .set_duration(2)
                   .crossfadein(0.5)
                   .crossfadeout(0.5))

# Combiner les clips texte avec le clip principal
final_video = CompositeVideoClip([clip, intro_text, text_clip, effect_text, conclusion_text])

# Exporter la vidéo finale
final_video.write_videofile("demo_moviepy.mp4", fps=24)
