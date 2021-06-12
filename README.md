# CamLapse
A tiny Timelapse tool based on python and opencv.

## How to use
### Install opencv-python
```
pip install opencv-python
```
### Configure
Edit CamLapse.py, line 5-7
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
### Run script
```
python CamLapse.py
```
or
```
python3 CamLapse.py
```
