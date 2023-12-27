# -*- coding: utf-8 -*-
import os
from threading import Thread, current_thread


def get_file_list(dir, ext):
    ext_files = [file for file in os.listdir(dir) if file.endswith(ext)]
    return ext_files


def get_device_list(platform):
    global d, n
    devices = {}
    if platform == 'ios':
        ios_res = os.popen('tidevice list').readlines()
        for r in ios_res:
            original_list = r.split('  ')
            filtered_list = list(filter(lambda x: x.strip() != '', original_list))
            if len(filtered_list) > 1:
                d = filtered_list[0]
                n = filtered_list[3]
            if d != 'UDID' and n != 'MarketName':
                devices[d] = n
        return devices
    elif platform == 'android':
        android_res = os.popen('adb devices').readlines()
        for r in android_res:
            if '\tdevice' in r:
                d = r.split('\t')[0]
                n = os.popen('adb -s ' + d + ' shell getprop ro.product.model').readlines()[0].replace('\n', '')
                devices[d] = n
        return devices
    else:
        print(f'暂不支持 {platform} 平台设备')


def install_app(device, file, platform):
    if platform == 'ios':
        os.system(f'tidevice -u {device} install {file}')
    elif platform == 'android':
        os.system(f'adb -s {device} install {file}')
    else:
        print(f'暂不支持 {platform} 平台设备安装')


def batch_install():
    if current_thread().name == 'ios':
        ios_files = get_file_list(os.getcwd(), '.ipa')
        print(ios_files)
        ios_devices = get_device_list('ios')
        names = []
        for key in ios_devices.keys():
            names.append(ios_devices[key])
        print(names)
        for ios_file in ios_files:
            for key in ios_devices.keys():
                install_app(device=key, file=ios_file, platform='ios')
    elif current_thread().name == 'android':
        android_files = get_file_list(os.getcwd(), '.apk')
        print(android_files)
        android_devices = get_device_list('android')
        names = []
        for key in android_devices.keys():
            names.append(android_devices[key])
        print(names)
        for android_file in android_files:
            for key in android_devices.keys():
                install_app(device=key, file=android_file, platform='android')
    else:
        pass


if __name__ == '__main__':
    ios_thread = Thread(target=batch_install, name='ios')
    android_thread = Thread(target=batch_install, name='android')
    ios_thread.start()
    android_thread.start()
    ios_thread.join()
    android_thread.join()
