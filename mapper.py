import sys
import re


for line in sys.stdin:
    
    line = line.strip().lower()
    line = (re.sub(r"[^a-zA-Z0-9]+", ' ', line))

    words = line.split()
    
    for word in words: 
        print ('%s\t%s' % (word, 1))