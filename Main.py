# main.py


# 1. 导入文件名
import SearchAlgo

# 2. 将执行逻辑放入主程序入口
if __name__ == "__main__":

    list = [1,2,3,4,5,6,7,8,999]
    target =7

    s = SearchAlgo.BinarySearch()
    # 这里因为 binary Search里有self，所以它是一个跟着object的method，必须要new出来一个新的object才用这个

    output = s.binary_search(list,target)

    if output == -1:
        print("Not found")
    else:
        print(f"found {target} at {output}")



