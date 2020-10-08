from pygame import mixer

mixer.init()
mixer.music.load("Song_path.mp3")
mixer.music.play()

while True:# infinite loop
    print("Press \nP to Pause\nR to Resume\nE to exit the program")
    user_input_query = input(" ")

    if user_input_query == 'P':
        mixer.music.pause()
    elif user_input_query == 'R':
        mixer.music.unpause()
    elif user_input_query == 'E':
        mixer.music.stop()
        break
