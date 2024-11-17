# text rotation using moviepy
import moviepy.editor as mped
import numpy as np

colour_clip = mped.ColorClip(size=[300, 200], color=np.array([250, 90, 0]).astype(np.uint8), duration=10).set_position((0, 0))
txtClip = mped.TextClip('Text', color="#4a4a4a", size=[200,100]).set_position((0,0)).set_duration(1)
txtClip = txtClip.add_mask().rotate(45, unit='deg', expand=True)
stacked_clips = mped.CompositeVideoClip([colour_clip, txtClip]).set_duration(10)
stacked_clips.write_videofile('text_rotated_with_mask_applied_to_rotation.mp4', fps=5)