from flask import Flask, request, render_template, redirect, url_for, make_response

from logic import open_file, is_find

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.debug = True

data = {}


@app.route('/', methods=['post', 'get'])
def index():
    resp = make_response(render_template('search.html'))
    if request.method == 'POST':
        word = request.form.get('word')
        quantity = request.form.get('quantity')
        data.update(word=word, quantity=quantity)

        # всё сохраняем в куки/ для них нужно что-то вернуть
        cookie = {'word': request.cookies.get('word'), 'quantity': request.cookies.get('quantity')}
        resp = make_response(render_template('search.html', cookie=cookie))
        resp.set_cookie('word', data.get('word'))
        resp.set_cookie('quantity', data.get('quantity'))

        return redirect(url_for('result'))
    return resp


@app.route('/result/')
def result():
    obj_file = open_file("Harry Potter and the Sorcerer.txt")
    flag = is_find(obj_file, data.get('word'), data.get('quantity'))
    data.update(flag=flag)

    return render_template('result.html', data=data)


# if __name__ == "__main__":
#     app.run()
