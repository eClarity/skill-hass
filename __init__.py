# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from requests import get
import json

discovery_url = 'http://localhost:8123/api/discovery_info'
config_url = 'http://localhost:8123/api/config'

headers = { 'content-type': 'application/json'}

discovery_response = get(discovery_url, headers=headers)
sentence = discovery_response.text

config_response = get(config_url, headers=headers)
config_sentence = config_response.text

__author__ = 'eclarity'

LOGGER = getLogger(__name__)

class HassSkill(MycroftSkill):
    def __init__(self):
        super(HassSkill, self).__init__(name="HassSkill")

    def initialize(self):
        hass_services_intent = IntentBuilder("HassServicesIntent"). \
            require("HassServices").build()
        self.register_intent(hass_services_intent,
                             self.handle_hass_services_intent)

        hass_config_intent = IntentBuilder("HassConfigIntent"). \
            require("HassConfig").build()
        self.register_intent(hass_config_intent,
                             self.handle_hass_config_intent)

    def handle_hass_services_intent(self, message):
        self.speak(sentence)

    def handle_hass_config_intent(self, message):
        self.speak(config_sentence)

    def stop(self):
        pass


def create_skill():
    return HassSkill()
