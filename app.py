from flask import Flask, request, render_template, redirect, url_for, make_response, Response, jsonify

from logic import open_file, is_find, open_file_for_json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.debug = True

data = {}
cookie = {'flag': False}


@app.route('/', methods=['post', 'get'])
def index():
    global cookie
    # resp = Response()
    if request.method == 'POST':
        word = request.form.get('word')
        quantity = request.form.get('quantity')
        data.update(word=word, quantity=quantity)

        # всё сохраняем в куки/ для них нужно что-то вернуть
        resp = make_response("")
        resp.set_cookie('word', data.get('word'), max_age=1000 * 60 * 60 * 60 * 24)
        resp.set_cookie('quantity', data.get('quantity'), max_age=1000 * 60 * 60 * 60 * 24)
        cookie = {'word': request.cookies.get('word'), 'quantity': request.cookies.get('quantity')}
        resp.headers['location'] = url_for('result')

        return resp, 302
    return render_template('search.html', cookie=cookie)


@app.route('/result/')
def result():
    # obj_file = open_file(r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\6\flask\Harry Potter and the Sorcerer.txt")
    obj_file = open_file("/home/Artemy/mysite/Harry Potter and the Sorcerer.txt")
    flag = is_find(obj_file, data.get('word'), data.get('quantity'))
    data.update(flag=flag)

    cookie['flag'] = flag
    return render_template('result.html', data=data)


@app.route('/request/')
def my_request():
    # json_obj = read_json(path_json_i
    # file_read = open_file_for_json(r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\
    # 6\flask\Harry Potter and the Sorcerer.txt")
    file_read = open_file("/home/Artemy/mysite/Harry Potter and the Sorcerer.txt")
    proposal = []

    for str_read in file_read:
        if request.json["example minimum length"] <= len(str_read) <= request.json["example maximum length"]:
            fl_search = True
            for words in request.json["words"]:
                if words not in str_read:
                    fl_search = False
                    break
            if fl_search:
                proposal.append(str_read)
        if len(proposal) == request.json["number of examples"]:
            break

    return jsonify(example=proposal,
                   example_minimum_length=request.json["example minimum length"],
                   example_maximum_length=request.json["example maximum length"],
                   len=len(proposal),
                   word=data.get('word'))


# if __name__ == "__main__":
#     app.run()
