#!/usr/bin/env ruby
#script accepts a string argument uses regex to match all instances
#of the pattern 'h.n' in the string, then returns the matches as a
#single string.
puts ARGV[0].scan(/h.n/).join

