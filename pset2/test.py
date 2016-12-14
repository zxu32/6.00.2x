from pset2.ps2 import StandardRobot, RectangularRoom, runSimulation
from pset2.ps2_visualize import RobotVisualization

# env = RobotVisualization(0, 100, 100)

room1 = RectangularRoom(10, 10)
bot1 = StandardRobot(room1, 1)

print(runSimulation(5, 1, 10, 10, 0.8, 5, StandardRobot))


# import tkinter
#
# top = tkinter.Tcl()
# bot = tkinter.Tk()
# # top.mainloop()
