from flask import Flask, render_template
import requests
import urllib.request,json


app=Flask(__name__)
@app.route('/')
def home_page():
    base_url="https://newsapi.org/v2/everything?q=Apple&from=2022-01-25&sortBy=popularity&apiKey=00f0b05c0edb45a38a541d1d9bbcab6b"
    data=requests.get(base_url).json()["articles"]
    print(data)
    return render_template('index.html',news=data)

if __name__=='__main__':
    app.run(debug=True)

  