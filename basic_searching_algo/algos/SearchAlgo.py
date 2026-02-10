class BinarySearch:
    def binearySerach(self, arr:list, tar:int):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid -1

        return -1 # didnt find





if __name__ == "__main__":
    list = [11,22,33,44,55,66,99,109,555]
    target = 66

    bs = BinarySearch()
    result = bs.binearySerach(list,target)
    print(result)




















