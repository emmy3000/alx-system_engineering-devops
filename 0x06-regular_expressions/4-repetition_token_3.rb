#!/usr/bin/env ruby
#script accepts one argument and matches regex with 0 or more 't' characters
#It then joins the matching string elements and prints it to the screen.

input_string=ARGV[0]
pattern=/hbt*n/
puts input_string.scan(pattern).join

