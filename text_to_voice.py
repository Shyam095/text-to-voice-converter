import pyttsx3

def save_to_file(text, output_file, gender='female', tone='neutral', pitch=150, rate=200):
    engine = pyttsx3.init()

    # Set voice properties
    voices = engine.getProperty('voices')
    if gender == 'male':
        engine.setProperty('voice', voices[0].id)  # Index 0 for male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Index 1 for female voice

    # Set pitch and rate
    engine.setProperty('pitch', pitch / 100)  # Pitch is in the range 0 to 2
    engine.setProperty('rate', rate)  # Rate is the speed of speech (words per minute)

    # Apply tone variation based on user's choice
    if tone == 'happy':
        engine.setProperty('pitch', pitch * 2.0)
    elif tone == 'sad':
        engine.setProperty('pitch', pitch * 0.2)
    elif tone == 'angry':
        engine.setProperty('pitch', pitch * 4.0)

    # Speak the text and save it to a WAV file
    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    gender = input("Enter voice gender (male/female): ").lower()
    tone = input("Enter the desired tone (neutral, happy, sad, angry): ").lower()
    pitch = int(input("Enter pitch (50 to 200, default 150): ") or 150)
    rate = int(input("Enter rate (100 to 500, default 200): ") or 200)
    output_file = input("Enter the output file name (without extension): ") + ".wav"

    save_to_file(text, output_file, gender=gender, tone=tone, pitch=pitch, rate=rate)
    print(f'Speech saved to "{output_file}"')
