#!/usr/bin/python
# find and delete water molecules that are not within 6 angstroms of a ligand atom
# assumes ligand is the only residue in chain X.

from pymol import cmd

# fill in some information
resfile_path = "/Users/anumglasgow/Dropbox/Research/Structures/transcription_factor/lacI/"
ligand_name = "IPTG"
ligand1_location = "resi 998"
ligand2_location = "resi 999"

# pymol function to find and delete the water molecules
def delete_waters():
    near_waters = "waters_near_" + ligand_name
    waters_to_delete = "waters_far_" + ligand_name
    
    # select the correct water atoms
    cmd.select(near_waters, ligand1_location + " around 5 or " + ligand2_location + " around 5")
    cmd.select(waters_to_delete, "hetatm and not " + near_waters + " and not " + ligand2_location)
    
    # delete the water atoms that are far from the ligand(s)
    cmd.remove(waters_to_delete)
    
    # remove selection
    cmd.delete(waters_to_delete)

# let pymol know about this function
cmd.extend("delete_waters", delete_waters)