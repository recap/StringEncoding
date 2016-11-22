import sys
import struct
import re
import os

class StringEncoding:

	def decode(self, s):
		decoded_string = ""
		i = 0
		for i in range(0, len(s), 2):
			if(s[i] == 0x00):
				# check valid ascii char
				if(s[i+1] > 32) and (s[i+1] < 127):
					decoded_string += chr(s[i+1])
				else:
					decoded_string += "\3F"
			else:
				start_index = len(decoded_string) - s[i]
				end_index = start_index + s[i+1]
				if((s[i] > len(decoded_string)) or (end_index > len(decoded_string))):
					decoded_string += "\3F"
				else:
					decoded_string += decoded_string[start_index:end_index]

		return decoded_string

	def repetitions(self, s):
	   r = re.compile(r"(.+?)\1+")
	   for match in r.finditer(s):
	       yield (match.group(1), len(match.group(0))/len(match.group(1)))

	def encode(self, s, trivial=True):
		byte_stream = []
		repeat_dict = {}
		position_dict = {}
		
		if(trivial):
			for c in s:
				byte_stream.append(0x0)
				byte_stream.append(ord(c))

		else:
			# ran out of time. the basic idea is to get the repetitions which I do here. Then start from the longest
			# repetition and substitute the repetitions excpet the first one with indecies. Next check if the smaller
			# repetitions are substrings of the larger repetition in which case ignore, else do the same procedure of
			# substitution.	
			byte_stream = list(self.repetitions(s))
			#for r in list(repetitions(l)):
			#	a = [m.start() for m in re.finditer(r[0], l)]
			#	#repeat_dict[r[0]] = (a[0], len[r[0]])				
			#	repeat_dict[r[0]] = a[0]
			#	a.pop(0)
			#	for e in a:
			#		position_dict[e] = r[0]

			#print repeat_dict
			#print position_dict
			

		return byte_stream


