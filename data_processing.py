
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def process_file(lines):
	clean_lines=[convert_line(line) for line in lines]
	print clean_lines

def convert_line(line):
	clean_lines = []
	values = line.strip().split(',')
	return[
		float(values[1]),
		float(values[2]),
		float(values[3]),
		float(values[4]),
		values[0],
		int(values[5]),
	]


def main():
	with open('nke.txt', 'r') as f:
		content = f.readlines()
		process_file(content)


if __name__== "__main__":
	main()