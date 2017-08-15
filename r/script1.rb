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
  data = read_json_file "#{file_name}.json"
  export_json = []
  data.each do |el|
    _x = el["Longitude"].to_f
    _y = el["Latitude"].to_f
    _t = el["time"]
    export_json.push([_x,_y,_t]) if _x != 0 && _y != 0
  end
  save_json_to_file "#{file_name}_positions_only.json", export_json
end

def print_length file_name
  data = read_json_file "#{file_name}.json"
  data_pos = read_json_file "#{file_name}_positions_only.json"
  p "----"
  p file_name
  p data.length
  p data_pos.length
end

def combine_multiple_json_file array_file_names
  temp = []
  p array_file_names.length
  array_file_names.each do |filename|
    p filename
    data = read_json_file filename
    data.each do |el|
      temp.push(el)
    end
  end
  return temp
end

  # data_pos = read_json_file "#{file_name}_positions_only.json"
  # p "----"
  # p file_name
  # p data.length
  # p data_pos.length

name = [
  "temp/HKG - Cordis, Hong Kong_2016-09-01_positions_only.json",
  "temp/HKG - Cordis, Hong Kong_2016-10-01_positions_only.json",
  "temp/HKG - Cordis, Hong Kong_2016-11-01_positions_only.json",
  "temp/HKG - Cordis, Hong Kong_2016-12-01_positions_only.json",
  "temp/HKG - Cordis, Hong Kong_2017-01-01_positions_only.json",
  "temp/HKG - Cordis, Hong Kong_2017-02-01_positions_only.json",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2016-09-01",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2016-10-01",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2016-11-01",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2016-12-01",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2017-01-01",
  # "temp/HKG - Dorsett Tsuen Wan Hong Kong_2017-02-01"
]

# name.each do |elem|
  # print_length elem
  # export_clean_json elem
# end

comb = combine_multiple_json_file name
save_json_to_file "temp/cordis.json", comb
