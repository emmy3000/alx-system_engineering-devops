#!/usr/bin/env ruby
#script extracts all uppercase letters from a given string
#and outputs them as a single string.
#Usage: ./7-OMG_WHY_ARE_YOU_SHOUTING.rb <string>

input_string=ARGV[0]
pattern=/[A-Z]/

puts input_string.scan(pattern).join

