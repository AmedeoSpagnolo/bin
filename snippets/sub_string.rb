content = "{{first}}. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation {{second}} ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. {{third}}"

new_content = content
new_content = new_content.gsub("{{first}}", "word_1")
new_content = new_content.gsub("{{second}}", "word_2")
new_content = new_content.gsub("{{third}}", "word_3")

puts new_content
