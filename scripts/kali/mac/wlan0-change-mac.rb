#!/usr/bin/env ruby

def interfaces_list
  list = []
  interfaces = `ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'`
  interfaces
    .split("\n")
    .reject { |c| c.empty? }
    .map { |e| e.chop!}
    .each { |i|
      list.push(i)
    }
  list
end

def random_mac
  new_mac = `~/myscripts/mac/genmac-master/genmac`
  new_mac
end

def change_mac (interface, new_mac)
  `ifconfig #{interface} down`
  `ifconfig #{interface} hw ether #{new_mac}`
  `ifconfig #{interface} up`
end

def print_mac_list interfaces 
  interfaces.each do |i|
    status = `ifconfig #{i} | grep ether | awk '{print $2}'`
    puts "#{i}: #{status}"
  end
end

print_mac_list interfaces_list
puts "\n------\n"
change_mac('wlan0',random_mac)
print_mac_list interfaces_list
