# Embedded file name: c:\Jenkins\live\output\win_32_static\Release\python-bundle\MIDI Remote Scripts\Oxygen8v2\__init__.py
from _Generic.GenericScript import GenericScript
import Live
from config import *

def create_instance(c_instance):
    """ The generic script can be customised by using parameters (see config.py). """
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTION, MIXER_OPTIONS)