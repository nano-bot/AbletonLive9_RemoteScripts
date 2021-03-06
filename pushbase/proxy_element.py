# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\pushbase\proxy_element.py
from __future__ import absolute_import, print_function
from ableton.v2.base import Proxy
from ableton.v2.control_surface import ControlElement

class ProxyElement(Proxy, ControlElement):

    def reset(self):
        try:
            super(ProxyElement, self).__getattr__('reset')()
        except AttributeError:
            pass