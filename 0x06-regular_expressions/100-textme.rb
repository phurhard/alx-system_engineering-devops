#!/usr/bin/env ruby
str =  ARGV[0].scan(/\[([^\]([TFSu])]*)\]/).join(", ")
#str.split(/(.*),(.*),(.*)/)
puts str
