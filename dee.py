#lambads and built in functions

# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable
square2 = lambda num: num * num

# Another lambda
add = lambda a,b: a + b

# Executing the lambdas
print(square2(7))
print(add(3,10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)


####.......making button....................#####
import tkinter as tk##help creat GUI applications##
root = tk.Tk()##creates the root window#
frame = tk.Frame(root)##its like a container##
frame.pack()##the pack method sizes the frame so that all content are preffered size##
def say_hi():
    print("HELLO!")
button = tk.Button(frame, 
                   text="CLICK ME", 
                   fg="red",#foreground colour#
                   command=lambda: print("Hello"))##function that is called whenever button is clicked##
button.pack(side=tk.LEFT) #=========
root.mainloop() #=======                  
