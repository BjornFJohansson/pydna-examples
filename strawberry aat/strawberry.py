from pydna.genbank import Genbank
from pydna.design import cloning_primers
from pydna.amplify import pcr
from pydna.readers import read
from pydna.parsers import parse_primers
from pydna.assembly import Assembly
from pydna.gel import Gel

gb=Genbank("bjornjobb@gmail.com")

saat = gb.nucleotide("AF193791 REGION: 78..1895")

fw, rv = cloning_primers(saat, fp_tail="aa")

fw.id, rv.id = "fw_saat_cds", "rv_saat_cds"

saat_pcr_prod = pcr(fw, rv, saat)

saat_pcr_prod.figure()

pYPKa=read("pYPKa.gb")

from Bio.Restriction import AjiI

pYPKa_AjiI = pYPKa.linearize(AjiI)

pYPKa_A_saat = ( pYPKa_AjiI + saat_pcr_prod ).looped()

pYPKa_Z_prom = read("pYPKa_Z_TEF1.gb")

pYPKa_E_term = read("pYPKa_E_TPI1.gb")

p567,p577,p468,p467,p568,p578  =  parse_primers('''

>567_pCAPsAjiIF (23-mer)
GTcggctgcaggtcactagtgag
>577_crp585-557 (29-mer)
gttctgatcctcgagcatcttaagaattc

>468_pCAPs_release_fw (25-mer)
gtcgaggaacgccaggttgcccact
>467_pCAPs_release_re (31-mer) 
ATTTAAatcctgatgcgtttgtctgcacaga

>568_pCAPsAjiIR (22-mer) 
GTGCcatctgtgcagacaaacg
>578_crp42-70 (29-mer)
gttcttgtctcattgccacattcataagt''')

p = pcr(p577, p567, pYPKa_Z_prom)

g = pcr(p468, p467, pYPKa_A_saat)

t = pcr(p568, p578, pYPKa_E_term)

pYPKpw = read("pYPKpw.gb")

from Bio.Restriction import ZraI

pYPKpw_lin = pYPKpw.linearize(ZraI) 

asm = Assembly( (pYPKpw_lin, p, g, t) )

candidate = asm.circular_products[0]
candidate.figure()

pYPK0_TDH3_FaPDC_TEF1 = candidate.synced(pYPKa)

pYPK0_TDH3_FaPDC_TEF1.write("pYPK0_TDH3_FaPDC_TPI1.gb")