# /usr/bin/env python3

import glob
import re
import sys


def getDefinedSprites():
	definedSprites = set()
	guifiles = glob.glob("./*.gfx")
	for f in guifiles:
		# print(f)
		with open(f, encoding='cp1252', errors='strict') as h:
			text = h.read()

		for match in re.finditer(r'name\s*=\s+"(\w+)"', text):
			definedSprites.add(match.group(1))
	return definedSprites


if __name__ == '__main__':
	definedSprites = getDefinedSprites()

	try:
		i = sys.argv.index('--ignored-sprites')
		# assume these sprites are externally defined.
		moreDefined = sys.argv[i + 1].split(',')
		definedSprites.update(moreDefined)
	except:
		pass

	hasError = False
	guifiles = glob.glob("./*.gui")
	for f in guifiles:
		# print(f)
		with open(f, encoding='cp1252', errors='strict') as h:
			text = h.read()

		for match in re.finditer(r'spriteType\s*=\s+"(\w+)"', text):
			s = match.group(1)
			if s not in definedSprites:
				print(f"{s} used in {f} is not defined in any .gfx files.", file=sys.stderr)
				hasError = True

	if hasError:
		exit(1)
