#!/usr/bin/env ruby
print ARGV[0].scan(/from:([+]?\d+)/).join(',') + ','
print ARGV[0].scan(/to:([+]?\d+)/).join(',') + ','
print ARGV[0].scan(/flags:(.*?)\]/).join
