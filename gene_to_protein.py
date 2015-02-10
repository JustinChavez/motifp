#input: list of gene id's
#output: list of protein id's
def gene_to_protein(geneid):
    #this list will contain the protein id's at the end
    proteinList = []    
    
    #will loop through each gene id in the list
    for gene in geneid:
        
        #converts gene id into string incase integer is used
        gene = str(gene)
        
        #code from Nikhil
        from Bio import Entrez
        Entrez.email = "nickyesupriya@hotmail.com"
        handle = Entrez.efetch(db="gene", id=gene, rettype="null", retmode="asn.1")
        output = (handle.read())
        
        #flag needed because only the first protein id is what we want
        flag = False
    
        #split each line into a list so that it can be iterated
        outputList = output.splitlines()
        for line in outputList:
        
            #this will find the line that contains the keyword "products"
            if ("products" in line) and (flag == False):
    
                #it is the fourth line down that will contain the protein id
                proteinid = outputList[outputList.index(line) + 4]
                
                #the following will strip the line so that only the id 
                #remains
                proteinid = proteinid.replace(" ", "")
                proteinid = proteinid.replace("accession", "")
                proteinid = proteinid.replace('"',"" )
                proteinid = proteinid.replace(",", "")
               
                #will now indicate we have take the protein id out                
                flag = True
                
        #places protein id in a lsit that will be returned in the end
        proteinList.append(proteinid)
        
    return proteinList

#this tests out the function, preexisting geneid's are hardcoded into the
#variable geneidList
def main():
    geneidList = [3719330, 949794, 879875]
    proteinidList = gene_to_protein(geneidList)
    
    print proteinidList
main()

    
