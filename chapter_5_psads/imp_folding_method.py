import random

# My implementation of a Hashtable class from scratch. 
# this implementation utilizes the folding method of calculating hash values 
# in order to minimize collisions and to evenly divide the numbers given 

class Hashtable(object):

    def __init__(self, size):
        # we utilize a list data structure to contain the hashtable
        self.initial_list = []
        # size of the hashtable, should be a prime to guarantee all spots get checked
        self.size = size

    def create_table(self):
        """ The hashtable is initialized with each slot equal to None for further insertion/comparison """
        for i in range(self.size):
            self.initial_list.append(None)
        return self.initial_list

    def fold_method_hash_func(self, elementy):
        """ This function computes the hash function for each value provided as the 'elementy' parameter """
        # First I convert the number into a string, utilizing the fact that each string in python is a list of individual characters 
        nstr = str(elementy)
        # here I use a list comprehension to convert each string into an integer, now we have a list of integers
        nint = [int(n) for n in nstr]

        # enumerate allows us to access the index and value at that index for each element of the list
        for indx, val in enumerate(nint):
            plus1 = indx + 1
            if plus1 in range(len(nint)):
                # this part of the function takes the nth element and concatenates it to the n + 1 element
                # e.g. [1,2] >> '1' + '2' >> ['12'] 
                nint[indx] = str(nint[indx]) + str(nint[plus1])
                del nint[plus1]
        # convert the double digit strings back to integers, we now have a list of double digit integers 
        nint = [int(i) for i in nint]

        # now that we have the two digit pairs, we can sum them
        hash_val = sum(nint) % self.size

        return hash_val


    def insert_into_table(self, list1):
        """ This inserts a list containing multiple values into a hashtable """
        for i in list1:
            hash_val = self.fold_method_hash_func(i)

            # here I am inserting the values into the hashtable while utilizing collision control
            # currently, the slots will be overwritten if there are more elements inserted than there are spaces in the hashtable
            while self.initial_list[hash_val] != None:
                hash_val = (hash_val + 3) % self.size

            self.initial_list[hash_val] = i


        return self.initial_list

    def search_table(self, numbrr):
        """ search table for a given value, numbrr """
        hash_value = self.fold_method_hash_func(numbrr)
        
        # the loggin_var ensures that all slots in the hashtable are checked
        logging_var = 0

        while ((numbrr != self.initial_list[hash_value]) and (logging_var <= self.size)):
            hash_value = (hash_value + 3) % self.size
            logging_var += 1

        if logging_var == 12:
            print("The item is not in the list")


        elif self.initial_list[hash_value] == numbrr:
            print(f"Your item is in the table at position: {hash_value}!!!")







# my_randoms = random.sample(range(10000,50000), 10)
my_randoms = [38587, 38457, 48617, 40427, 13684, 35622, 29950, 46556, 28378, 20106]
print(my_randoms)

h = Hashtable(11)
h.create_table()
h.insert_into_table(my_randoms)
print(h.initial_list)
h.search_table(38587)
