#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'sdiox'


class Keyword:
    def __init__(self, _keyword, _definitions=[]):
        self.keyword = _keyword
        self.definitions = _definitions

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, _keyword):
        self.__keyword = _keyword

    @property
    def definitions(self):
        return self.__definitions

    @definitions.setter
    def definitions(self, _defs):
        self.__definitions = _defs

    @property
    def definition_number(self):
        return len(self.definitions)

    def __str__(self):
        return u'<Word: {0} with {1} definitions>'.format(self.keyword, len(self.definitions))

    def __repr__(self):
        return u'Word({0}, {1})'.format(self.keyword, self.definitions)
