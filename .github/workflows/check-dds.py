import glob
import sys

from PIL import Image

if __name__ == '__main__':
	for imageFile in glob.glob("./*.dds"):
		try:
			with Image.open(imageFile, formats=['DDS']) as im:
				if im.format != 'DDS' or im.mode != 'RGBA':
					print(f'{imageFile} is not in DDS 32bit-A8R8G8B8 mode.', file=sys.stderr)
		except:
			print(f'{imageFile} is not in DDS format.', file=sys.stderr)
