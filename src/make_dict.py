"""Creates a dictionary given fastalign's outputs
Author: Antonios Anastasopoulos <aanastas@andrew.cmu.edu>
"""
import argparse
from collections import Counter
import string

def align(textfile, alignmentfile, l1, l2, N):

	outputfile=f"dict.{l1}-{l2}"

	# Read the text and the alignment files
	with open(textfile, mode='r', encoding='utf-8') as inp:
		lines = inp.readlines()
	with open(alignmentfile, mode='r') as inp:
		allines = inp.readlines()

	assert(len(lines) == len(allines))

	# Get counts over aligned word pairs
	d = {}
	allwords = {}
	for line, al in zip(lines[:N], allines[:N]):
		try:
			sents = line.strip().lower().split('|||')
			leftside = sents[0].strip().split()
			rightside = sents[1].strip().split()
			als = [(int(k.split('-')[0]), int(k.split('-')[1])) for k in al.strip().split()]
			for i,j in als:
				if leftside[i] in d:
					if rightside[j] in d[leftside[i]]:
						d[leftside[i]][rightside[j]] += 1
					else:
						d[leftside[i]][rightside[j]] = 1
				else:
					d[leftside[i]] = {}
					d[leftside[i]][rightside[j]] = 1
			for w in leftside:
				if w in allwords:
					allwords[w] += 1
				else:
					allwords[w] = 1
		except:
			pass

	# Allow different alignment probability thresholds for different word-pair occurence counts
	# TODO(): This should probably be tuned to the smaller amount of data we have
	count_thresholds = [20, 5, 2]
	prob_thresholds = [0.5, 0.6, 0.9]

	# Write out the word pairs with probabilities above the thresholds
	with open(f"{outputfile}.txt", 'w') as outall:
		N = len(allwords)
		print(N)
		#N = 40
		counter = Counter(allwords)
		for word, count in counter.most_common(N):
			if word in d and (not any(c in string.punctuation for c in word)):
				for trans in d[word]:
					if trans and (not any(c in string.punctuation for c in trans)):
						for c_t,p_t in zip(count_thresholds,prob_thresholds):
							if count > c_t:
								if d[word][trans] >= p_t * count:
									outall.write(f"{word}\t{trans}\n")
								break





if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "-input_dir", help="input text", type=str)
	parser.add_argument("-a", "-alignment", help="input alignment", type=str)
	parser.add_argument("-l1", "-l1", help="l1", type=str)
	parser.add_argument("-l2", "-l2", help="l2 file", type=str)
	parser.add_argument("-n", "-number", default=1000000, help="number of lines to use", type=int)
	args = parser.parse_args()

	align(args.i, args.a, args.l1, args.l2, args.n)

