from flask import Flask ,render_template, request, redirect, url_for
from kanji2number import kanji2number
from number2kanji import number2kanji


app = Flask(__name__)


# トップページ
@app.route('/') #, methods=['GET','POST']) 
def index():
    return render_template('index.html')
    

# 入力送信用ページ    
@app.route('/v1/kanji2number', methods=['GET', 'POST'])
def kan():
    if request.method == 'POST':
        kanji=request.form.get('val')
        return redirect('/v1/kanji2number/'+kanji)     
    
@app.route('/v1/number2kanji', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        number=request.form.get('val')
        return redirect('/v1/number2kanji/'+number)     
       

# 結果表示用ページ        
@app.route('/v1/kanji2number/<kanji>')
def k2n(kanji):
    number = kanji2number(kanji)
    return render_template('k2n.html',number=number)
    
@app.route('/v1/number2kanji/<number>')
def n2k(number):
    kanji = number2kanji(number) 
    if kanji == '':
        return render_template('204.html')  # 変換できない場合のエラー表示
    return render_template('n2k.html',kanji=kanji)    
    
    
    

    

if __name__ == "__main__":
    app.run(debug=True)
    
