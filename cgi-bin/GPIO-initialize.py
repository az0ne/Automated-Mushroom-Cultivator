#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import ConfigParser

#### Configure Install Directory ####
install_directory = "/var/www/mycodo"
#### Configure Install Directory ####

config_file = "%s/config/mycodo.cfg" % install_directory

# GPIO pins (BCM numbering) and name of devices attached to relay
relayPin = [0] * 9
relayTrigger = [0] * 9

def ReadCfg():
    global relayPin
    global relayTrigger

    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    relayPin[1] = config.getint('RelayPins', 'relay1pin')
    relayPin[2] = config.getint('RelayPins', 'relay2pin')
    relayPin[3] = config.getint('RelayPins', 'relay3pin')
    relayPin[4] = config.getint('RelayPins', 'relay4pin')
    relayPin[5] = config.getint('RelayPins', 'relay5pin')
    relayPin[6] = config.getint('RelayPins', 'relay6pin')
    relayPin[7] = config.getint('RelayPins', 'relay7pin')
    relayPin[8] = config.getint('RelayPins', 'relay8pin')
    
    relayTrigger[1] = config.getint('RelayTriggers', 'relay1trigger')
    relayTrigger[2] = config.getint('RelayTriggers', 'relay2trigger')
    relayTrigger[3] = config.getint('RelayTriggers', 'relay3trigger')
    relayTrigger[4] = config.getint('RelayTriggers', 'relay4trigger')
    relayTrigger[5] = config.getint('RelayTriggers', 'relay5trigger')
    relayTrigger[6] = config.getint('RelayTriggers', 'relay6trigger')
    relayTrigger[7] = config.getint('RelayTriggers', 'relay7trigger')
    relayTrigger[8] = config.getint('RelayTriggers', 'relay8trigger')

ReadCfg()

for i in range(1, 9):
    if relayTrigger[i] == 0: relayTrigger[i] = 1;
    else: relayTrigger[i] = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(1, 9):
    GPIO.setup(relayPin[i], GPIO.OUT)
    GPIO.output(relayPin[i], relayTrigger[i])