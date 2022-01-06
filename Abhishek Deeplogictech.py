import flask
from flask import request, jsonify
import requests
from waitress import serve

app = flask.Flask(_name_)


@app.route('/getTimeStories')
def func():
    base_url = "https://time.com"
    resp = requests.get(url=base_url)
    response_text = resp.text
    line_no = 0
    result=[]
    for line in response_text.splitlines():
        line_no += 1
        if line_no in [1411, 1422, 1433, 1444, 1455]:
            temp = line.split(">")
            title = temp[2][:-3]
            url = base_url + temp[1][8:]
            result.append({"title":title, "link":url})
    return jsonify(result)


if _name_ == "_main_":
    serve(app, host='0.0.0.0', port=8888)