# 讀取檔案函式
def read_file(filename):
    lines = []
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 資料轉換函式
def convert(lines):
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
        #print(s)
    print('allen說了', allen_word_count, '個字')
    print('Allen傳了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '個圖片')
    print('viki說了', viki_word_count, '個字')
    print('viki傳了', viki_sticker_count, '個貼圖')
    print('viki傳了', viki_image_count, '個圖片')

# 資料寫入函式
def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')

# 執行函式
def main():
    lines = read_file('LINE-Viki.txt') 
    lines = convert(lines)
    # write_file('output.txt', lines)

# 執行
main()

# 在此加上print(new)會出現NameError: name 'new' is not defined 錯誤訊息，因def內設定的變數僅能於def內使用
# 如加print(lines)也是 NameError: name 'lines' is not defined