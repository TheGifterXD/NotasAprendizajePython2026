def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]
    range_list = range_of_numbers(start_num, end_num - 1)
    range_list.append(end_num)
    return range_list
