#!/usr/bin/python

import subprocess
import sys

output = "this is a test"

subprocess.call(["touch", "stolen_creds.txt"])
fileObject = open("stolen_creds.txt", "w")
print >>fileObject, output

