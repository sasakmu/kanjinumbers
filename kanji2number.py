# 漢数字をアラビア数字に変換するプログラムです．
# 入力は漢数字，出力はアラビア数字（文字列扱い）です．
#
# 桁数の確認や漢数字が値として成立するか等のエラー判定は実装できていません．
# 規定の桁数の正しい漢数字が与えられたとき，対応するアラビア数字を返すことのみ保証しています．


import re 

t_ksuji = str.maketrans('壱弐参四五六七八九零', '1234567890')

re_ksuji = re.compile(r'[拾百千万億兆\d]+')
re_unit = re.compile(r'[拾百千]|\d+')
re_manshin = re.compile(r'[万億兆]|[^万億兆]+')

TRANSUNIT = {'拾': 10,
             '百': 100,
             '千': 1000}
TRANSMANS = {'万': 10000,
             '億': 100000000,
             '兆': 1000000000000}


def kanji2number(kstring: str, sep=False):
 
    def _transvalue(sj: str, re_obj=re_unit, transdic=TRANSUNIT):
        unit = 1
        result = 0
        for piece in reversed(re_obj.findall(sj)):
            if piece in transdic:
                unit = transdic[piece]
            else:
                val = int(piece) if piece.isdecimal() else _transvalue(piece)
                result += val * unit
                unit = 1

        if unit > 1:
            result += unit

        return result

    transuji = kstring.translate(t_ksuji)
    if not transuji.isdecimal():
            transuji = _transvalue(transuji, re_manshin, TRANSMANS)
            transuji = '{:,}'.format(transuji) if sep else str(transuji)
            
    return transuji
