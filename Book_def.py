from tkinter import *
from tkinter import messagebox
import Rent_View as rv
import UI_Class as UC

# 도서조회
def createNewWindow_book_s(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 조회')
    else:
        new_win=window
        new_win.Change_Frame('도서 조회')

    new_win.Search_bar()
    new_win.createButton('등록', new_win.baseLabel)
    new_win.createButton('대출', new_win.baseLabel)
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '확인', lambda:creaNewWindow_book_info(new_win, 1))


# 도서 등록
def createNewWindow_book_r(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 등록')
    else:
        new_win=window
        new_win.Change_Frame('도서 등록')

    new_win.input_set('도서 등록')
    new_win.entry_set('제목', 1)
    new_win.entry_set('저자', 2)
    new_win.entry_set('출판사', 3)
    new_win.entry_set('ISBN', 4, ol=1)
    new_win.entry_set('가격', 6)
    new_win.entry_set('관련링크', 7)
    new_win.book_ex()
    new_win.under_button('등록', new_win.base_frame, bt2_def=lambda:creaNewWindow_book_info(new_win, 1))

# 도서 정보
def creaNewWindow_book_info(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 조회')
    else:
        new_win=window
        new_win.Change_Frame('도서 조회')

    new_win.input_set('도서 정보', 0)
    new_win.info_output('제목', 1)
    new_win.info_output('저자', 2)
    new_win.info_output('출판사', 3)
    new_win.info_output('ISBN', 4)
    new_win.info_output('가격', 5)
    new_win.info_output('관련링크', 6)
    new_win.book_ex(1, 1)
    new_win.under_button('삭제', new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:creaNewWindow_book_info_re(new_win, 1))

# 도서 정보 수정
def creaNewWindow_book_info_re(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 수정')
    else:
        new_win=window
        new_win.Change_Frame('도서 수정')

    new_win.input_set('도서 수정')
    new_win.entry_set('제목', 1, 1)
    new_win.entry_set('저자', 2, 1)
    new_win.entry_set('출판사', 3, 1)
    new_win.entry_set('ISBN', 4, 1, 1)
    new_win.entry_set('가격', 6, 1)
    new_win.entry_set('관련링크', 7, 1)
    new_win.book_ex(1)
    new_win.under_button('완료', new_win.base_frame, bt2_def=lambda:creaNewWindow_book_info(new_win, 1))
    

# 도서조회(수정)
def createNewWindow_book_m(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 수정')
    else:
        new_win=window
        new_win.Change_Frame('도서 수정')

    new_win.Search_bar()
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t\t", '수정', lambda:creaNewWindow_book_info_re(new_win, 1), False)
    
# 도서조회(삭제)
def createNewWindow_book_del(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 삭제')
    else:
        new_win=window
        new_win.Change_Frame('도서 삭제')

    new_win.Search_bar()
    new_win.createButton('삭제', new_win.baseLabel)
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '삭제')