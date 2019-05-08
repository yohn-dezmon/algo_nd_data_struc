import random


class Hashtable(object):

    def __init__(self, size):
        self.initial_list = []
        self.size = size

    def create_table(self):
        for i in range(self.size):
            self.initial_list.append(None)
        return self.initial_list

    def fold_method_hash_func(self, elementy):
        nstr = str(elementy)
        nint = [int(n) for n in nstr]

        # I want to make a for loop that only accesses the even and/or odd values
        for indx, val in enumerate(nint):
            plus1 = indx + 1
            if plus1 in range(len(nint)):
                nint[indx] = str(nint[indx]) + str(nint[plus1])
                del nint[plus1]

        nint = [int(i) for i in nint]

        # now that we have the two digit pairs, we can sum them
        hash_val = sum(nint) % self.size

        return hash_val


    def insert_into_table(self, list1):
        """ list1 can be a list or a single item """
        for i in list1:
            hash_val = self.fold_method_hash_func(i)

            # here I am inserting the values into the hashtable while using collision control
            while self.initial_list[hash_val] != None:
                hash_val = (hash_val + 3) % self.size

            self.initial_list[hash_val] = i


        return self.initial_list

    def search_table(self, numbrr):
        hash_value = self.fold_method_hash_func(numbrr)
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
h.search_table(22)
