from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, concatenate_audioclips


# Placeholder paths for images and music files
image_path_1 = 'images\\averyoriginal.png'
image_path_2 = 'images\\2.png'
music_path_1 = 'music\\happy_light_loop.ogg'
music_path_2 = 'music\\loop1.ogg'

# Duration of each image in the video
image_duration = 15  # 15 seconds for each image

# Create video clips from images
clip1 = ImageClip(image_path_1, duration=image_duration)
clip2 = ImageClip(image_path_2, duration=image_duration)

# Concatenate the two image clips
final_clip = concatenate_videoclips([clip1, clip2])

# Add music to the video
music1 = AudioFileClip(music_path_1).subclip(0, image_duration)
music2 = AudioFileClip(music_path_2).subclip(0, image_duration)
final_music = concatenate_audioclips([music1, music2])

# Setting the audio of the concatenated video
final_clip = final_clip.set_audio(final_music)

# Specify the output file path
output_path = 'output_video.mp4'

# Write the final video file
final_clip.write_videofile(output_path, fps=24)  # fps can be adjusted as needed

# This is a basic script. It can be enhanced with more features like transitions, effects, etc