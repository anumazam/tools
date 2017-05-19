#!/usr/bin/python
# find first-shell residues (6 angstroms) around a ligand bound to a protein structure and generate a resfile.
# assumes ligand is the only residue in chain X.

from pymol import cmd,stored
resfile_path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/20170518_coupledmoves/"
ligand_name = "NPF"

def first_shell_res( userSelection ):
    
    stored.FSresidues = []

    userSelection = userSelection + " and n. c+o+n+ca"
    cmd.iterate(userSelection, "stored.FSresidues.append( (resi, resn) )")
    
    list_FSresidues = "\n".join(str(x) for x in stored.FSresidues )
    
    filename = ligand_name + ".res"

    f = open(resfile_path + filename, "w+")
    f.write("NATRO \nSTART \n" + list_FSresidues)
    f.close

def first_shell_select():

    shell_name = "near" + ligand_name
    cmd.select(shell_name, "chain X around 6")

# let pymol know about this function
cmd.extend("first_shell_res", first_shell_res)
cmd.extend("first_shell_select", first_shell_select)