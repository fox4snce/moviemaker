import yaml
from planner import Planner
from voice_generator import VoiceGenerator
from image_generator import ImageGenerator
from sound_effects_generator import SoundEffectsGenerator
from movie_builder import MovieBuilder

def load_script(file_path):
    # Load the YAML script file and return the parsed data
    with open(file_path, 'r') as file:
        script_data = yaml.safe_load(file)
    return script_data

def main():
    # Load the input script
    script_file = 'path/to/script.yaml'
    script_data = load_script(script_file)

    # Initialize the Planner module
    planner = Planner()

    # Generate the video plan
    video_plan = planner.generate_video_plan(script_data)

    # Initialize the Voice module
    voice_generator = VoiceGenerator()

    # Generate voice audio for each dialogue line
    for scene in video_plan['scenes']:
        for dialogue in scene['dialogue']:
            character = dialogue['character']
            text = dialogue['text']
            voice_file = voice_generator.generate_voice(character, text)
            dialogue['voice_file'] = voice_file

    # Initialize the Image module
    image_generator = ImageGenerator()

    # Generate images for each scene
    for scene in video_plan['scenes']:
        scene_description = scene['description']
        image_file = image_generator.generate_image(scene_description)
        scene['image_file'] = image_file

    # Initialize the Sound Effects module
    sound_effects_generator = SoundEffectsGenerator()

    # Generate sound effects for each scene
    for scene in video_plan['scenes']:
        for sound_effect in scene['sound_effects']:
            sound_effect_name = sound_effect['name']
            sound_effect_file = sound_effects_generator.generate_sound_effect(sound_effect_name)
            sound_effect['file'] = sound_effect_file

    # Initialize the Movie Builder module
    movie_builder = MovieBuilder()

    # Build the final video
    output_video = movie_builder.build_movie(video_plan)

    # Save the output video
    output_path = 'path/to/output.mp4'
    movie_builder.save_video(output_video, output_path)

    print(f"Video generated successfully. Output saved to: {output_path}")

if __name__ == '__main__':
    main()