def interfaces
  interfaces_array = []
  $INTERFACES=`ifconfig -a | sed 's/[ \t].*//;/^\(lo\|\)$/d'`
  $INTERFACES
    .split("\n")
    .reject { |c| c.empty? }
    .map { |e| e.chop!}
    .each { |i|
      interfaces_array.push(i) if i != 'lo'
    }
    interfaces_array
end

p interfaces

puts `nmcli c`

interfaces.each do |interf|
  puts `ifconfig #{interf} down`
end

hasActiveConnection = `ls /etc/NetworkManager/system-connections/ | wc -l`.to_i != 0

puts `rm /etc/NetworkManager/system-connections/*` if hasActiveConnection

puts `ifconfig`
