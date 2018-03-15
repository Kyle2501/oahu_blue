#!/usr/bin/env python



  # - System
import os
import cgi
import urllib
import wsgiref.handlers
import datetime
import json, ast
import sys,imp
  # - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
  # -
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app

import _html as _html


main_nav_list = '''
<a href="../../fm_radio"><li>FM Radio</li></a>
<a href="../../user_profiles"><li>User Profiles</li></a>
<a href="../../social_graph"><li>Social Graph</li></a>
<a href="../../dashboard_feed"><li>Dashboard Feed</li></a>
<a href="../../nfc_contact"><li>NFC Contact</li></a>
<a href="../../qrcode_vibe"><li>QR Code Vibe</li></a>
<a href="../../adhoc_tooth"><li>Ad-Hoc Tooth</li></a>
<a href="../../maps_gps"><li>Maps GPS</li></a>
<a href="../../user_photos"><li>User Photos</li></a>
<a href="../../forcast_data"><li>Forcast Data</li></a>
<a href="../../events_agenda"><li>Events Agenda</li></a>
<a href="../../buddy_list"><li>Buddy List</li></a>
<a href="../../local_pages"><li>Local Pages</li></a>
'''


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class FM_Radio_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class userProfile_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class socialGraph_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class dashboardFeed_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class NFC_Contact_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()

#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class QRcode_Vibe_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class adHoc_Tooth_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class mapsGPS_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class userPhotos_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class forcastData_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class eventsAgenda_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class buddyList_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


#----------------------------------------------#
#       Bikini Bootcamp Data Stucture          #
#----------------------------------------------#
class localPages_db(ndb.Model):
    add_time = ndb.DateTimeProperty(auto_now_add=True)
    data_id = ndb.StringProperty()
  #
    user_name = ndb.StringProperty()
  #
    video_id = ndb.StringProperty()
    video_name = ndb.StringProperty()
    video_text = ndb.StringProperty()
    video_icon = ndb.BlobProperty()
    video_key = ndb.StringProperty()


class publicSite(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
      
        html_file = 'main_layout.html'
        
        main_nav = main_nav_list
        
        page_html = 'hi'
        
        if path_layer == 'fm_radio':
            page_id = 'fm_radio'
            page_name = 'FM Radio'
            page_html = _html.fm_radio
            nav_select = 'fm_radio'
            if base == 'about':
              page_html = _html.fm_radio_about
        
        if path_layer == 'user_profiles':
            page_id = 'user_profiles'
            page_name = 'User Profiles'
            page_html = _html.user_profiles
            nav_select = 'user_profiles'
            if base == 'about':
              page_html = _html.user_profiles_about
            
        if path_layer == 'social_graph':
            page_id = 'social_graph'
            page_name = 'Social Graph'
            page_html = _html.social_graph
            nav_select = 'social_graph'
            if base == 'about':
              page_html = _html.social_graph_about
        
        if path_layer == 'dashboard_feed':
            page_id = 'dashboard_feed'
            page_name = 'Dashboard Feed'
            page_html = _html.dashboard_feed
            nav_select = 'dashboard_feed'
            if base == 'about':
              page_html = _html.dashboard_feed_about
            
        if path_layer == 'nfc_contact':
            page_id = 'nfc_contact'
            page_name = 'NFC Contact'
            page_html = _html.nfc_contact
            nav_select = 'nfc_contact'
            if base == 'about':
              page_html = _html.nfc_contact_about
        
        if path_layer == 'qrcode_vibe':
            page_id = 'qrcode_vibe'
            page_name = 'QR Code Vibe'
            page_html = _html.qrcode_vibe
            nav_select = 'qrcode_vibe'
            if base == 'about':
              page_html = _html.qrcode_vibe_about
            
        if path_layer == 'adhoc_tooth':
            page_id = 'adhoc_tooth'
            page_name = 'Ad-Hoc Tooth'
            page_html = _html.adhoc_tooth
            nav_select = 'adhoc_tooth'
            if base == 'about':
              page_html = _html.adhoc_tooth_about

        if path_layer == 'maps_gps':
            page_id = 'maps_gps'
            page_name = 'Maps GPS'
            page_html = _html.maps_gps
            nav_select = 'maps_gps'
            if base == 'about':
              page_html = _html.maps_gps_about

        if path_layer == 'user_photos':
            page_id = 'user_photos'
            page_name = 'User Photos'
            page_html = _html.user_photos
            nav_select = 'user_photos'
            if base == 'about':
              page_html = _html.user_photos_about

        if path_layer == 'forcast_data':
            page_id = 'forcast_data'
            page_name = 'Forcast Data'
            page_html = _html.forcast_data
            nav_select = 'forcast_data'
            if base == 'about':
              page_html = _html.forcast_data_about

        if path_layer == 'events_agenda':
            page_id = 'events_agenda'
            page_name = 'events_agenda'
            page_html = _html.events_agenda
            nav_select = 'events_agenda'
            if base == 'about':
              page_html = _html.events_agenda_about

        if path_layer == 'buddy_list':
            page_id = 'buddy_list'
            page_name = 'buddy_list'
            page_html = _html.buddy_list
            nav_select = 'buddy_list'
            if base == 'about':
              page_html = _html.buddy_list_about

        if path_layer == 'local_pages':
            page_id = 'local_pages'
            page_name = 'local_pages'
            page_html = _html.local_pages
            nav_select = 'local_pages'
            if base == 'about':
              page_html = _html.local_pages_about



      # - template
        objects = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
        
            'main_nav': main_nav,
        
            'page_html': page_html
        
        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html/%s' %html_file)
        self.response.out.write(template.render(path, objects))




app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),
    ('/fm_radio/?', publicSite),
      ('/fm_radio/about/?', publicSite),
    ('/user_profiles/?', publicSite),
      ('/user_profiles/about/?', publicSite),
    ('/social_graph/?', publicSite),
      ('/social_graph/about/?', publicSite),
    ('/dashboard_feed/?', publicSite),
      ('/dashboard_feed/about/?', publicSite),
    ('/nfc_contact/?', publicSite),
      ('/nfc_contact/about/?', publicSite),
    ('/qrcode_vibe?/?', publicSite),
      ('/qrcode_vibe?/about/?', publicSite),
    ('/adhoc_tooth/?', publicSite),
      ('/adhoc_tooth/about/?', publicSite),
    ('/maps_gps/?', publicSite),
      ('/maps_gps/about/?', publicSite),
    ('/user_photos/?', publicSite),
      ('/user_photos/about/?', publicSite),
    ('/forcast_data/?', publicSite),
      ('/forcast_data/about/?', publicSite),
    ('/events_agenda/?', publicSite),
      ('/events_agenda/about/?', publicSite),
    ('/buddy_list/?', publicSite),
      ('/buddy_list/about/?', publicSite),
    ('/local_pages/?', publicSite),
      ('/local_pages/about/?', publicSite),
  

], debug=True)
