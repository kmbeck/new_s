import json
import os
import pathlib

# Contains paths listed in 'res/directories.json'
directories = json.load(open(str(pathlib.Path(__file__).parent.absolute()) + '/res/directories.json'))

def get(dir_name):
	'''
	Gets directory with 'dir_name' with absolute filepath prepended.
	'''
	if (directories.get(dir_name) is not None):
		return str(pathlib.Path(__file__).parent.absolute()) + directories.get(dir_name)
	return None
