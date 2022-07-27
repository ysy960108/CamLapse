import os
import time
from threading import Thread

save_path = '/home/pi/camera'
capture_interval = 120
image_rotation = 0
web_server_port = 8080
skip_capture_on_night = True
skip_capture_from_hr = 21
skip_capture_to_hr = 6

stop_signal = 0


def wait_input():
    while True:
        global stop_signal
        res = input("Timelapse is running, type 'stop' to quit.\n")
        if res == 'stop':
            stop_signal = 1


def start_web():
    import http.server
    import socketserver
    import os
    web_dir = os.path.dirname('/home/pi/web')
    os.chdir(web_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", web_server_port), Handler)
    print('Starting web server on 0.0.0.0:{}'.format(web_server_port))
    httpd.serve_forever()


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('New folder {} created.'.format(path))
    else:
        print('Folder {} already exists, creation skipped.'.format(path))


def check_time(hr):
    if skip_capture_to_hr < skip_capture_from_hr:
        if hr >= skip_capture_from_hr or hr < skip_capture_to_hr:
            return False
    else:
        if skip_capture_from_hr <= hr < skip_capture_to_hr:
            return False
    return True


def start_capture():
    capture_count = 0
    last_time = time.time()
    start_time = time.strftime("%Y%m%d-%H%M%S")
    print("Starting capture...")
    mkdir('{}/{}'.format(save_path, start_time))
    thd = Thread(target=wait_input)
    thd.daemon = True
    thd.start()
    thd_web = Thread(target=start_web)
    thd_web.daemon = True
    thd_web.start()
    while True:
        now_time = time.time()
        hr = int(time.strftime('%H'))
        if stop_signal > 0:
            break
        if now_time - last_time > capture_interval:
            now_str = time.strftime("%Y%m%d-%H%M%S")
            if check_time(hr) or not skip_capture_on_night:
                write_path = '{}/{}/{}.jpg'.format(save_path, start_time, now_str)
                os.popen('raspistill -o {} -rot {}'.format(write_path, image_rotation))
                capture_count += 1
                print('{}: Image saved:, total: {}'.format(now_str, capture_count))
            else:
                print('{}: Capture skipped at night...'.format(now_str))
            last_time = now_time
        time.sleep(1)
    print('Capture stopped, {} pictures saved.'.format(capture_count))


start_capture()

