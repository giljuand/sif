import time

class SifGenerator:
    def __init__(self):
        self.db = [[()],[(1,)],[(2,1)]]

    def return_all_sif(self,n):
        """
        Generates all SIF permutations of length n and returns as a list of tuples.
        """
        if len(self.db)>n:     # already stored in database
            return self.db[n].copy()
        elif len(self.db)<n:   # needs to generate smaller SIF
            self.return_all_sif(n-1)
        
        sif_list = []

        # generate SIF by adding n in some (n-1) length SIF
        for i in range(n-1):
            for base_sif in self.db[n-1]:
                new_sif = list(base_sif)
                new_sif.append(base_sif[i])
                new_sif[i]=n
                sif_list.append(tuple(new_sif))

        # generate SIF by combining two smaller SIF permutations, tau and rho
        for j in range(2,n-1):    # size of SIF component tau
            for k in range(1, j): # starting index of SIF component rho
                for sif1 in self.db[n-j]: # SIF permutation rho
                    for sif2 in self.db[j]: #SIF permutation tau
                        rho = list(sif1) 
                        tau = list(sif2)
                        
                        rho_labels = list(range(k+1, n-j+k))
                        rho_labels.append(n)
                        tau_labels = list(range(1,k+1))
                        tau_labels = tau_labels + list(range(n-j+k,n))

                        rho = self._label_perm(rho, rho_labels)
                        tau = self._label_perm(tau, tau_labels)
                        new_sif = self._combine_perms(rho, rho_labels,
                                                      tau, tau_labels, n)
                        sif_list.append(tuple(new_sif))
        
        self.db.append(sif_list)
        return self.db[n].copy()


    def _label_perm(self, perm, label):
        labelled_perm = []
        for i in range(len(perm)):
            labelled_perm.append(label[perm[i]-1])
        return labelled_perm

    def _combine_perms(self, rho, rho_labels, tau, tau_labels, n):
        new_sif = []
        rho_index = 0
        tau_index = 0
        while len(new_sif)<n:
            if rho_labels[rho_index] == len(new_sif)+1:
                new_sif.append(rho[rho_index])
                rho_index += 1
            else:
                new_sif.append(tau[tau_index])
                tau_index += 1
        return new_sif
        
if __name__ == "__main__":        
    g = SifGenerator()
    for n in range(0,11):
        t=time.time()
        print("n="+ str(n) + ":",len(g.return_all_sif(n)), "("+str(time.time()-t)+"s)")
