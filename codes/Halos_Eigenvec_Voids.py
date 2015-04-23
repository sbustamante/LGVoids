#Halos_Eigenvec_Voids.py
#
#This code produces a file with the respective eigenvalues for the closest voids cells of each halo
#
#Usage: run Halos_Eigenvec_Voids.py
#
#by: Sebastian Bustamante

execfile('_Head.py')

#==================================================================================================
#			PARAMETERS
#==================================================================================================
#Simulation
simulation = "BOLSHOI/"
#Box lenght
Box_L = 250
#Number of sections
N_sec = 256
#Smooth parameter
smooth = '_s1'
#Catalog Scheme
catalog = 'FOF'
#Web Scheme
web = 'Tweb'
#Number of neighbours
Nneigh = 5

#==================================================================================================
#			CONSTRUCTING FILES WITH HALOS ENVIRONMENT
#==================================================================================================    

#Eigenvector web filename
eigvec_filename = '%s%s%s/%d/Eigenvec%s'%(foldglobal,simulation,web,N_sec,smooth)
#Loading distances
distances = np.transpose(np.loadtxt('%s%s%s/%d/D_GH%s_%s.dat'%(foldglobal,simulation,web,N_sec,smooth,catalog)))
Ndist = len(distances[0])

#Loading eigenvectors
eig1 = read_CIC_vector( eigvec_filename+"_1" )
eig2 = read_CIC_vector( eigvec_filename+"_2" )
eig3 = read_CIC_vector( eigvec_filename+"_3" )

#Openning file for i-th neighbour
for ingh in xrange(Nneigh):
    f = open( '%s%s%s/%d/EV_D_GH%s_%s_%d.dat'%(foldglobal,simulation,web,N_sec,smooth,catalog,ingh), "w")
    for ih in xrange(Ndist):
	i = distances[ ingh*5+2, ih ]
	j = distances[ ingh*5+3, ih ]
	k = distances[ ingh*5+4, ih ]
	f.write( "%1.5e\t%1.5e\t%1.5e\t%1.5e\t%1.5e\t%1.5e\t%1.5e\t%1.5e\t%1.5e\n"%(
	eig1[0,i,j,k], eig1[1,i,j,k], eig1[2,i,j,k],
	eig2[0,i,j,k], eig2[1,i,j,k], eig2[2,i,j,k],
	eig3[0,i,j,k], eig3[1,i,j,k], eig3[2,i,j,k],) )
	
    f.close()