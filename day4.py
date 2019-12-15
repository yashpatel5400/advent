start = 125730
end = 579381
total_valid = 0
for num in range(start, end + 1):
    str_num = str(num)
    max_val = -1

    is_valid = True
    found_double = False
    
    repeat_len = 1
    for i, c in enumerate(str_num):
        if int(c) < max_val:
            is_valid = False
        else:
            max_val = int(c)
        
        if i > 0:
            if str_num[i] == str_num[i-1]:
                repeat_len += 1
            else:
                if repeat_len == 2:
                    found_double = True
                repeat_len = 1
    if repeat_len == 2:
        found_double = True
    if is_valid and found_double:
        total_valid += 1
print(total_valid)