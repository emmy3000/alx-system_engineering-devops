#!/usr/bin/env ruby
#script extracts specific data from a string and joins them using a comma

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

