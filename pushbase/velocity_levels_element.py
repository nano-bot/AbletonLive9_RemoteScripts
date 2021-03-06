# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\pushbase\velocity_levels_element.py
from __future__ import absolute_import, print_function
from ableton.v2.base import EventObject, listenable_property
from .proxy_element import ProxyElement

class NullVelocityLevels(EventObject):
    enabled = False
    target_note = -1
    target_channel = -1
    source_channel = -1
    notes = []

    @property
    def levels(self):
        return []

    @listenable_property
    def last_played_level(self):
        return -1.0


class VelocityLevelsElement(ProxyElement):

    def __init__(self, velocity_levels = None, *a, **k):
        super(VelocityLevelsElement, self).__init__(proxied_object=velocity_levels, proxied_interface=NullVelocityLevels())

    def reset(self):
        self.notes = []
        self.source_channel = -1