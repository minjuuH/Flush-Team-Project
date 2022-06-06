from tkinter import *
from tkinter import messagebox
import UI_Class as UC
import Rent_View as rv
import Book_def as Bd

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

    Book = Button(Base.base_frame, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:Bd.createNewWindow_book_s(window, uc=Base))
    User = Button(Base.base_frame, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:userwindow(window, uc=Base))
    Rent = Button(Base.base_frame, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window, uc=Base))

    Book.place(x=110, y=265)
    User.place(x=360, y=265)
    Rent.place(x=610, y=265)
    
#회원 조회창
def userwindow(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 조회')
    new_win.Change_Frame('회원 조회')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '확인', lambda:userwindowinfo(window, uc=new_win), 0))
    new_win.User_list('확인', check_choice=False, quit_choice=True, command_def=lambda:userwindowinfo(window, uc=new_win,Quser=1))#Quser=1로 받으면 탈퇴회원정보가 출력

#회원 조회창(수정)
def re_userwindow(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 수정')
    new_win.Change_Frame('회원 수정')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '수정', lambda:userwindowmodi(window, uc=new_win), 0))
    new_win.User_list('수정', check_choice=False, command_def=lambda:userwindowmodi(window, uc=new_win))

#회원 조회창(탈퇴)
def del_userwindow(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 탈퇴')
    new_win.Change_Frame('회원 탈퇴')

    new_win.Search_bar(S_def=lambda:search_info(new_win, '탈퇴'))
    new_win.createButton('탈퇴', new_win.baseLabel)
    new_win.User_list('탈퇴')
    
#회원 상세정보창
def userwindowinfo(window, uc=None, Quser=False):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 정보')
    new_win.Change_Frame('회원 정보')

    new_win.input_set('회원 정보', 0)
    new_win.info_output('이름', 1)
    new_win.info_output('생년월일', 2)
    new_win.info_output('전화번호', 3)
    new_win.info_output('성별', 4)
    new_win.info_output('이메일', 5)
    if Quser:
        Q = Label(new_win.Base_Bottom, text='탈퇴회원입니다.', font=('돋움', 15), fg='red', bg='white')
        Q.pack(pady=50)
        new_win.under_button('복구', new_win.base_frame)
    else:
        new_win.user_rent()
        new_win.under_button('탈퇴', new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:userwindowmodi(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))
    
    
#회원 수정
def userwindowmodi(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 수정')
    new_win.Change_Frame('회원 수정')

    new_win.input_set('회원 수정')
    new_win.entry_set('이름', 1, True)
    new_win.entry_set('생년월일', 2, True)
    new_win.entry_set('전화번호', 3, True, True)
    new_win.user_gender('성별', 5, True)
    new_win.entry_set('이메일', 6, True)
    new_win.under_button('완료', new_win.base_frame, bt2_def=lambda:userwindowinfo(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))

#회원 등록
def userwindowadd(window, uc=None):
    new_win = UC.new_window()
    if uc!=None:
        new_win=uc

    window.title('회원 등록')
    new_win.Change_Frame('회원 등록')

    new_win.input_set('회원 등록')
    new_win.entry_set('이름', 1)
    new_win.entry_set('생년월일', 2, form=1)
    new_win.entry_set('전화번호', 3, ol=1)
    new_win.user_gender('성별', 5)
    new_win.entry_set('이메일', 6)
    new_win.under_button('등록', new_win.base_frame, bt2_def=lambda:userwindowinfo(window, uc=new_win), bt3_def=lambda:main_menu(window, new_win))
    
#회원 삭제 
# def userwindowremove(window):
#     user = windowtool('탈퇴 회원', window)
#     mb.MenuBar(user.window)
#     cast = user.labeltool(user.window)
#     cast.pack()
    
#     Topframe = Frame(cast)
#     Topframe.pack(side = TOP, expand=True)
#     Bottomframe = Frame(cast)
#     Bottomframe.pack(side = BOTTOM, expand=True)

#     userimage = user.labeltool(Topframe, color = 'white', x = 20, y = 15)
#     userinfo = user.labeltool(Topframe, color = 'white', x = 100, y = 15)
#     backbutton = user.buttontool(Bottomframe, '복구', incommand = buttonevent)
#     Nobutton = user.buttontool(Bottomframe, '취소', incommand = buttonevent)

#     userimage.pack(side = LEFT, padx = 5, pady = 10)
#     userinfo.pack(side = LEFT, padx = 5, pady = 10)
#     backbutton.pack(side = LEFT,  padx = 5, pady = 10)
#     Nobutton.pack(side = LEFT, padx = 5, pady = 10)
