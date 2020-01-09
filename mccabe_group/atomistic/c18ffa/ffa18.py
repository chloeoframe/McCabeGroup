import mbuild as mb
class ffa18(mb.Compound):
    def __init__(self, use_atom_name=True):
        super(ffa18,self).__init__()
        if use_atom_name:
            mb.load('ffa18_new.mol2', compound=self, 
                    relative_to_module=self.__module__,
                    infer_hierarchy=False)
        else:
            mb.load('ffa18.mol2', compound=self, relative_to_module=self.__module__,
                    infer_hierarchy=False)

        self.children[0].charge = 0.44
        self.children[1].charge = -0.61
        self.children[2].charge = -0.55
        self.children[3].charge = 0.75
        self.children[4].charge = -0.21
        self.children[5].charge = 0.09
        self.children[6].charge = 0.09
        self.children[7].charge = -0.18
        self.children[8].charge = 0.09
        self.children[9].charge = 0.09
        self.children[10].charge = -0.18
        self.children[11].charge = 0.09
        self.children[12].charge = 0.09
        self.children[13].charge = -0.18
        self.children[14].charge = 0.09
        self.children[15].charge = 0.09
        self.children[16].charge = -0.18
        self.children[17].charge = 0.09
        self.children[18].charge = 0.09
        self.children[19].charge = -0.18
        self.children[20].charge = 0.09
        self.children[21].charge = 0.09
        self.children[22].charge = -0.18
        self.children[23].charge = 0.09
        self.children[24].charge = 0.09
        self.children[25].charge = -0.18
        self.children[26].charge = 0.09
        self.children[27].charge = 0.09
        self.children[28].charge = -0.18
        self.children[29].charge = 0.09
        self.children[30].charge = 0.09
        self.children[31].charge = -0.18
        self.children[32].charge = 0.09
        self.children[33].charge = 0.09
        self.children[34].charge = -0.18
        self.children[35].charge = 0.09
        self.children[36].charge = 0.09
        self.children[37].charge = -0.18
        self.children[38].charge = 0.09
        self.children[39].charge = 0.09
        self.children[40].charge = -0.18
        self.children[41].charge = 0.09
        self.children[42].charge = 0.09
        self.children[43].charge = -0.18
        self.children[44].charge = 0.09
        self.children[45].charge = 0.09
        self.children[46].charge = -0.18
        self.children[47].charge = 0.09
        self.children[48].charge = 0.09
        self.children[49].charge = -0.18
        self.children[50].charge = 0.09
        self.children[51].charge = 0.09
        self.children[52].charge = -0.27
        self.children[53].charge = 0.09
        self.children[54].charge = 0.09
        self.children[55].charge = 0.09
