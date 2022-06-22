from tkinter import *
from tkinter import messagebox
from UI_Class import *
import Book_def as Bd
import User_View as uv
import Rent_Dataframe as RD
import pandas as pd
import datetime as dt

#검색 시 사용할 커맨드
def search_info(win, B_DataFrame=None, U_DataFrame=None, choice=True):
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    data = list()
    if choice:
        search_data = User_Search(U_DataFrame, search)
        if len(search_data)!=0:
            for i in search_data.index:
                add_list = [search_data.loc[i,'USER_NAME'],search_data.loc[i,'USER_BIRTH'],search_data.loc[i,'USER_PHONE']]
                data.append(add_list)
    else:
        search_data = search_book(B_DataFrame, search)
        if len(search_data)!=0:
            for i in search_data.index:
                add_list = [search_data.loc[i,'BOOK_TITLE'],search_data.loc[i,'BOOK_AUTHOR'],search_data.loc[i,'BOOK_PUB'],search_data.loc[i,'BOOK_ISBN']]
                data.append(add_list)

    win.info_list(text_del=1, list=data)

#회원 검색
def User_Search(u_DF, search):
    user = u_DF
    if(user['USER_PHONE'].str.contains(search).any()) or (user['USER_NAME'].str.contains(search).any()):
        return user.loc[user['USER_PHONE'].str.contains(search) | user['USER_NAME'].str.contains(search)]
    else:
        return []
        #print(user.loc[user['USER_PHONE'].str.contains(search) | user['USER_NAME'].str.contains(search)])

#도서 검색
def search_book(b_DF, search):
    book = b_DF
    if book['BOOK_TITLE'].str.contains(search).any() or book['BOOK_AUTHOR'].str.contains(search).any():
        return book.loc[book['BOOK_TITLE'].str.contains(search) | book['BOOK_AUTHOR'].str.contains(search)]
        # print("조회 결과 : ")
        # print(book.loc[book['BOOK_TITLE'].str.contains(search) | book['BOOK_AUTHOR'].str.contains(search)]) 
    else:
        return []

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
    #print(user.loc[-1:0])
    new_win = new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 대출')
    new_win.Change_Frame('도서 대출')

    rent_info = RD.Rent_DF()
    rent_info.read_csv()

    #대출 기능
    def rent_acc(rent_IF, win, new_win):
        if len(rent_IF.rent_book)==0 or rent_IF.rent_user==None:
            messagebox.showwarning('도서관리시스템', '회원과 도서를 모두 선택해주십시오.')
        else:
            msg_Ans = messagebox.askokcancel('도서관리시스템', "대출하시겠습니까?")  #부울값 반환 -> ok:True, cancel:False
            if msg_Ans:
                rent_IF.Rent_Add()
                rent_IF.to_csv()
                rent_IF.add_rent.loc
                messagebox.showinfo('도서관리시스템', "대출 완료되었습니다.\n대여일:{}\n반납예정일:{}".format(rent_IF.add_rent.loc[0,'RENT_DATE'], rent_IF.add_rent.loc[0,'RETURN_DUE_DATE']))
                Rent_Screen(window, new_win)

    new_win.Choice_base()
    #회원 선택 버튼/선택한 회원 정보 출력
    new_win.Choice('회원 선택', 45, lambda:User_Choice(window, new_win, rent_info))
    #도서 선택 버튼/선택한 도서 정보 출력
    new_win.Choice('도서 선택', 200, lambda:Book_Choice(window, new_win, rent_info), False)
    #대출/취소 버튼
    new_win.under_button('대출', new_win.Base, bt3_def=lambda:main_menu(window, new_win), bt2_def=lambda:rent_acc(rent_info,window,new_win))
    #대출 정보 출력
    new_win.rent_info()

