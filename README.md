# Hue Rotation Looper
This code transforms a .png image into a .avi hue rotated loop.

Hue rotation means to individually increment some offset to the hue of each pixel in an image. This code creates a video of a continuously rotating hue from a photo.
## Example

![spooky skeleton](https://media.giphy.com/media/ftfT93cCdlKvT7icgh/200w_d.gif)

[Full video](https://media.giphy.com/media/ftfT93cCdlKvT7icgh/giphy.mp4)

## Dependencies
This code depends on the following Python3 modules.

```
numpy
Pillow
imageio
imageio-ffmpeg

```

Should you find you do not have these installed get them with pip like so.

```bash
pip install numpy Pillow imageio imageio-ffmpeg
```

or

```bash
pip install -r requirements.txt
```
