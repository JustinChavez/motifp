from __future__ import division
import math
from decimal import *

#Starting here is what I imported to get the protein sequence
from Bio import Entrez
from Bio import SeqIO
Entrez.email = "nickyesupriya@hotmail.com"

#this list holds the gene id for what we are quering with
id_list = ['77462544']
handle = Entrez.efetch(db="protein", id=id_list, rettype="fasta", retmode="text")   
#the following are just extra details that I took out since they are not relevant

#for seq_record in SeqIO.parse(handle, "fasta"):
 #   print ">" + seq_record.id, seq_record.description
#print seq_record.seq
handle.close()


result_handle = open("my_blast.out")

#seq_record.seq holds the protein sequence, q_length will take the length of 
#that to find query length, I placed it between the two print statements so
#you can verify that the length is the actual length
q_length = len(seq_record.seq)
print "####################"
print str(q_length)
print "####################"

from Bio.Blast import NCBIXML
#Parses for multiple query sequences
blast_record = NCBIXML.read(result_handle)

file_name = open("blast_eval.txt", "w")
seq_hits = []

E_VALUE_THRESH = (10 ** -10)
count = 0
for alignment in blast_record.alignments:
	for hsp in alignment.hsps:
            
            if (hsp.expect < E_VALUE_THRESH) and (((hsp.query_end - hsp.query_start)/q_length) > .9): 
                  
                  count += 1
                  
                  print alignment.title	
                  print "e value:" + str(hsp.expect) 
                  print "identity:" + str(Decimal(hsp.identities) / Decimal(alignment.length))
                  print "strand" + str(hsp.strand)
#                  print "bits" + str(hsp.bits)
#                  print "num_align" + str(hsp.num_alignments)
#                  print "positives" + str(hsp.positives)
#                  print "gaps" + str(hsp.gaps)
                  print "query" + str(hsp.query)
                  print "query_start" + str(hsp.query_start)
                  print "query_end" + str(hsp.query_end)
#                  print "sbkct_start" + str(hsp.sbjct_start)
#                  print "frame" + str(hsp.frame)
#                  print "score:" + str(hsp.score)+ "\n"
                  print "query length: " + str(len(hsp.query))
                  print ""
                  print ""
                  print ""
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
                  
                  
print "total number of matches recieved is: " + str(count)