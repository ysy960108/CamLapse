import os
import time
import cv2

device_index = 0
save_path = 'E:/CamLapseSave'
capture_interval = 10


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('New folder {} created.'.format(path))
    else:
        print('Folder {} already exists, creation skipped.'.format(path))


def start_capture():
    cap = cv2.VideoCapture(device_index)
    capture_count = 0
    last_time = time.time()
    start_time = time.strftime("%Y%m%d-%H%M%S")
    print("Starting capture...")
    mkdir('{}/{}'.format(save_path, start_time))
    while True:
        ret, frame = cap.read()
        now_time = time.time()
        if now_time - last_time > capture_interval:
            now_str = time.strftime("%Y%m%d-%H%M%S")
            write_path = '{}/{}/{}.jpg'.format(save_path, start_time, now_str)
            cv2.imwrite(write_path, frame)
            print('Debug: Image saved: {}.jpg.'.format(now_str))
            last_time = now_time
            capture_count += 1
        k = cv2.waitKey(25)
        if k == 27:
            break
        cv2.imshow("capture", frame)
    cap.release()
    print('Capture stopped, {} pictures saved.'.format(capture_count))


start_capture()
