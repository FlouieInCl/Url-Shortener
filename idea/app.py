from flask import Flask, request, redirect

app = Flask(__name__)

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
mapper = {}


def base62_encoding(val, str_scope=BASE62):
    if val == 0:
        return str_scope[0]

    arr = []
    while val:
        val, tmp = divmod(val, 62)
        arr.append(str_scope[tmp])
    arr.reverse()

    return ''.join(arr)


@app.route('/short', methods=['POST'])
def index():
    url = request.json['url']
    ascii_sum = sum([ord(i) for i in url])

    shortened_url = base62_encoding(ascii_sum)

    mapper[shortened_url] = url

    return shortened_url


@app.route('/<shortened_url>', methods=['GET'])
def move(shortened_url):
    return redirect(mapper[shortened_url], 302)


app.run()
