#Marco Sbaffoni - 283934


# EXERCISE 1 #

# Model: Ferrari F430

# EXERCISE 2 #

from pyplasm import *
import scipy
from scipy import *

#import sys
#sys.path.append("/home/marco/CGlib/larpy/larpy")

#from lar import *

#def GRID(args):
#	model = ([[]],[[0]])
#	for k,steps in enumerate(args):
#		model = larExtrude(model,steps*[1])
#	V,cells = model
#	verts = AA(list)(scipy.array(V)/AA(float)(args))
#	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])
#

#dom2D = GRID([5,5])

dom1D = INTERVALS(1)(20)
dom2D = PROD([dom1D,dom1D]) 

leftSideCP = [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[8,0,0],[9,0,2.6],[10,0,2.9],[11,0,3.3],[12,0,2.9],[13,0,2.6],[14,0,0],[14,0,0],[34,0,0],[34,0,0],
[35,0,2.6],[36,0,2.9],[37.5,0,3.6],[39,0,2.9],[40,0,2.6],[41,0,0],[41,0,0],[45,0,2],[45,0,2],[45,0,2],[45,0,2]]
leftSideCP2 = [[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,3],[2,0,3.8],[5,0,4.5],[8,0,5],[9,0,5.6],[11,0,6],[12,0,6],[22,0,11.4],[27,0,12],[32,0,11.4],
[42,0,8],[45,0,8],[45,0,2],[45,0,2],[45,0,2],[45,0,2]]
leftSide = STRUCT([SPLINE(CUBICUBSPLINE(dom1D))(leftSideCP),SPLINE(CUBICUBSPLINE(dom1D))(leftSideCP2)])
rightSide = T(2)(18.72)(leftSide) 

sectionCP = [[0,0.46,1],[0,0.46,1],[0,0.46,1],[0,9,1.3],[0,18.26,1],[0,18.26,1],[0,18.72,5.75],[0,16.26,6.21],[0,13.5,11.4],
[0,12.5,11.4],[0,9.2,12],[0,6.14,11.4],[0,6.14,11.4],[0,3.38,6.21],[0,0.92,5.75],[0,0.46,1],[0,0.46,1],[0,0.46,1]]
section = SPLINE(CUBICUBSPLINE(dom1D))(sectionCP)

middleSide = T(1)(25)(section)

backSide = T(1)(45)(section)

section2CP = [[0,0.46,1],[0,0.46,1],[0,0.46,1],[0,9,1.3],[0,18.26,1],[0,18.26,1],[0,18.72,5.15],[0,16.26,5.21],
[0,3.38,5.21],[0,0.92,5.15],[0,0.46,1],[0,0.46,1],[0,0.46,1]]
section2 = T(1)(8.2)(SPLINE(CUBICUBSPLINE(dom1D))(section2CP))

frontSideCP= [[0,0.46,1],[0,0.46,1],[0,0.46,1],[0,9,1.3],[0,18.26,1],[0,18.26,1],[0,18.72,3.15],[0,16.26,3.21],
[0,3.38,3.21],[0,0.92,3.15],[0,0.46,1],[0,0.46,1],[0,0.46,1]]
frontSide = (SPLINE(CUBICUBSPLINE(dom1D))(frontSideCP))

backSideCP = [[0,0.46,1],[0,0.46,1],[0,0.46,1],[0,9,1.3],[0,18.26,1],[0,18.26,1],[0,18.72,5.75],[0,16.26,6.21],
[0,3.38,6.21],[0,0.92,5.75],[0,0.46,1],[0,0.46,1],[0,0.46,1]]
backSide = T([1,3])([45,2])(SPLINE(CUBICUBSPLINE(dom1D))(backSideCP))

upSideCP = [[8.28,0,5],[8.28,0,5],[8.28,0,5],[9,0,5.6],[11,0,6],[12,0,6],[22,0,11.4],[27,0,12],[32,0,11.4],[42,2,8],[45,3,8],[45,16,8],
[42,16,8],[32,18.4,11.4],[27,18.4,12],[22,18.4,11.4],[12,18.4,6],[11,18.4,6],[9,18.4,5.6],[8.28,18.4,5],[0,9.2,3],[8.28,0,5],[8.28,0,5],[8.28,0,5]]
upSide = SPLINE(CUBICUBSPLINE(dom2D))(upSideCP)
model = T([1,2,3])([-20,-9,-6])(STRUCT([leftSide,rightSide,middleSide,section2,frontSide,backSide,upSide]))
VIEW(model)
