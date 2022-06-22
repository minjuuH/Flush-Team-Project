from tkinter import *
from tkinter import messagebox
import UI_Class as UC
import Book_class as BC
import Rent_View as rv
import User_View as uv

def search_info(win, choice, chk=True, bd_win=None, UC=None): # bt_def=None, 
    book_data = BC.Book_DataFrame()
    book_data.readcsv()
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    search_data = book_data.Book_Search(search)   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
    if choice == '조회':
        win.Book_info_list(search_data, bd_window=bd_win, font_size=15, uc=UC, choice=chk, bt_text='확인') # win.info_list(t, bt_def, 15, chk, 1)

    elif choice == '수정':
        win.Book_info_list(search_data, bt_text=choice, bd_window=bd_win, font_size=15, uc=UC, choice=chk)

    elif choice == '삭제':
        win.Book_info_list(search_data, bd_window=bd_win, font_size=15, uc=UC, choice=chk, bt_text=choice)

    # else:
    #     win.Book_info_list(search_data, bd_window=bd_win, font_size=15, uc=UC, choice=chk) # win.info_list(t, bt_def, 15, chk, 1)


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


# 도서조회  -------------------완료----------------------
def createNewWindow_book_s(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()
    
    if uc != None:
        book_new_win=uc

    window.title('도서 조회')
    book_new_win.Change_Frame('도서 조회')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, '조회', bd_win=window, UC=book_new_win, chk=False))
    book_new_win.createButton('대출', book_new_win.baseLabel, lambda : rv.Rent_Screen(window, uc=book_new_win))
    book_new_win.createButton('등록', book_new_win.baseLabel, lambda: createNewWindow_book_r(window, uc=book_new_win))
    book_new_win.Book_list("{:>25}{:>25}{:>25}{:>30}".format('제목','저자','출판사','ISBN'), '확인', book_class.Book_list_all(), choice = False, bd_window = window, uc=book_new_win)

# 도서조회(수정) -------------------완료----------------------
def createNewWindow_book_m(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc

    window.title('도서 수정')
    book_new_win.Change_Frame('도서 수정')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, '수정', chk=False, bd_win=window, UC=book_new_win))
    book_new_win.Book_list("{:>25}{:>25}{:>25}{:>30}".format('제목','저자','출판사','ISBN'), '수정', book_class.Book_list_all(), choice = False, bd_window = window, uc=book_new_win)


# 도서조회(삭제) ---------------------삭제------------------
def createNewWindow_book_del(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc
    window.title('도서 삭제')
    book_new_win.Change_Frame('도서 삭제')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, '삭제', bd_win=window, UC=book_new_win))
    book_new_win.createButton('삭제', book_new_win.baseLabel, uc=book_new_win, Mwin=window)
    book_new_win.Book_list("{:>25}{:>25}{:>25}{:>30}".format('제목','저자','출판사','ISBN'), '삭제', book_class.Book_list_all(), choice = True, bd_window = window, uc=book_new_win)

# 도서 삭제 함수
def del_book(window, isbn, uc=None, info=False):
    book_class=BC.Book_DataFrame()
    book_class.readcsv()
    ask = book_class.Book_del(isbn)
    book_class.tocsv()
    #도서 상세정보창에서 삭제한 경우, 도서 삭제 후 도서 조회창으로 이동하도록 설정
    if ask and info:
        createNewWindow_book_s(window, uc)
    elif ask:
        createNewWindow_book_del(window, uc)


# 도서 등록 
def createNewWindow_book_r(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

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

    def book_add() :
        in_data = [title.get(), author.get(), pub.get(), int(isbn.get()), price.get(), link.get(), description.get()]
        ask = book_class.Book_in(in_data=in_data)
        book_class.tocsv()
        if ask:
            creaNewWindow_book_info(window, in_data[3], uc)

    book_new_win.under_button('등록', book_new_win.base_frame, bt2_def=book_add, bt3_def=lambda : main_menu(window, uc=book_new_win))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 도서 정보
def creaNewWindow_book_info(window, isbn, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    out_data = book_class.Book_info(isbn)
    if uc != None:
        book_new_win=uc
    window.title('도서 정보')
    book_new_win.Change_Frame('도서 정보')

    book_new_win.input_set('도서 정보', 0)
    book_new_win.info_output('제목', 1, out_data[1])
    book_new_win.info_output('저자', 2, out_data[2])
    book_new_win.info_output('출판사', 3, out_data[3])
    book_new_win.info_output('ISBN', 4, out_data[0])
    book_new_win.info_output('가격', 5, out_data[4])
    book_new_win.info_output('관련링크', 6, out_data[5])
    book_new_win.book_ex(1, out_data[6], 1)
    book_new_win.under_button('삭제', book_new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:creaNewWindow_book_info_re(window, isbn, uc=book_new_win), bt3_t='닫기', bt3_def=lambda:main_menu(window, book_new_win), bt2_def=lambda:del_book(window,[out_data[0]],book_new_win,1))

# 도서 정보 수정 ----------완료-------------
def creaNewWindow_book_info_re(window, ISBN, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc

    window.title('도서 수정')
    book_new_win.Change_Frame('도서 수정')


    out_data = book_class.Book_info(ISBN)
    book_new_win.input_set('도서 수정')
    #out_data의 순서와 입력칸의 순서가 맞지 않아 제대로 연결되게끔 수정
    title = book_new_win.book_entry_set('제목', 1, 1, text_data = out_data[1])
    author = book_new_win.book_entry_set('저자', 2, 1, text_data = out_data[2])
    pub = book_new_win.book_entry_set('출판사', 3, 1, text_data = out_data[3])
    isbn = book_new_win.book_entry_set('ISBN', 4, 1, 1, text_data = out_data[0], ISBN=ISBN)
    price = book_new_win.book_entry_set('가격', 6, 1, text_data = out_data[4])
    link = book_new_win.book_entry_set('관련링크', 7, 1, text_data = out_data[5])
    description=book_new_win.book_ex(1, out_data[6])

    def modi_clear():   #완료 버튼 커멘드로 연결할 함수
        in_data = [title.get(), author.get(), pub.get(), int(isbn.get()), int(price.get()), link.get(), description.get()]
        # print(in_data)
        ask = book_class.Book_modi(check_isbn=ISBN, modi_data=in_data)
        book_class.tocsv()
        if ask:
            creaNewWindow_rebook_info(window, in_data, uc)
        # main_menu(window, uc=book_new_win) #추후에 해당도서 상세정보창으로 이동하도록 변경
    book_new_win.under_button('완료', book_new_win.base_frame, bt2_def=modi_clear, bt3_def=lambda:main_menu(window, book_new_win))

    # 도서 수정 정보 확인
def creaNewWindow_rebook_info(window, out_data=[], uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc
    window.title('도서 정보')
    book_new_win.Change_Frame('도서 정보')
    print(out_data)
    book_new_win.input_set('도서 정보', 0)
    book_new_win.info_output('제목', 1, out_data[0])
    book_new_win.info_output('저자', 2, out_data[1])
    book_new_win.info_output('출판사', 3, out_data[2])
    book_new_win.info_output('ISBN', 4, out_data[3])
    book_new_win.info_output('가격', 5, out_data[4])
    book_new_win.info_output('관련링크', 6, out_data[5])
    book_new_win.book_ex(1, out_data[6], 1)
    book_new_win.under_button('삭제', book_new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:creaNewWindow_book_info_re(window, out_data[3], uc=book_new_win), bt2_def=lambda:del_book(window,[out_data[3]],book_new_win,1), bt3_t='닫기', bt3_def=lambda:main_menu(window, book_new_win))
    

