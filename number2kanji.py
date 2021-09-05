# アラビア数字を漢数字に変換するプログラムです．
# 入力はアラビア数字（文字列扱い），出力は漢数字です．
#
# 既定の桁数に対するエラー判定は実装していません．
# 16 桁までのアラビア数字に対して，対応する漢数字を返すことだけを保証しています．



import re

t_ksuji = str.maketrans('1234567890','壱弐参四五六七八九零')

t_unit = '千百拾兆千百拾億千百拾万千百拾'
t_unit = t_unit[::-1]

def number2kanji(sj:str):

    kansuji = sj.translate(t_ksuji)
    m = len(kansuji)
    
    if m == 1:
        return kansuji
    
    else:
        transuji = ''
        if not kansuji[m-1] == '零':
            transuji = kansuji[m-1] 
        for i in range(2,m+1):
            
            if not  kansuji[m-i] == '零':
                 transuji = kansuji[m-i]+t_unit[i-2] + transuji 
    
        return transuji
