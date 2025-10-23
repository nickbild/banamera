# Banamera

Banamera is an AI-powered digital camera that edits your photos using voice commands.

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/logo_sm.jpg)

AI image editors are incredibly useful. In a few seconds, you can make edits that might take an hour or more to do manually. Up until recently, these tools could be a bit wonky, to say the least, so the results weren’t always something you could use. But the release of Google's Nano Banana changed that in a big way. It regularly surprises me with how accurate it is in following instructions.

But the user experience through the web interface is less than ideal. Upload an image. Type out a request. Wait. Download the result. Repeat for each image. So that’s why I created what I call the Banamera.

It’s a digital camera that takes pictures just like any other camera when you press a button. But when you press the *other* button — that’s when the magic happens. A microphone on the side records your voice, and the request that you make is forwarded to the Nano Banana API behind the scenes. Within a matter of seconds, the image on the screen updates, showing the result produced by the model.

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/front_angle_sm.jpg)

## How It Works

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/prototype_sm.jpg)

The Banamera is built around a Raspberry Pi Zero 2 W single-board computer. I have a Camera Module 2 connected to the computer to capture images, and a 2.2-inch LCD display to show the captured images. There is also an I2S MEMS microphone to record the user’s voice.

Everything is controlled by two buttons, as previously mentioned. One simply snaps a picture, and the other edits it based on a verbal request.

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/banamera.jpg)

When the edit button is pressed, the device will first record audio from the microphone, allowing the user to explain how they want the image to be edited. That audio is then forwarded along to a Gemini 2.5 Flash LLM, along with a prompt instructing it to return only a transcript of the audio contained in the attached audio file. The extracted text is then sent to Nano Banana, along with the image captured by the camera. When the result is returned, it is displayed on the Banamera’s screen.

## Media

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/back_off_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/back_close_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/back_angle_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/front_close_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/front_unchanged_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/moon_fig_clear_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/moon_screen_clear_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/side_angle_sm.jpg)

![](https://raw.githubusercontent.com/nickbild/banamera/refs/heads/main/media/generated_image.moon.png)

## Bill of Materials

- 1 x Raspberry Pi Zero 2 W
- 1 x Raspberry Pi Camera Module 2
- 1 x Adafruit 2.2-inch, 320x240 TFT display
- 1 x Adafruit I2S MEMS microphone
- 2 x Push buttons
- Assorted LEGO bricks (or a 3D printer if you want to be fancy)

## About the Author

[Nick A. Bild, MS](https://nickbild79.firebaseapp.com/#!/)
