# ý tưởng:
"""
{}1{}2{}3{}4{}5{}6{}7{}8{}9
khởi tạo hàm chứa dấu s = [0,0,0,0,0,0,0,0,0]
thực hiện hàm để thay đổi các giá trị trong s với 0 : none , 1 : '-', 2 : '+'
cứ với mỗi sự thay đổi thì có 1 list [123456789] được tạo ra
từ các hàm đó thì xét tổng = 100 hay ko?
nếu = 100 thì in ra còn ko thì tiếp tục tăng giá trị trong s
"""
# hàm tạo ra các list [123456789] có dấu
def get_values(sign):
    v = 0
    values = []
    for i in range(9):
        s = sign[i]
        d = i + 1
        if s == 0:
            if v >= 0:
                v = v * 10 + d
            else:
                v = v * 10 - d
        elif s == 2:
            if v != 0:
                values.append(v)
            v = d
        elif s == 1:
            if v != 0:
                values.append(v)
            v = -d

    values.append(v)
    return values


# 0 : none , 1 : '-', 2 : '+'
# hàm tăng giá trị trong s theo 2 giá trị liên tiếp
def sign_increase(s):
    n = s[0] + 1
    carry_on = 0
    idx = 0

    while idx == 0 or carry_on > 0:
        divider = 2 if idx == 0 else 3
        n += carry_on
        s[idx] = n % divider
        carry_on = n // divider
        idx += 1
        if idx >= len(s):
            break
        n = s[idx]

# hàm in ra kết quả
def to_str(vals):
    s = ""
    for v in vals:
        if v > 0:
            if s:
                s = s + '+' + str(v)
            else:
                s = str(v)
        else:
            s = s + str(v)

    s = s + '=' + str(sum(vals))
    return s

# hàm chính
def sum_to_target(target):
    s = [0] * 9 # khởi tạo hàm chứa dấu
    for i in range(pow(3, 8)*2):
        # s = [0,0,0,0,0,0,0,0,0]
        vals = get_values(s)
        if sum(vals) == target:
            # print(s)
            # print(vals)
            print(to_str(vals))
        sign_increase(s)

sum_to_target(100)
