
def open_pdb(f_loc):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_loc) as f:
        data = f.readlines()
    c = []
    sym = []
    for l in data:
        if 'ATOM' in l[0:6] or 'HETATM' in l[0:6]:
            sym.append(l[76:79].strip())
            c2 = [float(x) for x in l[30:55].split()]
            c.append(c2)
    coords = np.array(c)
    return sym, coords

atomic_weights = {
    'H': 1.00784,
    'C': 12.0107,
    'N': 14.0067,
    'O': 15.999,
    'P': 30.973762,
    'F': 18.998403,
    'Cl': 35.453,
    'Br': 79.904,
}


def open_xyz(file_location):
    
    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coords = (xyz_file[:,1:])
    coords = coords.astype(np.float)
    return symbols, coords

def write_xyz(file_location, symbols, coordinates):
    
    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)
    
    with open(file_location, 'w+') as f:
        f.write('{}\n'.format(num_atoms))
        f.write('XYZ file\n')
        
        for i in range(num_atoms):
            f.write('{}\t{}\t{}\t{}\n'.format(symbols[i], 
                                              coordinates[i,0], coordinates[i,1], coordinates[i,2]))
