def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            post = pos+1

        return found


# If the item is not in the list, the only way to know it is to compare it against every item present.
# seq search without ordering = O(n)

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos+1

    return found

# In summary, a sequential search is improved by ordering the list only in the case where we do not find the item.
