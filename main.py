import os


def get_ipa_filenames(path):
    filenames = os.listdir(path)
    ipa_filenames = []
    for filename in filenames:
        if filename.endswith('.ipa'):
            ipa_filenames.append(filename)
    return ipa_filenames


def get_device_list():
    result = os.popen("tidevice list").readlines()
    devices = []
    for r in result:
        d = r.split(' ')[0]
        print(d)
        if d != 'UDID' and d != '\x1b[0m':
            devices.append(d)
    return devices


def install_ipa(device, ipa_name):
    cmd = f'tidevice -u {device} install {ipa_name}'
    os.system(cmd)


def batch_install():
    ipa_names = get_ipa_filenames('.')
    devices = get_device_list()
    for device in devices:
        for ipa_name in ipa_names:
            install_ipa(device, ipa_name)


if __name__ == '__main__':
    ios_res = os.popen('tidevice list').readlines()
    for r in ios_res:
        original_list = r.split('  ')
        filtered_list = list(filter(lambda x: x.strip() != '', original_list))
        print(filtered_list)
        if len(filtered_list) > 1:
            d = filtered_list[0]
            n = filtered_list[3]
