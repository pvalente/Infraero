#!/usr/bin/env python2.5
#coding: utf-8

from google.appengine.api import memcache
import logging

def get_cache(k):
    item = None
    item = memcache.get(k)
    return item

def set_cache(k,v, sec=3000):
    if not memcache.add(k, v, sec):
          logging.error("Memcache set failed.")

def set_multi(kvdic, prefix ,v, sec=3000):
    if not memcache.set_multi(kvdic, prefix, sec):
          logging.error("Memcache set failed.")