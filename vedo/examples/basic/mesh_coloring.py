"""Specify a colors for cells
and points of a Mesh"""
from vedo import *

##################################### addCellArray
man1 = load(datadir+"man_low.vtk").lineWidth(0.1)
nv = man1.NCells()                         # nr. of cells
scals = range(nv)                          # coloring by the index of cell

man1.addCellArray(scals, "mycellscalars")  # add an array of scalars to mesh
#print(man1.getCellArray('mycellscalars')) # it can be retrieved this way
show(man1, __doc__, at=0, N=3, axes=4, elevation=-60)


##################################### Point coloring
man2 = load(datadir+"man_low.vtk")
scals = man2.points()[:, 0] + 37           # pick x coordinates of vertices

man2.cmap("hot", scals, vmax=37)
man2.addScalarBar(horizontal=True)
show(man2, "mesh.cmap()", at=1)


##################################### Cell coloring
man3 = load(datadir+"man_low.vtk")
scals = man3.cellCenters()[:, 0] + 37      # pick x coordinates of cells
man3.cmap("afmhot", scals, mode='cells')

# add a fancier 3D scalar bar embedded in the scene
man3.addScalarBar3D(sy=3).rotateX(90).y(0.2)
show(man3, "mesh.cmap(mode='cells')", at=2, zoom=1.2, interactive=True)
