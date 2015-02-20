from __future__ import division
import math
from decimal import *


result_handle = open("my_blast.out")

from Bio.Blast import NCBIXML
#Parses for multiple query sequences
blast_record = NCBIXML.read(result_handle)

file_name = open("blast_eval.txt", "w")
seq_hits = []

E_VALUE_THRESH = (10 ** -10)

for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
		if (hsp.expect < E_VALUE_THRESH) and (Decimal(hsp.identities) / Decimal(alignment.length) > .9): 

			print alignment.title	
			print "e value:" + str(hsp.expect) 
			print "identity:" + str(Decimal(hsp.identities) / Decimal(alignment.length))
			print "strand" + str(hsp.strand)
			print "bits" + str(hsp.bits)
			print "num_align" + str(hsp.num_alignments)
			print "positives" + str(hsp.positives)
			print "gaps" + str(hsp.gaps)
			print "query" + str(hsp.query)
			print "query_start" + str(hsp.query_start)
			print "sbkct_start" + str(hsp.sbjct_start)
			print "frame" + str(hsp.frame)
			print "score:" + str(hsp.score)+ "\n"
				
			

			sequence = alignment.title
			length = alignment.length
			e_value = hsp.expect
			query = hsp.query
			match = hsp.match
			subject = hsp.sbjct
			identity = hsp.identities
			score = hsp.score
			coverage = identity/length

			
			seq_hits = [sequence, length, identity, e_value, score]
			file_name.write(str(seq_hits)+"\n\n")
