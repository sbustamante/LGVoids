#Halos_Lambda_File.py
#
#This code produces a file with the respective eigenvalues for each halo
#
#Usage: Halos_Lambda_File.py
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

#==================================================================================================
#			CONSTRUCTING FILES WITH HALOS ENVIRONMENT
#==================================================================================================    

#Loading Eigenvalues Vweb filename
eig_filename = '%s%s%s/%d/Eigen%s'%(foldglobal,simulation,web,N_sec,smooth)
#Loading All properties of Halos
halos = np.transpose(np.loadtxt('%s%s/C_GH_%s.dat'%(foldglobal,simulation,catalog)))
Nhalos = len(halos[0])

#Loading eigenvalues
eig1 = read_CIC_scalar( eig_filename+"_1" )
eig2 = read_CIC_scalar( eig_filename+"_2" )
eig3 = read_CIC_scalar( eig_filename+"_3" )

#Openning file
f = open( '%s%s%s/%d/E_GH%s_%s.dat'%(foldglobal,simulation,web,N_sec,smooth,catalog), "w")
for ih in xrange(Nhalos):
    i = abs(int(np.floor(N_sec*(halos[1,ih]-1e-5)/Box_L)))
    j = abs(int(np.floor(N_sec*(halos[2,ih]-1e-5)/Box_L)))
    k = abs(int(np.floor(N_sec*(halos[3,ih]-1e-5)/Box_L)))
    f.write( "%d\t%1.5e\t%1.5e\t%1.5e\t%d\t%d\t%d\n"%( halos[0,ih], eig1[i,j,k], eig2[i,j,k], eig3[i,j,k], i, j, k ) )
    
f.close()