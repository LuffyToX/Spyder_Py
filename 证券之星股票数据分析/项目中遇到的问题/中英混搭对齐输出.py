def align_print(string, distance, alignment='left'):
    """ 中英混搭时对齐输出 """

    # 计算出 string 的 'gbk' 码长度
    length = len(string.encode('gbk'))
    if distance > length:
        space_to_fill = distance - length
    else:
        space_to_fill = 0

    if alignment == 'left':
        string = string + ' ' * space_to_fill

    elif alignment == 'right':
        string = ' ' * space_to_fill + string

    elif alignment == 'center':
        string = ' ' * (distance // 2) + string + ' ' * (distance - distance // 2)

    return string


print(align_print('姓名', 20), align_print('电话', 20), align_print('QQ', 20), align_print('邮箱', 20), sep='')

print(align_print('席天亮', 20), align_print('17854264217', 20), align_print('1239112948', 20), align_print('1239112948@qq.com', 20), sep='')

print(align_print('cll', 20), align_print('17854264217', 20), align_print('1239112948', 20), align_print('1239112948@qq.com', 20), sep='')
