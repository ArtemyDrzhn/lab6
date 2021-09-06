from flask import Flask, request, render_template, redirect, url_for, make_response

from logic import open_file, is_find

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.debug = True

data = {}


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        word = request.form.get('word')
        quantity = request.form.get('quantity')
        data.update(word=word, quantity=quantity)
        return redirect(url_for('result'))
    return render_template('search.html')


@app.route('/result/')
def result():
    obj_file = open_file("/home/Artemy/mysite/Harry Potter and the Sorcerer.txt")
    flag = is_find(obj_file, data.get('word'), data.get('quantity'))
    data.update(flag=flag)
    # всё сохраняем в куки
    res = make_response("Setting a cookie")
    res.set_cookie('word', data.get('word'))
    res.set_cookie('quantity', data.get('quantity'))
    # res.set_cookie('flag', str(data.get('flag')))

    if flag:
        res = make_response("Найдено слово {}".format(data.get('word')))
    else:
        res = make_response("Не найдено слово {}".format(data.get('word')))
    return res