#!/usr/bin/env python
#coding: utf-8
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import Infraero
import yql
import time
from airports import code_to_icao, icao_to_code
from cache import get_cache, set_cache

class MainHandler(webapp.RequestHandler):

  def get(self):
    s = ('status', 'Aeronave no P\xc3\xa1tio')
    self.response.out.write('hello')

class InfraeroHandler(webapp.RequestHandler):

  def get(self):
    
    
    airport = self.request.get('airport').upper()
    
    if len(airport) == 3:
        airport_code = airport 
        airport_icao = code_to_icao.get(airport)
    elif len(airport) == 4:
        airport_icao = airport 
        airport_code = icao_to_code.get(airport)
        
    flight_number = self.request.get('flight')
    
    flights = self.downloadData(airport_icao, flight_number)
    
    content = ""

    for flight in flights:    
        content = content + """
<flight>
    <airport_code>%s</airport_code>
    <airport_icao>%s</airport_icao>
    <flight_number>%d</flight_number>
    <company>%s</company>
    <from_city>%s</from_city>
    <from_state>%s</from_state>
    <date>%s</date>
    <time_expected>%s</time_expected>
    <time_confirmed>%s</time_confirmed>
    <stops>%s</stops>
    <status>%s</status>
    <from_cache>%s</from_cache>
</flight>
""" % ( 
        airport_code, 
        airport_icao, 
        int(flight[1][1]), 
        flight[0][1], 
        flight[2][1].decode('UTF-8'), 
        flight[3][1], 
        flight[4][1], 
        flight[5][1], 
        flight[6][1], 
        flight[7][1].strip().decode('UTF-8'), 
        flight[8][1].decode('UTF-8'),
        flight[9][1] )
    
    result = "<?xml version='1.0' encoding='UTF-8'?>\n<results>%s</results>" % (content)
    
    self.response.headers['Content-type'] = 'application/xml'
    self.response.out.write(result)


  def downloadData(self, airport_icao, flight_number=None):
    infra = Infraero.Harvester()
    if flight_number:
        key = airport_icao+str(int(flight_number))
        flight = get_cache(key)
        if not flight:
            flights = infra.request_flight(airport_icao, flight_number)
            set_cache(key, flights[0], 60*5)
            flights[0].append( ('from_cache','False') )
        else:
            flights = [ flight ]
            flights[0].append( ('from_cache','True') )
    else:
        key = airport_icao
        flights = get_cache(key)
         
        if not flights:
            flights = infra.request_airport(airport_icao)
            set_cache(key, flights, 60*5)
            for flight in flights:
                set_cache(key+str(int(flight[1][1])), flight, 60*5)
                flight.append( ('from_cache','False') )
        else:
            for flight in flights:
                flight.append( ('from_cache','True') )
    return flights



def main():
  application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/infraero/arrivals/', InfraeroHandler),
                                        ],
                                       debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
