import pyttsx3

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
# # Example usage
# text_to_speech("Hello, I'm Meenakshi.")

if __name__ == '__main__':
    print("\nwelcome to robo speaker 1.0 || Created by Meenakshi Panchal ")
    while True:
        pyttsx3.speak("enter something please which you want I should say")

        text = input("enter you name please: ")
        if(text == 'w'):
            pyttsx3.speak("bye my friend! Have a good day and enjoy your day!")
            break
        else:
            pyttsx3.speak(text)
        # pyttsx3.speak(name)



