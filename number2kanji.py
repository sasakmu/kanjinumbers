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