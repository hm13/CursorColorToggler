#! /usr/bin/python2.6

import ibus
import os
bus = ibus.Bus()
ic  = ibus.InputContext(bus, bus.current_input_contxt())
if ic.is_enabled():
    os.system('echo -en "\e]12;#ffcdcd\a"')
else:
    os.system('echo -en "\e]12;#00cdcd\a"')

    
