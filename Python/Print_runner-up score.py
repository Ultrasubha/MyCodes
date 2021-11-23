def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)
    
    arr= remove_values_from_list(arr,maximum)

    maximum = max(arr)
    print(maximum)
