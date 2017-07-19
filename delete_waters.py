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
    lig1_waters = "lig1_waters"
    lig2_waters = "lig2_waters"
    waters_to_delete = "waters_far_" + ligand_name
    
    # select the correct water atoms
    cmd.select(lig1_waters, ligand1_location + " around 4 and hetatm")
    cmd.select(lig2_waters, ligand2_location + " around 4 and hetatm")
    cmd.select(waters_to_delete, "hetatm and not " + lig1_waters + " and not " + lig2_waters + " and not " + ligand1_location + " and not " + ligand2_location)
    
    # delete the water atoms that are far from the ligand(s)
    cmd.remove(waters_to_delete)
    
    # show remaining waters as spheres and ligands as sticks
    cmd.show_as("spheres", lig1_waters)
    cmd.show_as("spheres", lig2_waters)
    cmd.show_as("sticks", ligand1_location)
    cmd.show_as("sticks", ligand2_location)
    
    # remove selection
    cmd.delete(waters_to_delete)

# let pymol know about this function
cmd.extend("delete_waters", delete_waters)