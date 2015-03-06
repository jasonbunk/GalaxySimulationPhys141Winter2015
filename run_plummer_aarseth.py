import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PlummerGalaxy import PlummerGalaxy

# Settings:

createNewInitialConditions = True

MakePositionsVideo = True
MakeDistributionsVideo = False

galaxyNumPts = 1000


#=================================================================================
if createNewInitialConditions:
	
	# Generate Plummer galaxy
	newGalaxy = PlummerGalaxy()
	newGalaxy.npts = galaxyNumPts
	newGalaxy.R = 1.0
	newGalaxy.timestep = 0.1
	newGalaxy.timemax = 2.0
	newGalaxy.ZeroVelocities_Bool = True
	
	newGalaxy.GenerateInitialConditions(0,0,0)
	newGalaxy.WriteToFile("plummer.data")
	
	print("compiling Aarseth c code...")
	os.system("gcc -o Aarseth/aarseth Aarseth/nbody0-lab.c -lm")
	
	print("Running compiled Aarseth nbody code on Plummer initial conditions file")
	os.system("./Aarseth/aarseth plummer.data")


if MakePositionsVideo or MakeDistributionsVideo:
	
	print("beginning to make plots/video...")	
	
	if MakePositionsVideo:
		MakeVideo(galaxyNumPts, "out_aarseth_npts_"+str()+".data", True)
	if MakeDistributionsVideo:
		MakeVideo(galaxyNumPts, "out_aarseth_npts_"+str()+".data", False)

