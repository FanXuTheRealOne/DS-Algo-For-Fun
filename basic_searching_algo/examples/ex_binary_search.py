from basic_searching_algo.algos import SearchAlgo
import math
if __name__ == "__main__":

    list = [1,2,3,4,5,6,7,8,888,8889]
    target = 8889

    s = SearchAlgo.BinarySearch()


    output = s.binary_search(list,target)

    if output == -1:
        print("Not found")
    else:
        print(f"found {target} at {output}")

        ##

##







