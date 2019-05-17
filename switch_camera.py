#!/usr/bin/env python

'''Farmware: switch between USB and Raspberry Pi cameras.'''

import os
import json
from farmware_tools import device

camera = os.getenv('camera', 'USB')
switch_camera_to = 'RPI' if 'USB' in camera else 'USB'
device.set_user_env('camera', json.dumps(switch_camera_to))
