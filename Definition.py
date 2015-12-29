#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'sdiox'
from re import escape

class Definition:
    def __init__(self, _kanji, _readings, _partOfSpeech, _meanings):
        self.kanji = _kanji
        self.readings = _readings
        self.partOfSpeech = _partOfSpeech
        self.meanings = _meanings

    @property
    def kanji(self):
        return self.kanji

    @kanji.setter
    def kanji(self, _kanji):
        self.kanji = _kanji

    @property
    def readings(self):
        return self.readings

    @readings.setter
    def readings(self, _readings):
        self.readings = _readings

    @property
    def partOfSpeech(self):
        return self.partOfSpeech

    @partOfSpeech.setter
    def partOfSpeech(self, _partOfSpeech):
        self.partOfSpeech = _partOfSpeech

    @property
    def meanings(self):
        return self.meanings

    @meanings.setter
    def meanings(self, _meanings):
        self.__meanings = _meanings

    def __repr__(self):
        return "Definition('{0}', '{1}', '{2}', '{3}')".format(escape(self.kanji),
                                                               escape(self.readings),
                                                               escape(self.partOfSpeech),
                                                               escape(self.meanings))
