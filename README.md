# CamLapse
A tiny Timelapse tool based on python and opencv.

## How to use
### Install opencv-python
```
pip install opencv-python
```
### Configure
Edit CamLapse.py, line 5-8
```
# If you have multiple video capture device, you can change it to 1,2,... , otherwise, leave it to 0
device_index = 0
```
```
# Image save path
save_path = 'E:/CamLapseSave' 
```
```
# Set capture interval to every 10 seconds
capture_interval = 10 
```
```
# Set capture resolution, e.g. '1920x1080', '1280x720', or 'auto' which will use max resolution
# Supports size < 10000px
frame_resolution = 'auto'
```
### Run script
```
python CamLapse.py
```
or
```
python3 CamLapse.py
```
Then you can see a video capture window, and images will be captured automaticlly.
#### Stop capture
press ESC to stop image capture.
