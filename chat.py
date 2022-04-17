# 讀取檔案函式
def read_file(filename):
    lines = []
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    print(lines)
    return lines

# 資料轉換函式
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        elif person:                                          # elif person有被設值的話，才做這一行；若是None則不執行
            new.append(person + ': ' + line)
    return new

# 資料寫入函式
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

# 執行函式
def main():
    inp = input('請輸入需讀取檔名:')
    lines = read_file(inp)
    lines = convert(lines)
    write_file('output.txt', lines)

# 執行
main()

# 在此加上print(new)會出現NameError: name 'new' is not defined 錯誤訊息，因def內設定的變數僅能於def內使用
# 如加print(lines)也是 NameError: name 'lines' is not defined