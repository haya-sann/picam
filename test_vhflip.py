#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
camera = picamera.PiCamera()
camera.resolution = (1280, 720)
camera.vflip = True
camera.hflip = False
camera.brightness = 60
camera.rotation = 0
camera.start_preview()

camera.capture('/home/pi/nas/photo/image_test_masuda_hflip.jpg')

