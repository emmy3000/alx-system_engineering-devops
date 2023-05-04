#!/usr/bin/env ruby
#script accepts a single argument and matches a string of exactly 10 digits
#at the beginning and end of the string.
input_string=ARGV[0]
pattern=/\A\d{10}\z/
puts input_string.scan(pattern).join

