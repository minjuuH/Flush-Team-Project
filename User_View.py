from tkinter import *
from tkinter import messagebox
from numpy import *
from pandas import isna, notna
import User_dataframe as UD
import UI_Class as UC

import Rent_View as rv
import Book_def as Bd

def search_info(win, t, bt_def=None, bt_button = None, chk:bool=1):
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    user_data = UD.user_dataframe()
    user_data.readcsv()
    search_data = user_data.searchdata(search, 1)   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
    win.info_list(t, bt_def, bt_button, 15, chk, 1, list = search_data)

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
    u_new_win = UC.new_window()
    if uc!=None:
        u_new_win=uc

    window.title('회원 조회')
    u_new_win.Change_Frame('회원 조회')

    u_new_win.User_list('확인', inwindow=window, check_choice=False, quit_choice=True, uc=u_new_win)#Quser=1로 받으면 탈퇴회원정보가 출력

#회원 조회창(수정)
def re_userwindow(window, uc=None):
    u_new_win = UC.new_window()
    userdata = UD.user_dataframe()
    userdata.readcsv()
    inlist = userdata.now_list(1)
    if uc!=None:
        u_new_win=uc

    window.title('회원 수정')
    u_new_win.Change_Frame('회원 수정')
    
    u_new_win.Search_bar(S_def=lambda:search_info(u_new_win, '수정', chk =  0, bt_button = [1, u_new_win]))
    u_new_win.User_list('수정',userlist = inlist, check_choice=False, command_def=[1, window], uc=u_new_win) #command_def = [window, 적용시킬 함수내용(1 = 수정, 2 = 탈퇴)] 

#회원 조회창(탈퇴)
def del_userwindow(window, uc=None):
    u_new_win = UC.new_window()
    userdata = UD.user_dataframe()
    userdata.readcsv()
    inlist = userdata.now_list(1)
    if uc!=None:
        u_new_win=uc

    window.title('회원 탈퇴')
    u_new_win.Change_Frame('회원 탈퇴')
              
    u_new_win.Search_bar(S_def = lambda:search_info(u_new_win, '탈퇴', None, [2, u_new_win], 0))
    #u_new_win.createButton('탈퇴', u_new_win.baseLabel)
    u_new_win.User_list('탈퇴',userlist = inlist, check_choice=False, command_def = [2, window], uc=u_new_win)

#회원 탈퇴 함수
def del_user(window, phone, where = True, uc=None):
    re_user = UD.user_dataframe()
    re_user.readcsv()
    ask = re_user.removedata(phone)
    re_user.tocsv()
    if ask:
        if where:
            del_userwindow(window, uc)
        else:
            userwindow(window, uc)
          
def reset_user(window, phone, uc=None):
    user = UD.user_dataframe()
    user.readcsv()
    ask = user.resetremove(phone)
    user.tocsv()
    if ask:
        userwindow(window, uc)

#회원 상세정보창
def userwindowinfo(window, userphone, uc=None, Quser=False):
    showuser = UD.user_dataframe()
    showuser.readcsv()
    showlist = showuser.userinfo(userphone)
    u_new_win = UC.new_window()
    if uc!=None:
        u_new_win=uc

    window.title('회원 정보')
    u_new_win.Change_Frame('회원 정보')

    u_new_win.input_set('회원 정보', 0, showimage = showlist[5])
    u_new_win.info_output('이름', 1, showlist[0])
    u_new_win.info_output('생년월일', 2, showlist[1])
    u_new_win.info_output('전화번호', 3, '0'+showlist[2])
    u_new_win.info_output('성별', 4, showlist[3])
    u_new_win.info_output('이메일', 5, showlist[4])
    if Quser:
        Q = Label(u_new_win.Base_Bottom, text='탈퇴회원입니다.', font=('돋움', 15), fg='red', bg='white')
        Q.pack(pady=50)
        u_new_win.under_button('복구', u_new_win.base_frame, bt2_def = lambda:reset_user(window, userphone, u_new_win), bt3_def=lambda:main_menu(window, u_new_win))
    else:
        u_new_win.user_rent()
        #u_new_win.under_button('탈퇴', u_new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:userwindowmodi(u_new_win, userphone,1), bt2_def= lambda:del_user(u_new_win, userphone), bt3_def=lambda:main_menu(window, u_new_win))
        u_new_win.under_button('탈퇴', u_new_win.base_frame, more=1, bt1_t='수정', bt1_def=lambda:userwindowmodi(window, userphone, u_new_win), bt2_def= lambda:del_user(window, userphone, uc=u_new_win), bt3_def=lambda:main_menu(window, u_new_win))

    
#회원 수정
def userwindowmodi(window, userphone, uc=None):
    modiuser = UD.user_dataframe()
    modiuser.readcsv()
    modiuserinfo = modiuser.modiuserinfo(userphone)
    u_new_win = UC.new_window()
    if uc!=None:
        u_new_win=uc

    window.title('회원 수정')
    u_new_win.Change_Frame('회원 수정')
    u_new_win.input_set('회원 수정',0 , showimage= modiuserinfo[5])
    nameentry = u_new_win.u_entry_set('이름', 1, True, modiuserinfo[0])
    birthentry = u_new_win.u_entry_set('생년월일', 2, True, modiuserinfo[1])
    phoneentry = u_new_win.u_entry_set('전화번호', 3, True, '0'+modiuserinfo[2], True)
    u_new_win.user_gender('성별', 5, modiuserinfo[3])
    emailentry = u_new_win.u_entry_set('이메일', 6, True, modiuserinfo[4])
    imageentry = u_new_win.u_entry_set('회원사진', 7, show= modiuserinfo[5], pic=True)
    
    def modiuserdata():
        modidata = [nameentry.get(), birthentry.get(), phoneentry.get()[1:], u_new_win.gender, emailentry.get(), str(imageentry.get())]
        ask = modiuser.modidata(modiuserinfo[2], modidata)
        modiuser.tocsv()
        if ask:
            userwindowinfo(window, modidata[2], uc=u_new_win)
    u_new_win.under_button('완료', u_new_win.base_frame, bt2_def=modiuserdata, bt3_def=lambda:main_menu(window, u_new_win))
#회원 등록
def userwindowadd(window, uc=None):
    adduser = UD.user_dataframe()
    adduser.readcsv()
    u_new_win = UC.new_window()
    if uc!=None:
        u_new_win=uc

    window.title('회원 등록')
    u_new_win.Change_Frame('회원 등록')

    u_new_win.input_set('회원 등록', 0)
    nameentry = u_new_win.u_entry_set('이름', 1)
    birthentry = u_new_win.u_entry_set('생년월일', 2, form=1)
    phoneentry = u_new_win.u_entry_set('전화번호', 3, ol=1)
    u_new_win.user_gender('성별', 5)
    emailentry = u_new_win.u_entry_set('이메일', 6)
    imageentry = u_new_win.u_entry_set('회원사진', 7, pic=True)
    def adduserdata():
        modidata = [nameentry.get(), birthentry.get(), phoneentry.get()[1:], u_new_win.gender, emailentry.get(), str(imageentry.get())]
        ask = adduser.add_data(modidata)
        adduser.tocsv()
        if ask:
            userwindowinfo(window, modidata[2], u_new_win)
    u_new_win.under_button('등록', u_new_win.base_frame, bt2_def=adduserdata, bt3_def=lambda:main_menu(window, u_new_win))
