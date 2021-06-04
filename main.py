import cn2an
import os

cn_digit = {'零':'零','一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
            '十': 10, '百': 100, '千': 1000, "萬": 10000, "億": 100000000, "兆": 1000000000000}
trad_num = {'壹': '一', '貳': '二', '參': '三', '肆': '四', '伍': '五', '陸': '六', '柒': '七', '捌': '八', '玖': '九',
            '拾': '十', '佰': "百", "仟": "千", "萬": "万", "億": "亿", ",": "", "兩": "二"}
cn_digit_pure = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
arab_digit_pure = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
approximate_words = ['多', '數', '餘']


def trad_num_to_simp_num(to_change):
    rep = [trad_num[x] if x in trad_num else x for x in to_change]
    return rep


def list_to_string_A(inputed_list):
    inputed_list = trad_num_to_simp_num(inputed_list)
    string = "".join(inputed_list)
    string = string.replace(",", "")
    string = string.replace(" ", "")
    string = string.replace("万0", '万零')
    string = string.replace("千0", '千零')
    return string


def list_to_string_B(inputed_list):
    inputed_list = trad_num_to_simp_num(inputed_list)
    string = "".join(inputed_list)
    string = string.replace("万", "萬")
    return string


def chn_to_arabic(string_to_translate):
    # print(string_to_translate, "[B]")
    return cn2an.cn2an(string_to_translate, "smart")


def count_files_in_the_folder(DIR):
    return len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])


def fetch_file_list(route):
    dirs = os.listdir(route)
    file_list = []
    for file in dirs:
        file_list.append(file)
    return file_list

route_ = input("input_route:")
# route_ = "C:\\Users\\hongh\\Desktop\\cases\\common"
new_route = route_.replace("\\","\\\\")
file_list = fetch_file_list(new_route)
error_list = []
for now in range(len(file_list)):
    try:
    # for now in range(2):
        f = open(new_route + "\\" + file_list[now], mode="r", encoding="utf-8")
        # f = open("tries.txt", mode="r", encoding="utf-8")
        inputed_string = f.read()
        # w = open("folder/text.txt", mode="w", encoding="utf-8")
        listed_inputed_string = list(inputed_string)
        record_i = 0
        new_list = []
        i = 0
        z = 0
        while z == 0:
            i += 1
            j = 0
            if len(listed_inputed_string) == 0:
                print("NO CONTENT")
                break
            # print(type(listed_inputed_string[i-1]))
            if listed_inputed_string[i] == "元":
                if listed_inputed_string[i - 1] == "\n":
                    del listed_inputed_string[i - 1]
                    i -= 1
                while cn_digit.__contains__(listed_inputed_string[i - 1]) or arab_digit_pure.__contains__(
                        listed_inputed_string[i - 1]) or trad_num.__contains__(listed_inputed_string[i - 1]):
                    if j == 0:
                        record_i = i
                    j = 1
                    i = i - 1
                    if approximate_words.__contains__(listed_inputed_string[i - 1]):
                        new_list = []
                        j = 0
                        # print(listed_inputed_string[i-1],"B")
                        while listed_inputed_string[i - 1] != '元':
                            # print(listed_inputed_string[i],"C")
                            # print(len(listed_inputed_string),"*",i)
                            i += 1
                        # break
                    if listed_inputed_string[i - 1] == "\n":
                        del listed_inputed_string[i - 1]
                        i -= 1
                        record_i -= 1
                if j != 0:
                    if i < 0:
                        i = 0
                    for k in range(i, record_i, 1):
                        new_list.append(listed_inputed_string[k])
                        # print(new_list, "[A]")
                    new_string = list_to_string_A(new_list)
                    del listed_inputed_string[i:record_i]
                    listed_inputed_string.insert(i, str(chn_to_arabic(new_string)))
                    i = i + 1
                    new_list = []
            if i == len(listed_inputed_string) - 1:
                break
        final_string = list_to_string_B(listed_inputed_string)
        print(final_string)
    except:
        error_list.append(file_list[now])


for error in range(len(error_list)):
    print("****** Remove",error_list[error],"******")

