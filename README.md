# text-to-voice-converter
Sure! Below is a template for the README file that you can include in your GitHub repository:

```
# Text-to-Voice Converter

This is a Python script that converts text to speech and allows users to modify the voice by gender, pitch, and tone. The script uses the `pyttsx3` library for text-to-speech conversion.

## Requirements

- Python 3.x
- `pyttsx3` library (install it using `pip install pyttsx3`)

## Usage

1. Clone the repository or download the `text_to_voice.py` file.

2. Install the required dependencies using the following command:
   ```
   pip install pyttsx3
   ```

3. Run the script:
   ```
   python text_to_voice.py
   ```

4. Follow the on-screen prompts to input the text, voice gender (male/female), desired tone (neutral, happy, sad, angry), pitch (50 to 200, default 150), rate (100 to 500, default 200), and the output file name (without extension).

5. The script will convert the input text to speech with the specified voice properties and save the output as a WAV audio file.

## Examples

1. Convert text to speech with default settings:
   ```
   Enter the text you want to convert to speech: Hello, how are you?
   Enter voice gender (male/female): male
   Enter the desired tone (neutral, happy, sad, angry): neutral
   Enter pitch (50 to 200, default 150): 
   Enter rate (100 to 500, default 200): 
   Enter the output file name (without extension): output
   Speech saved to "output.wav"
   ```

2. Convert text to speech with custom settings:
   ```
   Enter the text you want to convert to speech: I am feeling happy today!
   Enter voice gender (male/female): female
   Enter the desired tone (neutral, happy, sad, angry): happy
   Enter pitch (50 to 200, default 150): 180
   Enter rate (100 to 500, default 200): 250
   Enter the output file name (without extension): happy_output
   Speech saved to "happy_output.wav"
   ```

## Notes

- The script uses `pyttsx3` for text-to-speech conversion, and the available voices may vary depending on your operating system and the TTS engine used by `pyttsx3`.

- The script saves the output as a WAV audio file. If you need the output in a different format (e.g., MP3), you can use other libraries like `pydub` to convert the generated WAV file to your desired format.

- Experiment with different tones and voice properties to create various speech outputs.

## License

This project is licensed under the [MIT License](LICENSE).
```
