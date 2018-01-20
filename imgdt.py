# -*- coding: utf-8 -*-

import datetime
import os
import sys

def abort(msg):
    print(msg)
    exit(1)

def get_directory(path):
    return os.path.dirname(path)

def get_filename(path):
    return os.path.basename(path)

def get_basename(path):
    return os.path.splitext(get_filename(path))[0]

def get_extension(path):
    return os.path.splitext(get_filename(path))[1]

def filepath_to_datetimestr(filepath):
    timestamp = os.stat(filepath).st_mtime
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%y%m%d_%H%M%S')

curdir = os.getcwd()
filenames = os.listdir(curdir)
valid_exts = ['.jpg', '.png']
filenames = [fn for fn in filenames if get_extension(fn.lower()) in valid_exts]
filecount = len(filenames)

if filecount==0:
    abort('No image files.')

def image_to_dt(curdir, filenames, enable=False):
    for i in range(filecount):
        filename = filenames[i]

        fullpath = os.path.join(curdir, filename)
        datetimestr = filepath_to_datetimestr(fullpath)

        # 秒単位でファイル名にしてるから被ることはないやろ.
        # (1秒に2枚以上撮るとか連射しない限りは無理なはず)
        # ... というわけで既存なら連番増やす, なんて対応はしない.
        before_name = filename
        after_name = '{:}{:}'.format(datetimestr, get_extension(filename))

        if enable:
            old = fullpath
            new = os.path.join(curdir, after_name)
            os.rename(old, new)
        else:
            print('{:} -> {:}'.format(before_name, after_name))

image_to_dt(curdir, filenames, enable=False)
print('{:} items, do rename?'.format(filecount))
print('>', end='')
try:
    res = input()
except EOFError:
    res = None

if not res in ['y', 'yes']:
    abort('Canceled.')

image_to_dt(curdir, filenames, enable=True)
print('fin.')
