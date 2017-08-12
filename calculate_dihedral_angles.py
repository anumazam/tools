#!/usr/bin/python
# calculate differences in dihedral angles between two structures

from pymol import cmd

# PDB names
structure1 = "2p9h_IPTG"
structure2 = "2p9h_ONPF"
residues_structure1 = []
residues_structure2 = []
phi_structure1 = []
phi_structure2 = []
psi_structure1 = []
psi_structure2 = []

# pymol function to find and store phi/psi angles
def calculate_phi_psi():
    cmd.phi_psi(structure1)
    cmd.phi_psi(structure2)

# let pymol know about this function
cmd.extend("calculate_phi_psi", calculate_phi_psi)
