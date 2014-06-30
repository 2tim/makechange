__author__ = 'Kevin Evans'

def makechange(amount, denom=10, text=""):
    """

    :param amount:money left to divide
    :param denom: dimes, nickels, quarters

    This is my attempt to solve the problem of determining all the unique
    combinations of making change from any amount of money and giving the
    total number of combinations. It uses recursion instead of an iterative
    approach so that the number of denomination could be expanded.

    A string is used to keep track of the unique branches instead of a
    matrix to make it unique in its implementation.
    """
    global count
    denoms = [10, 5, 1]
    if amount < 1:
        return
    if denom == 1:
        print text + str(amount) + " for denom " + str(denom) + " in " + str(amount)
        text = ""
        count += 1
        return
    #using xrange instead of range for faster python 2.7 performance
    #warning: doesn't work in python 3.
    for i in xrange(amount / denom, -1, -1):
        temptext = str(i) + " for denom " + str(denom) + " in " + str(amount) + ", "
        text += temptext
        if amount - i * denom > 0:
            makechange(amount - i * denom, denoms[denoms.index(denom) + 1], text)
        else:
            count += 1
        if text.endswith(temptext):
            #shorthand for removing n characters from the end of a string
            text = text[:-(len(temptext))]

count = 0
makechange(31, denom=10)
print str(count) + " unique combinations"