#도서 반납 화면
def Return_Screen(window, uc=None):
    new_win = new_window()
    if uc!=None:
        new_win=uc

    window.title('도서 대출')
    new_win.Change_Frame('도서 대출')

    rent_info = RD.Rent_DF()
    rent_info.read_csv()

    #반납 기능
    def re_acc(re_IF, win, new_win):
        for i in new_win.chk_list:
            re_IF.re_book.append(i[3])
        if re_IF.re_user==None:
            messagebox.showwarning('도서관리시스템', '회원이 선택되지 않았습니다.')
        elif len(re_IF.re_book)==0:
            messagebox.showwarning('도서관리시스템', '반납할 도서를 선택해주십시오.')
        else:
            msg_Ans = messagebox.askokcancel('도서관리시스템', "반납하시겠습니까?")  #부울값 반환 -> ok:True, cancel:False
            if msg_Ans:
                if re_IF.Rent_return():
                    re_IF.to_csv()
                    messagebox.showinfo('도서관리시스템', "반납 처리되었습니다.\n반납예정일:{}\n반납일:{}".format(re_IF.re_due_day, re_IF.re_day))
                else:
                    re_IF.to_csv()
                    messagebox.showinfo('도서관리시스템', "연체되었습니다.\n반납예정일:{}\n반납일:{}\n대출가능일:{}".format(re_IF.re_due_day, re_IF.re_day, re_IF.alw_day.strftime('%Y.%m.%d')))
                Return_Screen(window, new_win)

    new_win.Choice_base()
    #회원 선택 버튼/선택한 회원 정보 출력
    new_win.Choice('회원 선택', 45, lambda:User_Choice(window, new_win, rent_info, True))
    #반납/취소 버튼
    new_win.under_button('반납', new_win.Base, bt3_def=lambda:main_menu(window, new_win), bt2_def=lambda:re_acc(rent_info,window,new_win))
    #대여 목록 출력
    new_win.rent_list("{:>40s}{:>20s}{:>20s}{:>20s}{:>20s}".format('제목','저자','출판사','ISBN','반납예정일'))

#회원 선택 기능 -> 확인 버튼 클릭 시 수행
def chkU_def(win, root_win, rent, re=False):
    if len(win.chk_list)==0:    #선택된 회원이 없을 경우
        messagebox.showwarning("회원 선택", "회원을 선택하십니오.", parent=win.newWindow)
    elif len(win.chk_list)==1:  #한 명의 회원만 선택되었을 경우 -> 정상 작동
        if re:  #반납창에서 회원 선택을 수행할 경우
            rent_DF = rent.existence(win.chk_list[0][2])
            rent.re_user = win.chk_list[0][2]   #반납할 회원 정보 rent 객체에 저장
            book_list = list()
            for i in rent_DF['BOOK_ISBN']:
                #편의성을 위해 대출 도서 정보에 반납예정일을 띄워줌
                re_due_day = rent_DF.loc[rent_DF[rent_DF['BOOK_ISBN']==i].index[0], 'RETURN_DUE_DATE']
                rent_book = rent.book[rent.book['BOOK_ISBN']==i]
                idx = rent_book.index
                book_list.append([rent_book.loc[idx[0],'BOOK_TITLE'],rent_book.loc[idx[0],'BOOK_AUTHOR'],rent_book.loc[idx[0],'BOOK_PUB'],rent_book.loc[idx[0],'BOOK_ISBN'],re_due_day])
            root_win.info_list(text_del=1, list=book_list)
            root_win.userinfo.config(text=win.chk_list[0][0]+' | '+win.chk_list[0][1]+' | '+win.chk_list[0][2])
            win.newWindow.withdraw()
        elif rent.rent_allow(win.chk_list[0][2]):   #대출창에서 기능 수행&선택한 회원이 대출 가능한 상태일 경우
            root_win.rentU_label.config(text="대여인:"+win.chk_list[0][0])
            rent.rent_user = win.chk_list[0][2] #대출정보에 사용할 회원 전화번호 데이터 저장
            root_win.rent_day.config(text="대여일:{}".format(dt.datetime.now().date()))
            root_win.re_day.config(text="반납예정일:{}".format(dt.datetime.now().date()+dt.timedelta(days=14)))
            root_win.userinfo.config(text=win.chk_list[0][0]+' | '+win.chk_list[0][1]+' | '+win.chk_list[0][2])
            win.newWindow.withdraw()
        else:
            messagebox.showinfo('회원 선택', '연체된 회원은 대출이 불가합니다.', parent=win.newWindow)
    else:   #선택된 회원이 한 명을 초과한 경우
        messagebox.showwarning("회원 선택", "회원 선택은 1명만 가능합니다.", parent=win.newWindow)
        
