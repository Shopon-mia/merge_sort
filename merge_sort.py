def merge_sort(data_list):

    if len(data_list) > 1:
        mid = len(data_list)//2
        left = data_list[:mid]
        right = data_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data_list[k] = left[i]
                i += 1
            else:
                data_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data_list[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    data_list = [4, 7, 1, 3, 8, 5, 2, 6]
    print("Before Merge Sort : ", data_list)
    merge_sort(data_list)
    print("After Merge Sort: ", data_list)
