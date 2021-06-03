# Program to implement NRZ-L and NRZ-I line coding scheme

import matplotlib.pyplot as plt
# matplotlib is imported to plot the graphs in the python


# A function to take data bits as list in parameters and calculate and plot the graph for NRZ-L scheme
def nrzL(inp):

    # inputted data bits is converted as per NRZ-L scheme and stored as list in y
    y = [1 if i == 0 else -1 for i in inp]
    y.append(y[-1])

    # integers to be shown on x-axis is stored as list in x
    x = list(range(0, len(y)))

    # title() function sets the title of the graph as passed string
    plt.title("NRZ-L")

    # xlabel() and ylabel() sets the label of x and y-axis as passed string
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # xlim() and ylim() sets the values to be shown on x and y-axis respectively
    plt.xlim(0, len(y)-1)
    plt.ylim(-3, 3)
    plt.yticks(range(-2, 3))

    # this for loop prints the text(here data bits 0 or 1) in the graph
    for i in range(0, len(y)-1):
        plt.text(i+0.375, 1.375, inp[i], fontsize=17)

    # arrow() is used to draw the arrow in the graph
    plt.arrow(0, 0, len(y)-1.2, 0, color='blue', head_width=0.15, head_length=0.2)

    # step() creates the graph as steps which is required in digital signal
    plt.step(x, y, color='red', where='post')

    # grid() enables the grid in the graph
    plt.grid()

    # show() presents the created graph
    plt.show()


# A function to take data bits as list in parameters and calculate and plot the graph for NRZ-I scheme
def nrzI(inp):

    # inputted data bits is converted as per NRZ-L scheme and stored as list in y
    y = [1]
    temp = 1
    for i in inp[1:]:
        if i == 1:
            temp = (-1 if temp == 1 else 1)
        y.append(temp)
    y.append(y[-1])

    # integers to be shown on x-axis is stored as list in x
    x = list(range(0, len(y)))

    plt.title("NRZ-I")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.xlim(0, len(y) - 1)
    plt.ylim(-3, 3)
    plt.yticks(range(-2, 3))
    for i in range(0, len(y)-1):
        plt.text(i+0.375, 1.375, inp[i], fontsize=17)
    plt.arrow(0, 0, len(y) - 1.2, 0, color='blue', head_width=0.15, head_length=0.2)
    plt.step(x, y, color='red', where='post')
    plt.grid()
    plt.show()


# the following lines operate the working of this program
# it takes input from user and stores data bits as int in list inp
inp = [int(i) for i in input("Enter data bits : ").split()]

# Calling the function nrzL and passing the list of data bits
nrzL(inp)
# Calling the function nrzI and passing the list of data bits
nrzI(inp)
