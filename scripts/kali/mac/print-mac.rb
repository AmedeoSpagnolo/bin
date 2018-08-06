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

interfaces_list.each do |i|
  status = `ifconfig #{i} | grep ether | awk '{print $2}'`
  puts "#{i}: #{status}"
end
