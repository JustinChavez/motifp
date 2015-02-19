from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


f_record = next(SeqIO.parse('total_fasta.fasta', 'fasta'))

print ('Performing Blast')
result_handle = NCBIWWW.qblast("blastp", "nr", f_record.format('fasta'))

save_file = open("my_blast.out", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()

