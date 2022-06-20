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
        win.Book_info_list(search_data, bd_window=bd_win, font_size=15, uc=UC, choice=chk) # win.info_list(t, bt_def, 15, chk, 1)

    elif choice == '수정':
        win.Book_info_list(search_data, bt_text=choice, bd_window=bd_win, font_size=15, uc=UC, choice=chk)

    elif choice == '삭제':
        win.Book_list("제목\t\t저자\t\t\t출판사\t\tISBN\t\t", '삭제', book_data.Book_list_all(), choice = False, bd_window = bd_win, uc=UC)

    else:
        win.Book_info_list(search_data, bd_window=bd_win, font_size=15, uc=UC, choice=chk) # win.info_list(t, bt_def, 15, chk, 1)

        


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
    book_class = BC.Book_DataFrame()
    book_class.readcsv()
    
    if uc != None:
        book_new_win=uc

    window.title('도서 조회')
    book_new_win.Change_Frame('도서 조회')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, '조회'))
    book_new_win.createButton('대출', book_new_win.baseLabel, lambda : rv.Rent_Screen(window, uc=book_new_win))
    book_new_win.createButton('등록', book_new_win.baseLabel, lambda: createNewWindow_book_r(window, uc=book_new_win))
    book_new_win.Book_list("제목\t\t저자\t\t\t출판사\t\tISBN\t\t", None, book_class.Book_list_all())
    # book_new_win.Book_list("제목\t\t저자\t\t\t출판사\t\tISBN\t\t", '확인', book_class.Book_list_all())



# 도서조회(수정)
def createNewWindow_book_m(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc

    window.title('도서 수정')
    book_new_win.Change_Frame('도서 수정')

    # book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, chk=False))
    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, '수정', chk=False, bd_win=window, UC=book_new_win))
    book_new_win.Book_list("제목\t\t저자\t\t\t출판사\t\tISBN\t\t", '수정', book_class.Book_list_all(), choice = False, bd_window = window, uc=book_new_win)


# 도서조회(삭제)
def createNewWindow_book_del(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    if uc != None:
        book_new_win=uc
    window.title('도서 삭제')
    book_new_win.Change_Frame('도서 삭제')

    book_new_win.Search_bar(S_def=lambda : search_info(book_new_win, lambda : createNewWindow_book_s(window, uc=book_new_win)))
    book_new_win.createButton('삭제', book_new_win.baseLabel, lambda : book_class.Book_del())
    book_new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t\t", '삭제', book_class.Book_list_all(), lambda : creaNewWindow_book_info_re(window, book_class.Select(), uc=book_new_win), False,bd_window = window)


# 도서 등록 
def createNewWindow_book_r(window, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    book_class.readcsv()

    if uc != None:
        book_new_win=uc

    window.title('도서 등록')
    book_new_win.Change_Frame('도서 등록')

    def book_add() :
        in_data = [title.get(), author.get(), pub.get(), isbn.get(), price.get(), link.get(), description.get()]
        book_class.Book_in(in_data)
        book_class.tocsv()
        main_menu(window, uc=book_new_win)

    book_new_win.input_set('도서 등록')
    title = book_new_win.book_entry_set('제목', 1)
    author = book_new_win.book_entry_set('저자', 2)
    pub = book_new_win.book_entry_set('출판사', 3)
    isbn = book_new_win.book_entry_set('ISBN', 4, ol=1)
    price = book_new_win.book_entry_set('가격', 6)
    link = book_new_win.book_entry_set('관련링크', 7)
    description = book_new_win.book_ex()
    book_new_win.under_button('등록', book_new_win.base_frame, bt2_def=lambda:[book_add, main_menu(window, uc=book_new_win)], bt3_def=lambda : main_menu(window, uc=book_new_win))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 도서 정보
def creaNewWindow_book_info(window, isbn, uc=None):
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
def creaNewWindow_book_info_re(window, ISBN, uc=None):
    book_new_win = UC.new_window()
    book_class = BC.Book_DataFrame()
    
    if uc != None:
        book_new_win=uc

    window.title('도서 수정')
    book_new_win.Change_Frame('도서 수정')

    def modi_clear(c_isbn):   #완료 버튼 커멘드로 연결할 함수
        in_data = [title.get(), author.get(), pub.get(), int(isbn.get()), int(price.get()), link.get(), description.get()]
        # print(in_data)
        book_class.Book_modi(check_isbn=c_isbn, modi_data=in_data)   #현재 isbn 값이 제대로 전달되지 X 임의의 값 지정으로 기능 확인만 완료
        main_menu(window, uc=book_new_win) #추후에 해당도서 상세정보창으로 이동하도록 변경

    out_data = book_class.Book_info(ISBN)
    book_new_win.input_set('도서 수정')
    #out_data의 순서와 입력칸의 순서가 맞지 않아 제대로 연결되게끔 수정
    title = book_new_win.book_entry_set('제목', 1, 1, text_data = out_data[1])
    author = book_new_win.book_entry_set('저자', 2, 1, text_data = out_data[2])
    pub = book_new_win.book_entry_set('출판사', 3, 1, text_data = out_data[3])
    isbn = book_new_win.book_entry_set('ISBN', 4, 1, 1, text_data = out_data[0])
    price = book_new_win.book_entry_set('가격', 6, 1, text_data = out_data[4])
    link = book_new_win.book_entry_set('관련링크', 7, 1, text_data = out_data[5])
    description=book_new_win.book_ex(1)

    #수정한 데이터를 완료 버튼 눌렀을 시에 가져와야 수정된 정보를 반환받을 수 있음->modi_clear에서 해당 기능 수행
    #수정 전에 굳이 엔트리값을 반환반을 필요는 없어보임
    # in_data = [title.get(), author.get(), pub.get(), int(isbn.get()), int(price.get()), link.get(), description.get()]
    # print(in_data)

    #bt3_def를 연결하여 취소버튼을 누르면 메인메뉴로 돌아갈 수 있게 함
    book_new_win.under_button('완료', book_new_win.base_frame, bt2_def=modi_clear(ISBN), bt3_def=lambda:main_menu(window, book_new_win))
    

