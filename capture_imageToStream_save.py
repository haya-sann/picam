#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   ↑↑コードの中に日本語の注釈を入れたいといったときにはcoding:utf-8を書く
# http://picamera.readthedocs.io/
#にあったサンプル
#
#
from time import sleep
from picamera import PiCamera

# Explicitly open a new file called my_image.jpg
my_file = open('my_image.jpg', 'wb')
camera = PiCamera()
camera.start_preview()
sleep(2)

camera.rotation = 180
camera.capture(my_file)
# At this point my_file.flush() has been called, but the file has
# not yet been closed
my_file.close()
