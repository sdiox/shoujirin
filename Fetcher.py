#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'sdiox'
from Keyword import Keyword
from Definition import Definition
from bs4 import BeautifulSoup
import requests

class Fetcher:
    BASE_URL = "http://j-doradic.com/index.php"

    __html = None
    __htmlSoup = None
    __totalPageNumber = 0

    def __init__(self, _firstPageOnly=True, _wordToSearch=None):
        self.firstPageOnly = _firstPageOnly
        self.wordToSearch = _wordToSearch

    @property
    def wordToSearch(self):
        return self.__wordToSearch
    @wordToSearch.setter
    def wordToSearch(self, _wordToSearch):
        self.__wordToSearch = _wordToSearch

    def performSearch(self):
        self.keyword = Keyword(self.wordToSearch)
        self.__fetch_html_page()
        self.__make_soup_from_html()
        self.__detect_page_number()

        _keyword = Keyword(self.wordToSearch)

        if self.__totalPageNumber == 0:
            return _keyword
        else:
            _keyword.definitions.extend(self.__extract_definitions())
            # print('[DEBUG] Working on page 1 with {0} definitions...'.format(len(_keyword.definitions)))
            if(self.__totalPageNumber > 1 and self.firstPageOnly == False):
                for _pageNumber in range(1, self.__totalPageNumber):
                    self.__fetch_html_page(_pageNumber + 1)
                    self.__make_soup_from_html()
                    _defs = self.__extract_definitions()
                    _keyword.definitions.extend(_defs)
                    # print('[DEBUG] Working on page {0} with {1} definitions...'.format(_pageNumber+1, len(_defs)))

        return _keyword

    def __fetch_html_page(self, pageNumber=None):
        payload = {}
        payload['m'] = 'dictionary'
        payload['a'] = 'data'
        payload['k'] = self.wordToSearch
        # payload['k'] = urllib.quote_plus(self.wordToSearch.encode('utf8'))

        if pageNumber is not None and pageNumber > 1:
            payload['page'] = pageNumber

        request = requests.get(self.BASE_URL, params=payload)
        self.__html = request.text
        # print('[DEBUG] payload: {0}'.format(payload))
        # print('[DEBUG] len of html response: {0}'.format(len(self.__html)))

    def __make_soup_from_html(self):
        self.__htmlSoup = BeautifulSoup(self.__html, 'html.parser')

    # this method returns 0 when there is no matching words from the keyword
    def __detect_page_number(self):
        _resultRows = self.__htmlSoup.find('tr', attrs={'class': 'tb1'})

        if _resultRows is None:
            self.__totalPageNumber = 0
        else:
            self.__totalPageNumber = 1

            _totalRow = self.__htmlSoup.find('tr', attrs={'class': 'total'})
            _linkToLastPage = _totalRow.find('a', text='»')

            if _linkToLastPage is not None:
                _url = _linkToLastPage['href']
                self.__totalPageNumber = int(_url[_url.rindex('=')+1:])

        return self.__totalPageNumber

    def __extract_definitions(self):
        _definitions = []
        _definitionRows = self.__htmlSoup.select('tr.tb1')

        for _defRow in _definitionRows:
            _cols = _defRow.find_all('td', attrs={'class': 'sl'})
            _stringsCols = map(lambda _col: _col.getText(), _cols)

            _def = Definition(_stringsCols[0], _stringsCols[1], _stringsCols[2], _stringsCols[3])
            _definitions.append(_def)

        return _definitions