#도서 선택 기능 -> 확인 버튼 클릭 시 수행
def chkB_def(win, root_win, rent):
    if len(win.chk_list)==0:    #선택된 도서가 없을 경우
        messagebox.showwarning("도서 선택", "도서가 선택되지 않았습니다.", parent=win.newWindow)
    else:
        rent.rent_book.clear()
        root_win.text.config(state=NORMAL)  #텍스트 위젯을 비워주기 위해 위젯 상태를 변경가능한 상태로 설정
        root_win.text.delete("1.0", "end")
        plus = 0
        for i in range(len(win.chk_list)):
            for j in win.chk_list[i]:
                root_win.text.insert('end', str(j)+' | ')
            root_win.text.insert('end', '\n')
            if i > 0:
                plus += 1
            rent.rent_book.append(win.chk_list[i][3])   #대출정보에 사용할 도서 ISBN 데이터 저장
        root_win.text.configure(state=DISABLED)
        if plus != 0:
            root_win.rentB_label.config(text="대출도서:{} 외 {}권".format(win.chk_list[0][0], plus))
        else:
            root_win.rentB_label.config(text="대출도서:{}".format(win.chk_list[0][0]))
        root_win.rent_day.config(text="대여일:{}".format(dt.datetime.now().date()))
        root_win.re_day.config(text="반납예정일:{}".format(dt.datetime.now().date()+dt.timedelta(days=14)))
        win.newWindow.withdraw()

#취소버튼 클릭시 확인창 -> 해당 기능이 실행된 창을 부모창으로 여기게끔 수정
def exit(showText, win=0):
        ask = messagebox.askquestion(showText, "취소하시겠습니까?", parent=win)
        if ask == 'yes':
            if win != 0:        #win의 인자를 전달받았을 경우(win이 0이 아닐 경우)
                win.withdraw()  #withdraw():Toplevel의 메소드. Toplevel()로 생성한 외부창을 화면에서 제거해준다.
        else:
            return

#회원 선택창
def User_Choice(window, root_win, rent, re=False):
    new_win = new_window()
    new_win.make_window(window, '회원 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win, U_DataFrame=user))   #탈퇴회원을 제외한 데이터프레임 전달
    #확인/취소 버튼
    new_win.under_button_R(lambda:chkU_def(new_win, root_win, rent, re), lambda:exit('회원 선택', new_win.newWindow))
    #회원 목록이 출력될 프레임
    user_list = list()      #user 출력형 리스트 생성
    #전체 user를 출력형 list에 append -> 탈퇴회원을 제외하고 출력하도록 변경할 것
    user = rent.user[rent.user['USER_QUIT_DATE'].isna()]    #탈퇴회원을 제외한 회원 목록
    for i in user.index:
        user_list.append([user.loc[i,'USER_NAME'],user.loc[i,'USER_BIRTH'],user.loc[i,'USER_PHONE']])
    new_win.list_print("{:>28s}{:>25s}{:>25s}".format('이름','생년월일','전화번호'), user_list)

#도서 선택창
def Book_Choice(window, root_win, rent):
    new_win = new_window()
    new_win.make_window(window, '도서 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win, book, choice=False)) #대출 중인 도서를 제외한 데이터프레임 전달
    #확인/취소 버튼
    new_win.under_button_R(lambda:chkB_def(new_win, root_win, rent), lambda:exit('도서 선택', new_win.newWindow))
    #도서 목록이 출력될 프레임
    book_list = list()      #book 출력형 리스트 생성
    book = pd.DataFrame()   #대출 중인 도서를 제외하고 저장할 데이터프레임 생성->검색 시 대상이 될 데이터 프레임
    #전체 book를 출력형 list에 append -> 대출 중인 도서를 제외하고 출력하도록 변경할 것
    for i in rent.book.index:
        #대출 정보에 존재하는 도서인지 확인
        if not rent.rent['BOOK_ISBN'].isin([rent.book['BOOK_ISBN'][i]]).any():
            #book = book.append(rent.book.loc[i:i])
            book = pd.concat([book, rent.book.loc[i:i]])
            book_list.append([rent.book.loc[i,'BOOK_TITLE'],rent.book.loc[i,'BOOK_AUTHOR'],rent.book.loc[i,'BOOK_PUB'],rent.book.loc[i,'BOOK_ISBN']])
        #반납된 도서인지 확인
        elif not rent.rent[rent.rent['BOOK_ISBN']==rent.book['BOOK_ISBN'][i]]['RETURN_DATE'].isna().any():
            book = pd.concat([book, rent.book.loc[i:i]])
            book_list.append([rent.book.loc[i,'BOOK_TITLE'],rent.book.loc[i,'BOOK_AUTHOR'],rent.book.loc[i,'BOOK_PUB'],rent.book.loc[i,'BOOK_ISBN']])
    new_win.list_print("{:>28s}{:>25s}{:>25s}{:>25}".format('제목','저자','출판사','ISBN'), book_list)