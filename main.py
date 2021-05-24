#!/usr/bin/env python3
"""
Программное средство поиска стоп-слов на gitlab.
"""
import search_by_id
import warnings as w

OUTPUT = r'data\output.txt'
BLACK_LIST = r'data\black_list.txt'
FILE_CSV = r'data\formats.csv'


if __name__ == '__main__':
    #fullname = search_by_id.searcher_rep('git@gitwork.ru:polev/test.git')
    #paths = search_by_id.searcher_files()
    with w.catch_warnings(record=True) as warnings:
        w.simplefilter("always")
        search_by_id.csv_out(search_by_id.search_expansion(), FILE_CSV)

    for out in warnings:
        print(str(out.message))

    #search_by_id.pars_docx(paths, fullname, black_list, output)
    #search_by_id.pars_pptx(paths, fullname, black_list, output)
    #search_by_id.pars_md(paths, fullname, black_list, output)

    #stop_word = search_by_id.black_list(file=black_list)
    #search_by_id.output(fullname, stop_word, file=output)

