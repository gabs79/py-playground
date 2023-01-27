#!/usr/bin/env python

import time
import sys

for i in range(100):
	time.sleep(0.05)
	sys.stdout.write("Downloading progress: %d%%   \r" % (i) )
	sys.stdout.flush()
complete = "Download complete."
print(f'{"Download complete.":<32}')
