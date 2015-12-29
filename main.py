#!/usr/bin/env python

# jdoradic-lite is a simple web application that extract the table that
# contains definitions of words containing the search keyword user typed.
# developed by sdiox

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager, Server
from KeywordForm import KeywordForm
from Fetcher import Fetcher
from bs4 import BeautifulSoup
from DictionaryDB import DictionaryDB

app = Flask(__name__)
app.config['SECRET_KEY'] = 'j-doradic lite rocks!'
app.config['DATASOURCE'] = 'web'
boostrap = Bootstrap(app)
manager = Manager(app)
manager.add_command("runserver", Server())

@app.route('/', methods=['GET'])
@app.route('/index.html', alias=True)
def index():
    keyword = ''
    form = KeywordForm(csrf_enabled=True)

    return render_template('index.html', form=form, keyword=keyword)

# a quick and dirty hack to beautify the resultant url
@app.route('/search', methods=['POST'])
def forward_search():
    form = KeywordForm(csrf_enabled=True)
    keyword = form.keyword.data
    onlyFirstPage = form.onlyFirstPage.data

    # strip tags
    _soup = BeautifulSoup(keyword, 'html.parser')
    keyword = _soup.getText()

    _destAction = 'search_limit' if onlyFirstPage else 'search'
    return redirect(url_for(_destAction, keyword=keyword))

# a quick and dirty hack to beautify the resultant url
@app.route('/search/<prev_keyword>', methods=['POST'])
def forward_search_2(prev_keyword):
    form = KeywordForm(csrf_enabled=True)
    keyword = form.keyword.data
    onlyFirstPage = form.onlyFirstPage.data

    # strip tags
    _soup = BeautifulSoup(keyword, 'html.parser')
    keyword = _soup.getText()

    _destAction = 'search_limit' if onlyFirstPage else 'search'
    return redirect(url_for(_destAction, keyword=keyword))

# a quick and dirty hack to beautify the resultant url
@app.route('/search/limit/<prev_keyword>', methods=['POST'])
def forward_search_3(prev_keyword):
    form = KeywordForm(csrf_enabled=True)
    keyword = form.keyword.data
    onlyFirstPage = form.onlyFirstPage.data

    # strip tags
    _soup = BeautifulSoup(keyword, 'html.parser')
    keyword = _soup.getText()

    _destAction = 'search_limit' if onlyFirstPage else 'search'
    return redirect(url_for(_destAction, keyword=keyword))


@app.route('/search/<keyword>', methods=['GET'])
def search(keyword):
    # a quick hack to clear out the value or attribute action in the form
    action_name = ' '

    form = KeywordForm(csrf_enabled=True)
    onlyFirstPage = False

    searchResult = None

    if app.config['DATASOURCE'] == 'local':
        dictDb = DictionaryDB(limit=onlyFirstPage)
        searchResult = dictDb.search(keyword)
    else:
        # send request to j-doradic and collect word definitions here
        fetcher = Fetcher(onlyFirstPage, keyword)
        searchResult = fetcher.performSearch()

    return render_template('search_result.html', form=form, action_name=action_name, onlyFirstPage=onlyFirstPage, keyword=keyword, searchResult=searchResult)

@app.route('/search/limit/<keyword>', methods=['GET'])
def search_limit(keyword):
    # a quick hack to clear out the value or attribute action in the form
    action_name = ' '

    form = KeywordForm(csrf_enabled=True)
    onlyFirstPage = True

    searchResult = None

    if app.config['DATASOURCE'] == 'local':
        dictDb = DictionaryDB(limit=onlyFirstPage)
        searchResult = dictDb.search(keyword)
    else:
        # send request to j-doradic and collect word definitions here
        fetcher = Fetcher(onlyFirstPage, keyword)
        searchResult = fetcher.performSearch()

    return render_template('search_result.html', form=form, action_name=action_name, onlyFirstPage=onlyFirstPage, keyword=keyword, searchResult=searchResult)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
