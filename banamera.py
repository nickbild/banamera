from picamera2 import Picamera2
import time
import os
import RPi.GPIO as GPIO
import google.genai as genai
from google.genai import types
from PIL import Image
from io import BytesIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

client = genai.Client(api_key=os.getenv('GENAIAPI'))

picam2 = Picamera2()
config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(config)

picam2.start()
time.sleep(2)


def capture_image():
    picam2.capture_file("image.jpg")

    return


def record_request():
    print("Recording...")
    os.system("arecord -d 2 -D plughw:0 -c1 -r 48000 -f S32_LE -t wav -V mono -v request.wav")

    return


def transcribe_request():
    wav_file = client.files.upload(file="request.wav", config={"mimeType": "audio/wav"})
    prompt = "Give me a transcript of the speech in the attached file. Only provide the transcript text in your response."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[prompt, wav_file],
    )

    return response.text


def modify_image(prompt):
    image = Image.open("image.jpg")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, image],
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            image.save("updated_image.png")

    return


def main():

    while True:
        # Watch for image capture button press.
        if GPIO.input(40) == GPIO.LOW:
            capture_image()
            os.system("python3 display_image.py image.jpg")

        # Watch for image modify button press.
        if GPIO.input(29) == GPIO.LOW:
            record_request()
            prompt = transcribe_request()
            modify_image(prompt)
            os.system("python3 display_image.py updated_image.png")

    return


if __name__ == "__main__":
    main()

