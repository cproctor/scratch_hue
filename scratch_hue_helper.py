#! /usr/bin/python

# Scratch Hue Helper app
# ----------------------
# (c) 2015 Chris Proctor
# Distributed under the MIT license.
# Project homepage: http://mrproctor.net/scratch

import phue
import json
import httplib
from flask import Flask
import logging
import os
import sys
from os import path

def copy_description_file():
    source = path.join(path.dirname(path.abspath(__file__)), 'scratch_hue_extension.s2e')
    destination = path.join('/Users', os.environ['USER'], 'Desktop', 'scratch_hue_extension.s2e')
    with open(source) as sourceFile:
        with open(destination, 'w') as destinationFile:
            destinationFile.write(sourceFile.read())

copy_description_file()

def get_ip_address():
    app.logger.info("Looking for Bridge IP address...")
    connection = httplib.HTTPSConnection('www.meethue.com')
    connection.request('GET', '/api/nupnp')
    result = connection.getresponse()
    result_str = result.read()
    data = json.loads(result_str)
    connection.close()
    return str(data[0]['internalipaddress']) or False

def create_scale(d_min, d_max, r_min, r_max):
    def scale(val):
        normalized = (val - d_min) / float(d_max - d_min)
        return max(r_min, min(r_max, int((r_max - r_min) * normalized + r_min)))
    return scale

color_scale = create_scale(0, 199, 0, 65535)
brightness_scale = create_scale(0, 100, 0, 254)

app = Flask("hue_helper_app")
app.logger.removeHandler(app.logger.handlers[0])

loggers = [app.logger, logging.getLogger('phue'), logging.getLogger('werkzeug')]
# No logging. Switch out handlers for logging.
# handler = logging.FileHandler('scratch_hue_extension.log')
handler = logging.NullHandler()
formatter = logging.Formatter('%(asctime)s - %(name)14s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
for logger in loggers:
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

ip = get_ip_address()
app.logger.info("Found bridge at " + ip)
bridge = phue.Bridge(ip)
jobs = set()

def reset():
    for light in bridge.lights:
        light.on = True
        light.brightness = brightness_scale(100)
        light.saturation = 254
        light.color = 0
        light.transitiontime = 0
        light.off = True

reset()

@app.route('/poll')
def poll():
    return "\n".join(["_busy {}".format(job) for job in jobs])

@app.route('/setcolor/<int:jobId>/<int:lightId>/<int:color>')
def set_color(jobId, lightId, color):
    jobs.add(jobId)
    bridge[lightId].hue = color_scale(color)
    jobs.remove(jobId)
    return "OK"
    
@app.route('/setbrightness/<int:jobId>/<int:lightId>/<int:brightness>')
def set_brightness(jobId, lightId, brightness):
    jobs.add(jobId)
    bridge[lightId].brightness = brightness_scale(brightness)
    jobs.remove(jobId)
    return "OK"

@app.route('/seton/<int:jobId>/<int:lightId>/<onstate>')
def set_on_state(jobId, lightId, onstate):
    jobs.add(jobId)
    if onstate == 'on':
        bridge[lightId].on = True
        bridge[lightId].brightness = brightness_scale(100)
    else:
        bridge[lightId].on = False
    jobs.remove(jobId)
    return "OK"

@app.route('/reset_all')
def reset_all():
    reset()
    return "OK"

@app.route('/crossdomain.xml')
def cross_domain_check():
    return """
<cross-domain-policy>
    <allow-access-from domain="*" to-ports="3316"/>
</cross-domain-policy>
"""

print("The Scratch helper app for controlling Hue lights is running.")
print("See mrproctor.net/scratch for help.")
print("Press Control + C to quit.")
app.run('0.0.0.0', port=3316)
