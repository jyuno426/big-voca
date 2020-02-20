# -*- coding: utf-8 -*-
import eyed3
import json

if __name__=='__main__':
    f = open('./word_list.txt', 'r')
    word_list = [x.strip() for x in f.readlines()]
    f.close()

    for i, word in enumerate(word_list):
        name = str(i + 2001) + '_' + word
        def_list, ex_list = json.load(open('./data/' + name + '.json'))
        audio_file = eyed3.load('./Done/' + name + '.mp3')
        lyrics = '\n'.join(['Definitions:'] + def_list + ['Examples:'] + ex_list)
        audio_file.tag.lyrics.set(lyrics)
        audio_file.tag.save()
        print(name)
