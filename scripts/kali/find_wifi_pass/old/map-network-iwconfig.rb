#!/usr/bin/env ruby

puts `iwlist wlan0 scanning|grep -i 'essid'`
