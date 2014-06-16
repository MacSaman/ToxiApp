from mod_python import apache

def index(req, DNA=""):
    DNAseq = getDNA(DNA)
    req.content_type = 'text/html'
    req.write("<body bgcolor=yellow;>")
    req.write ("<b> Van DNA naar eiwitsequentie </b>")
    req.write("<form>")
    req.write ("<table border=10>")
    req.write ("<form action=http://cytosine.nl/~owe4_pg5/afvinkopdracht 2.py>")
    req.write("<tr>")
    req.write("<td>De DNA sequentie:</td>")
    req.write("<td><input type=text name=DNA></td>")
    req.write("</tr>")
    req.write("<tr>")
    req.write("<td>De Eiwitsequentie:</td>")
    req.write("<td>"+DNAseq+"</td>")            
    req.write("</tr>")
    req.write("</table>")
    req.write("<input type=submit>")
    req.write("</form>")
    req.write("</body>")      
      
def getDNA(DNA):
    code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
        'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
        'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
        'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
        'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
        'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
        'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
        'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',     
        'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
        'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
        'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
        'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R', 
        'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
        'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
        'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
        'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}
    lijst = []
    codon = ""
    teller = 0
    AA = ""
    for nucleotide in DNA:
        teller += 1
        if teller == 1:
            codon += nucleotide
        elif teller == 2:
            codon += nucleotide
        elif teller == 3:
            codon += nucleotide
            lijst.append(codon)
            teller = 0
            codon = ""
    for i in lijst:
        AA += code[i]

    return(AA)

