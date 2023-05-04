#!/usr/bin/env ruby
#script on execution searches for the word "School" in the first command line arguement
#and prints out all occurrences of the word in a string.

if __FILE__==$0
  pattern=/School/
  input_string=ARGV[0]
  puts input_string.scan(pattern).join
end
