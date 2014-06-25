__author__ = 'kevev'

def makechange(amount, denom=10):
    """

    :param amount:
    :param denom:
    """
    global count
    denoms = [10, 5, 1]
    if amount < 1:
        return
    if denom == 1:
        print  str(amount) + " for denom " + str(denom) + " in " + str(amount)
        count+=1
        return
    for i in xrange(amount / denom, -1, -1):
        print str(i) + " for denom " + str(denom) + " in " + str(amount)
        if amount - i * denom > 0:
            makechange(amount - i * denom, denoms[denoms.index(denom) + 1])
        else:
            count+=1

count = 0
makechange(11, denom=10)
print str(count) + " unique combos"