#!/usr/bin/env ruby
#script searches for the regex pattern 'hbt?n' in the input string and output its matches.
#The regex matches 'hbtn' or 'hbtn' with 'b' optional.

input_string=ARGV[0]
pattern=/hb?n/

puts input_string.scan(pattern).join(' ')

