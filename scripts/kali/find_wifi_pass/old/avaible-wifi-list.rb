#!/usr/bin/env ruby

puts `echo "my connection:"`
puts `nmcli d`
puts `echo ""`
puts `echo "available:"`
puts `nmcli d wifi list`
# puts `nmcli -p con show chingching`
