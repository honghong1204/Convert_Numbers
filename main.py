import cn2an

cn_digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
            '十': 10, '百': 100, '千': 1000, "萬": 10000}
trad_num = {'壹': 1, '貳': 2, '參': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
            '十': 10, '百': 100, '千': 1000, "萬": 10000}
cn_digit_pure = [, '一', '二', '三', '四', '五', '六', '七', '八', '九']
arab_digit_pure = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def trad_num_to_simp_num(to_change):



def list_to_string(inputed_list):
    # inputed_list = trad_num_to_simp_num(inputed_list)
    return "".join(inputed_list)


def chn_to_arabic(string_to_translate):
    return cn2an.cn2an(string_to_translate, "smart")


inputed_string = "被告持有新臺幣三千元整及新臺幣2千元整"
listed_inputed_string = list(inputed_string)
record_i = 0
new_list = []
i = 0
z = 0
while z == 0:
    i += 1
    j = 0
    # print(listed_inputed_string, "TOP")
    if listed_inputed_string[i] == "元":
        while cn_digit.__contains__(listed_inputed_string[i - 1]) or arab_digit_pure.__contains__(
                listed_inputed_string[i - 1]) or trad_num.__contains__(listed_inputed_string[i - 1]):
            if j == 0:
                record_i = i
            j = 1
            i = i - 1
        for k in range(i, record_i, 1):
            # print("k=", k, "recordI =", record_i)
            new_list.append(listed_inputed_string[k])
            # print(new_list, "A")
        new_string = list_to_string(new_list)
        del listed_inputed_string[i:record_i]
        listed_inputed_string.insert(i, str(chn_to_arabic(new_string)))  # 本行置入要代換的字元，即中文換數字的部分
        i = i + 1
        new_list = []

    # print("i=", i, "len(listed)=", len(listed_inputed_string))
    if i == len(listed_inputed_string) - 1:
        break
final_string = list_to_string(listed_inputed_string)
print(final_string)
