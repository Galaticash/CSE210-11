import os
import pathlib
import pyray

DEFAULT_DIRECTORY = "assets\\sounds\\"

class Audio_Service():
    """
        A service that loads and plays sounds
    """
    def __init__(self):
        self._sounds = {}
        pyray.init_audio_device()

    def load_sounds(self, directory):
        """
            Loads all sounds in the sound folder to a sounds dictionary.
        """
        filepaths = self._get_filepaths(directory, [".wav", ".mp3", ".wma", ".aac"])
        for filepath in filepaths:
            if filepath not in self._sounds.keys():
                sound = pyray.load_sound(filepath)
                self._sounds[filepath] = sound
        self.adjust_volume()

    def adjust_volume(self):
        try:
            crab_rave = self._sounds["assets\\sounds\\crab_rave.mp3"]
            pyray.set_sound_volume(crab_rave, .4)

            start_sound = self._sounds["assets\\sounds\\start.wav"]
            pyray.set_sound_volume(start_sound, .6)

            bap_sound = self._sounds["assets\\sounds\\boing.wav"]
            pyray.set_sound_volume(bap_sound, .6)
        except KeyError:
            print("Invalid Key")
        except:
            print("An error has occurred while trying to Ajust volumes")


    def unload_sounds(self):
        """
            Unloads the audio files/sounds from memory.
            Will also close the audio stream
        """
        for sound in self._sounds.values():
            pyray.unload_sound(sound)
        self._sounds.clear()
        pyray.close_audio_device()
    
    def _get_filepaths(self, directory, filter):
        """
            Gets all the filepaths for each sound in the assets folder
            Edited to also find items within sub folders
        """
        filepaths = []
        files = os.listdir(directory)
        for file in files:
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
            # If there is a sub_folder
            elif extension == "":
                # Rename, know it is NOT a singular file
                folder = file
                # Wont load files from folder named NotLoaded
                if not(folder == "NotLoaded"):
                    sub_directory = directory + "\\" + folder
                    sub_files = os.listdir(sub_directory)
                    # Add all files within it to the files to look over
                    for sub_file in sub_files:            
                        files.append(folder + "\\" + sub_file)
        return filepaths

    def is_sound_playing(self, sound_obj):
        sound = self._get_sound(sound_obj)
        # TODO: Add if statement to prevent it from checking an invalid sound
        return pyray.is_sound_playing(sound)

    def num_sounds_playing(self):
        return pyray.get_sounds_playing()

    def _get_sound(self, sound_obj):
        """
            Returns the pyray sound from the given sound_obj.
        """
        filename = sound_obj.get_filename()
        # fix to be from assets\\sounds\\
        filepath = str(DEFAULT_DIRECTORY + filename)
        try:
            # Try getting the sound from _sounds dictionary using the filepath
            sound = self._sounds[filepath]
            # Volume as a value betwen 0 and 1.0
            volume = sound_obj.get_volume()
            # pyray.set_sound_volume(sound, volume)
        except KeyError:
            print(f"Invalid sound filepath: {filepath}")
            return
        except:
            print("An unexpected error occured in Audio Service.")
            return
        return sound

    def play_sound(self, sound_obj):
        sound = self._get_sound(sound_obj)
        # TODO: Add if statement to prevent it from playing an invalid sound
        pyray.play_sound(sound)
        #pyray.play_sound_multi(sound) ERROR: Too many sounds of the same kind LOL

    def stop_sound(self, sound_obj):        
        sound = self._get_sound(sound_obj)
        # TODO: Add if statement to prevent it from using an invalid sound
        if pyray.is_sound_playing(sound):
            pyray.stop_sound(sound)

    def loop_sound(self, sound_obj):
        filename = sound_obj.get_filename()
        # fix to be from assets\\sounds\\
        filepath = str(DEFAULT_DIRECTORY + filename)
        try:
            sound = self._sounds[filepath]            
            # Volume as a value betwen 0 and 1.0
        except KeyError:
            print(f"Invalid sound filepath: {filepath}")
            return


            pyray.play_sound(sound)

        # ERROR: Program will be stuck here, no GUI updates or anything L
        # while True:
        #    if not pyray.is_sound_playing(sound):
        #        pyray.play_sound(sound)