from tkinter import *
from tkinter import messagebox
import Rent_View as rv
import User_View as uv
import UI_Class as UC

def search_info(win, t, bt_def=None, chk:bool=1):
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    search_data = ['검색 후', search]   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
    win.info_list(t, bt_def, 15, chk, 1, search_data)

def main_menu(window:Tk, uc=None):
    Base = UC.new_window()
    if uc!=None:
        Base=uc

    window.title('도서관리시스템')
    Base.Change_Frame('도서관리시스템')

    Book = Button(Base.base_frame, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:createNewWindow_book_s(window, uc=Base))
    User = Button(Base.base_frame, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:uv.userwindow(window, uc=Base))
    Rent = Button(Base.base_frame, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window, uc=Base))

    Book.place(x=110, y=265)
    User.place(x=360, y=265)
    Rent.place(x=610, y=265)

# 도서조회
def createNewWindow_book_s(window:Tk, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 조회')
    new_win.Change_Frame('도서 조회')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '확인', lambda:creaNewWindow_book_info(window, uc=new_win)))
    new_win.createButton('등록', new_win.baseLabel, lambda:createNewWindow_book_r(window, uc=new_win))
    new_win.createButton('대출', new_win.baseLabel, lambda:rv.Rent_Screen(window, uc=new_win))
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '확인', lambda:creaNewWindow_book_info(window, uc=new_win))

# 도서조회(수정)
def createNewWindow_book_m(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 수정')
    new_win.Change_Frame('도서 수정')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '수정',lambda:creaNewWindow_book_info_re(window, uc=new_win), 0))
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t\t", '수정', lambda:creaNewWindow_book_info_re(window, uc=new_win), False)
    
# 도서조회(삭제)
def createNewWindow_book_del(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 삭제')
    new_win.Change_Frame('도서 삭제')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '삭제'))
    new_win.createButton('삭제', new_win.baseLabel)
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ", '삭제')

# 도서 등록
def createNewWindow_book_r(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 등록')
    new_win.Change_Frame('도서 등록')

    new_win.input_set('도서 등록')
    new_win.entry_set('제목', 1)
    new_win.entry_set('저자', 2)
    new_win.entry_set('출판사', 3)
    new_win.entry_set('ISBN', 4, ol=1)
    new_win.entry_set('가격', 6)
    new_win.entry_set('관련링크', 7)
    new_win.book_ex()
    new_win.under_button('등록', new_win.base_frame, bt2_def=lambda:creaNewWindow_book_info(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))

# 도서 정보
def creaNewWindow_book_info(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 정보')
    new_win.Change_Frame('도서 정보')

    new_win.input_set('도서 정보', 0)
    new_win.info_output('제목', 1)
    new_win.info_output('저자', 2)
    new_win.info_output('출판사', 3)
    new_win.info_output('ISBN', 4)
    new_win.info_output('가격', 5)
    new_win.info_output('관련링크', 6)
    new_win.book_ex(1, 1)
    new_win.under_button('삭제', new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:creaNewWindow_book_info_re(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))

# 도서 정보 수정
def creaNewWindow_book_info_re(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 정보')
    new_win.Change_Frame('도서 정보')

    new_win.input_set('도서 수정')
    new_win.entry_set('제목', 1, 1)
    new_win.entry_set('저자', 2, 1)
    new_win.entry_set('출판사', 3, 1)
    new_win.entry_set('ISBN', 4, 1, 1)
    new_win.entry_set('가격', 6, 1)
    new_win.entry_set('관련링크', 7, 1)
    new_win.book_ex(1)
    new_win.under_button('완료', new_win.base_frame, bt2_def=lambda:creaNewWindow_book_info(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))
    