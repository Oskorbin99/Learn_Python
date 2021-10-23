import os
import mutagen

def length_music_file(address):
    if address[-3:] == "mp3" or address[-3:] == "m4a":
        return int(mutagen.File(address).info.length)  # legth
    else:
        return 0


def change_address(address, root, name):
    name_change = name[:-4]
    pos = 0
    for i, x in enumerate(name_change):
        if x.isalpha():
            pos = i
            break
    new_name = root + "\\" + name[pos:].capitalize()
    try:
        os.rename(address, new_name)
    except FileExistsError:
        os.remove(address)


directory_list = list()
for root, dirs, files in os.walk("D:/Test", topdown=False):
    for name in files:
        now_file = os.path.join(root, name)
        now_file_length = length_music_file(now_file)
        if now_file_length <= 60 or now_file_length >= 360:
            os.remove(now_file)
        else:
            change_address(now_file, root, name)

