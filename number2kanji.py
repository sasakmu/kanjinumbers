# アラビア数字を漢数字に変換するプログラムです．
# 入力はアラビア数字（文字列扱い），出力は漢数字です．
#
# 規定の桁数（16 桁）以上の値が入力された場合はエラーコードを表示するページに遷移します．
# 入力値の頭に 0 がついている場合でも出力に問題はありませんが，頭の 0 を含めて 16 桁までの値しか変換できません． 




import re

t_ksuji = str.maketrans('1234567890','壱弐参四五六七八九零')

t_unit = '千百拾兆千百拾億千百拾万千百拾'
t_unit = t_unit[::-1]

def number2kanji(sj:str):

    if len(sj)>16:
        return 'err'　# 桁数が規定の 16 桁を超えた場合のエラー表示
    
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
