#!/usr/bin/env python  
# coding=utf-8


def mountain_find(num_data):
    # 单数字区间，传入的num_data为data的数组索引号
    left_len = -2  # 设-2为NULL
    right_len = -2  
    # 左区间长度判断
    for left_i in xrange(1, num_data + 1):
        if data[num_data - left_i + 1] > data[num_data - left_i]:
            continue
        else:
            left_len = left_i - 1
            break
    if left_i == num_data:
        left_len = left_i
    # 右区间长度判断
    for right_i in xrange(num_data + 1, n):
        if data[right_i - 1] > data[right_i]:
            continue
        else:
            right_len = right_i - num_data - 1
            break
    if right_i == n-1:
        right_len = right_i - num_data
    # 返回结果字典
    return {'num_data': num_data, 'left_len': left_len, 'right_len': right_len}


n = 10
data = [1, 3, 2, 9, 7, 6, 4, 10, 5, 4]  
# n = int(raw_input()) # 数组长度输入
# data = map(int, raw_input().split(' ')) # 数组内容输入
final_dict = {'right_len': -2, 'left_len': -2, 'num_data': -2}
for i in xrange(1, n-1):
    temp_dict = mountain_find(i)
    if temp_dict.get('left_len') > 0 and temp_dict.get('right_len') > 0:
        new_len = temp_dict.get('left_len') + temp_dict.get('right_len')
        old_len = final_dict.get('left_len') + final_dict.get('right_len')
        if new_len > old_len:
            final_dict = temp_dict
left_flag = final_dict.get('num_data') - final_dict.get('left_len')
right_flag = final_dict.get('num_data') + final_dict.get('right_len')
print left_flag, right_flag