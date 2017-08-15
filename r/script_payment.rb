require 'json'

def delete_key_from_hash hash_name, key_name
  hash_name.delete(key_name)
end

def save_json_to_file file_name, json_data
  File.open(file_name, "w") do |f|
    f.write(json_data.to_json)
  end
end

def read_json_file file_name
  file = File.read(file_name)
  data_hash = JSON.parse(file)
end

def export_clean_json file_name
  data = read_json_file "mixpanel_payments/#{file_name}.json"
  export_json = {}
  data.each do |el|
    export_json[el["Deal Title"]] = {
      "pos": [el["Longitude"].to_f, el["Latitude"].to_f],
      "time": el["time"],
      "hotel": el["Service Counter"]
    } if el["Longitude"].to_f != 0 && el["Latitude"].to_f != 0
  end
  save_json_to_file "mixpanel_payments/#{file_name}_positions_only.json", export_json
end

def print_length file_name
  data = read_json_file "mixpanel_payments/#{file_name}.json"
  data_pos = read_json_file "mixpanel_payments/#{file_name}_positions_only.json"
  p "----"
  p file_name
  p data.length
  p data_pos.length
end

# name = [
#   "UAE - Dubai - Dusit Thani Dubai_2017-01-01",
#   "UAE - Dubai - Dusit Thani Dubai_2017-02-01",
#   "UAE - Dubai - Fairmont The Palm_2017-01-01",
#   "UAE - Dubai - Fairmont The Palm_2017-02-01",
#   "UAE - Dubai - Le Meridien Mina Seyahi Beach Resort & Marina_2017-01-01",
#   "UAE - Dubai - Le Meridien Mina Seyahi Beach Resort & Marina_2017-02-01",
#   "UAE - Dubai - The Westin Dubai Mina Seyahi_2017-01-01",
#   "UAE - Dubai - The Westin Dubai Mina Seyahi_2017-02-01"
# ]

# name.each do |elem|
  # print_length elem
  # export_clean_json elem
# end

export_clean_json "HKG - Cordis, Hong Kong__2016-11-01"
