from tkinter import *
from tkinter import messagebox
from UI_Class import *
import Book_def as Bd
import User_View as uv
#import Rent_Dataframe as RD

def search_info(win, choice=True):
    #choice->회원 정보에서 조회할 지, 도서 정보에서 조회할지 선택(True=회원, False=도서)
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    search_data = ['검색 후', search]   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
    win.info_list(text_del=1, list=search_data)

def main_menu(window:Tk, uc=None):
    Base = new_window()
    if uc!=None:
        Base=uc

    window.title('도서관리시스템')
    Base.Change_Frame('도서관리시스템')

    Book = Button(Base.base_frame, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:Bd.createNewWindow_book_s(window, uc=Base))
    User = Button(Base.base_frame, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:uv.userwindow(window, uc=Base))
    Rent = Button(Base.base_frame, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: Rent_Screen(window, uc=Base))

    Book.place(x=110, y=265)
    User.place(x=360, y=265)
    Rent.place(x=610, y=265)

#---------------------------------창 화면 설계---------------------------------
#도서 대출 화면
def Rent_Screen(window, uc=None):
    new_win = new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 대출')
    new_win.Change_Frame('도서 대출')

    new_win.Choice_base()
    #회원 선택 버튼/선택한 회원 정보 출력
    new_win.Choice('회원 선택', 45, User_Choice)
    #도서 선택 버튼/선택한 도서 정보 출력
    new_win.Choice('도서 선택', 200, Book_Choice)
    #대출 정보 출력
    new_win.rent_info()
    #대출/취소 버튼
    new_win.under_button('대출', new_win.Base, bt3_def=lambda:main_menu(window, new_win))

#도서 반납 화면
def Return_Screen(window, uc=None):
    new_win = new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 대출')
    new_win.Change_Frame('도서 대출')

    new_win.Choice_base()
    #회원 선택 버튼/선택한 회원 정보 출력
    new_win.Choice('회원 선택', 45, User_Choice)
    #반납/취소 버튼
    new_win.under_button('반납', new_win.Base, bt3_def=lambda:main_menu(window, new_win))
    #대여 목록 출력
    new_win.rent_list()

# def Rent_info(rb, ru):
#     data = RD.Rent_DF()
#     data.read_csv()

#     data.Rent_Add(rb, ru)
#     R_book = []
    
#     for i in range(len(data.book)):
#         if (data.book['BOOK_ISBN'][i]==data.add_rent['BOOK_ISBN']).any():
#             R_book.append(data.book['BOOK_TITLE'][i])

#회원 선택창
def User_Choice(window):
    new_win = new_window()
    new_win.make_window(window, '회원 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win))
    #확인/취소 버튼
    new_win.under_button_R()
    #회원 목록이 출력될 프레임
    new_win.list_print("\t이름\t생년월일\t전화번호")

#도서 선택창
def Book_Choice(window):
    new_win = new_window()
    new_win.make_window(window, '도서 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win))
    #확인/취소 버튼
    new_win.under_button_R()
    #회원 목록이 출력될 프레임
    new_win.list_print("\t제목\t저자\t출판사\tISBN\t대출여부")