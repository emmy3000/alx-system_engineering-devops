#!/usr/bin/env ruby
#script searches for any string that contains "hbt" followed by ione or more 'n' characters
#It accepts one argument and passes it to a regex matching method.

input_string=ARGV[0]
pattern=/hbt+n/

puts input_string.scan(pattern).join

