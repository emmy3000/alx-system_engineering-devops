#!/usr/bin/env ruby
#script takes a string as an argument and searches for a pattern of the form "hbt{n}"
#where n is between 2 and 5 inclusive, and then prints all occurrences of the pattern
#found in the string.

puts ARGV[0].scan(/hbt{2,5}n/).join

