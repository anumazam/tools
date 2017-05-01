#!/usr/bin/python
# generate a resfile for first-shell residues (6 angstroms) around a ligand bound to a protein structure.
# assumes ligand is the only residue in chain X.

from pymol import cmd,stored
resfile_path = "/Users/anum/Dropbox/Research/Structures/transcription_factor/lacI/20170501_coupledmoves_LacI_ONPF/"
ligand_name = "NPF"

def first_shell_res( userSelection ):
    stored.FSresidues = []

    userSelection = userSelection + " and n. c+o+n+ca"
    cmd.iterate(userSelection, "stored.FSresidues.append( (resi, resn) )")
    print stored.FSresidues
    
    list_FSresidues = "\n".join(str(x) for x in stored.FSresidues )
    
    filename = ligand_name + ".res"

    f = open(resfile_path + filename, "w+")
    f.write("NATRO \nSTART \n" + list_FSresidues)
    f.close


# let pymol know about this function
cmd.extend("first_shell_res", first_shell_res)