from tkinter import *
from tkinter import messagebox
import UI_Class as UC
import Book_class as BC
import Rent_View as rv
import User_View as uv

def search_info(win, chk:bool=1): # bt_def=None, 
    book_data = BC.Book_DataFrame()
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    search_data = book_data.Book_Search(search)   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
    win.Book_info_list(search_data, font_size=15, choice=chk) # win.info_list(t, bt_def, 15, chk, 1)

def main_menu(window:Tk, uc=None):
    Base = UC.new_window()
    if uc!=None:
        Base = uc

    window.title('도서관시스템')
    Base.Change_Frame('도서관리프로그램')

    Book = Button(Base.base_frame, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:createNewWindow_book_s(window, uc=Base))
    User = Button(Base.base_frame, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:uv.userwindow(window, uc=Base))
    Rent = Button(Base.base_frame, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window, uc=Base))

    Book.place(x=110, y=265)
    User.place(x=360, y=265)
    Rent.place(x=610, y=265)

# 도서조회 
def createNewWindow_book_s(window, uc=None):
    book_new_win = UC.new_window()
    book_data = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc

    window.title('도서 조회')
    book_new_win.Change_Frame('도서 조회')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, lambda : createNewWindow_book_s(window, uc=book_new_win)))
    book_new_win.createButton('대출', book_new_win.baseLabel, lambda : rv.Rent_Screen(window, uc=book_new_win))
    book_new_win.createButton('등록', book_new_win.baseLabel, lambda: createNewWindow_book_r(window, uc=book_new_win))
    book_new_win.Book_list("제목\t\t저자\t\t\t출판사\t\tISBN\t대출여부     ", None, book_data.Book_list_all(), lambda : creaNewWindow_book_info(window, uc=book_new_win))

# 도서조회(수정)
def createNewWindow_book_m(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc

    window.title('도서 수정')
    book_new_win.Change_Frame('도서 수정')
    
    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, None, lambda : createNewWindow_book_s(window, uc=book_new_win), 0))
    book_new_win.createButton('등록', book_new_win.baseLabel, lambda: createNewWindow_book_r(window, uc=book_new_win))
    book_new_win.createButton('대출', book_new_win.baseLabel, lambda : rv.Rent_Screen(book_new_win, 1))
    book_new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '수정', book_class.Book_list_all(),lambda : creaNewWindow_book_info_re(window, uc=book_new_win), False)

# 도서조회(삭제)
def createNewWindow_book_del(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc
    window.title('도서 삭제')
    book_new_win.Change_Frame('도서 삭제')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, lambda : createNewWindow_book_s(window, uc=book_new_win)))
    book_new_win.createButton('삭제', book_new_win.baseLabel, lambda : book_class.Book_del)
    book_new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '삭제', book_class.Book_list_all(),lambda : creaNewWindow_book_info_re(window, uc=book_new_win), False)



# 도서 등록 
def createNewWindow_book_r(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc

    window.title('도서 등록')
    book_new_win.Change_Frame('도서 등록')

    book_new_win.input_set('도서 등록')
    title = book_new_win.book_entry_set('제목', 1)
    author = book_new_win.book_entry_set('저자', 2)
    pub = book_new_win.book_entry_set('출판사', 3)
    isbn = book_new_win.book_entry_set('ISBN', 4, ol=1)
    price = book_new_win.book_entry_set('가격', 6)
    link = book_new_win.book_entry_set('관련링크', 7)
    description = book_new_win.book_ex()
    in_data = [title, author, pub, isbn, price, link, description]
    book_new_win.under_button('등록', book_new_win.base_frame, bt2_def=lambda:[book_class.Book_in(in_data), main_menu(window, uc=book_new_win)], bt3_def=lambda : main_menu(window, uc=book_new_win))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 도서 정보
def creaNewWindow_book_info(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    out_data = book_class.book
    if uc != None:
        book_new_win=uc
    window.title('도서 정보')
    book_new_win.Change_Frame('도서 정보')

    book_new_win.input_set('도서 정보', 0)
    book_new_win.info_output('제목', 1, out_data['BOOK_TITLE'])
    book_new_win.info_output('저자', 2, out_data['BOOK_AUTHOR'])
    book_new_win.info_output('출판사', 3, out_data['BOOK_PUB'])
    book_new_win.info_output('ISBN', 4, out_data['BOOK_ISBN'])
    book_new_win.info_output('가격', 5, out_data['BOOK_PRICE'])
    book_new_win.info_output('관련링크', 6, out_data['BOOK_LINK'])
    book_new_win.book_ex(1, 1)
    book_new_win.under_button('삭제', book_new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:creaNewWindow_book_info_re(window, uc=book_new_win))

# 도서 정보 수정
def creaNewWindow_book_info_re(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc
    window.title('도서 정보')
    book_new_win.Change_Frame('도서 정보')

    out_data = book_class.Book_info(9788970504773)
    book_new_win.input_set('도서 수정')
    title = book_new_win.entry_set('제목', 1, 1, out_data[0])
    author = book_new_win.entry_set('저자', 2, 1, out_data[1])
    pub = book_new_win.entry_set('출판사', 3, 1, out_data[2])
    isbn = book_new_win.entry_set('ISBN', 4, 1, 1, out_data[3])
    price = book_new_win.entry_set('가격', 6, 1, out_data[4])
    link = book_new_win.entry_set('관련링크', 7, 1, out_data[5])
    description=book_new_win.book_ex(1)
    in_data = [title, author, pub, isbn, price, link, description]
    book_new_win.under_button('완료', book_new_win.base_frame, bt2_def=lambda:creaNewWindow_book_info(window, uc=book_new_win))
    

