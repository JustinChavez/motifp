from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

#be sure first line of the file is not empty or each fasta paragraph
#is only separated by one line!!!!
fasta_file = open("LexA_fasta.txt")
i=0
fasta_list = []
flag = 0
count = 0
temp = ""
read = False
#iterate through each line of the file
for line in fasta_file:
    
   #indicates the start of a new paragraph in the file
    if line[0:3] == ">gi":
        
        #ensures we don't append when there is nothing there
        if read == True:        
            flag == 0
            fasta_list.append(temp)
            count += 1
        temp = line
        read = True
        flag = 1
    #this indicates we are still reading the paragraph into the variable    
    if flag == 1:
        temp += line
    
    
print "there are: " + str(count) + "fasta in the list"
print fasta_list
            

#f_record = next(SeqIO.parse('prot_fasta.txt', 'fasta'))
#
#print ('Performing Blast')
#result_handle = NCBIWWW.qblast("blastp", "nr", f_record.format('fasta'))
#
#save_file = open("my_blast.out", "w")
#save_file.write(result_handle.read())
#save_file.close()
#result_handle.close()

