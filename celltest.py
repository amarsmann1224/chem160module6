from ising_class import *
acell=cell(3,3,10)
print(acell.cellspin())
acell.spin.flip()
print(acell.cellspin())
print(acell.left)
print(acell.right)
print(acell.up)
print(acell.down)
