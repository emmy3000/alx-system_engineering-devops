#!/usr/bin/env ruby
#script searches for the regex pattern 'hbt?n' in the input string and output its matches.
#The regex matches 'hbtn' or 'hbtn' with 'b' optional.
puts ARGV[0].scan(/hb?tn/).join

