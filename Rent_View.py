from tkinter import *
from tkinter import messagebox
from UI_Class import *
import Book_def as Bd
import User_View as uv
import Rent_Dataframe as RD
import pandas as pd
import datetime as dt

#실제로 사용할 함수
# def search_info(win, choice=True):
#     #choice->회원 정보에서 조회할 지, 도서 정보에서 조회할지 선택(True=회원, False=도서)
#     search = win.input_text.get()   #기입창에 입력한 데이터 추출
#     search_data = ['검색 후', search]   #search로 데이터 프레임에서 추출한 데이터 저장(추후 수정)
#     win.info_list(text_del=1, list=search_data)

#테스트용
def search_info(win, B_DataFrame, U_DataFrame, choice=True):
    search = win.input_text.get()   #기입창에 입력한 데이터 추출
    data = list()
    if choice:
        search_data = User_Search(U_DataFrame, search)
        for i in search_data.index:
            add_list = [search_data.loc[i,'USER_NAME'],search_data.loc[i,'USER_BIRTH'],search_data.loc[i,'USER_PHONE']]
            data.append(add_list)
    else:
        search_data = search_book(B_DataFrame, search)
        for i in search_data.index:
            add_list = [search_data.loc[i,'BOOK_TITLE'],search_data.loc[i,'BOOK_AUTHOR'],search_data.loc[i,'BOOK_PUB'],search_data.loc[i,'BOOK_ISBN']]
            data.append(add_list)

    win.info_list(text_del=1, list=data)

#회원 검색
def User_Search(u_DF, search):
    user = u_DF
    if(user['USER_PHONE'].str.contains(search).any()) or (user['USER_NAME'].str.contains(search).any()):
        # print('등록되어 있지 않은 회원입니다.')
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

#테스트를 위한 도서/회원 데이터 프레임------------------------------
#실제 사용 X -> 삭제해야할 내용
book = pd.DataFrame({'BOOK_ISBN':[9788970504773,9791163030911,9788966263301, 9791160507812], 
                     'BOOK_TITLE':['파이썬과 데이터 과학', '점프투파이썬', 'it 지식', '모두의 데이터분석'],
                     'BOOK_AUTHOR':['천인국, 박동규, 강영민', '박응용', '브라이언', '송석리, 이현아'], 
                     'BOOK_PUB':['생능출판사','이지스퍼블리싱','인사이트','길벗'], 
                     'BOOK_PRICE':[26000, 18800, 20000, 19000], 
                     'BOOK_LINK':['http://www.yes24.com','http://www.yes24.com','http://www.yes24.com','http://www.yes24.com'],
                     'BOOK_IMAGE':['py.png','jump.png','it.png','data.png'], 
                     'BOOK_DESCRIPTION':['파이썬 교재','파이썬 교재','it 교재','파이선 데이터 분석']})
# book = pd.DataFrame(columns=['BOOK_ISBN','BOOK_TITLE','BOOK_AUTHOR','BOOK_PUB','BOOK_PRICE','BOOK_LINK','BOOK_IMAGE','BOOK_DESCRIPTION'])

user = pd.DataFrame(columns=['USER_NAME','USER_BIRTH','USER_PHONE','USER_SEX','USER_MAIL','USER_IMEGE',
                             'USER_RENT_CNT', 'USER_QUIT_DATE', 'USER_RENT_ALW', 'USER_WARN'])
add_user = pd.DataFrame({'USER_NAME': ['이순신', '홍길동', '신사임당', '유관순', '장영실'],
                     'USER_BIRTH': [ "1999-01-01", "1973-03-21", "1988-08-15", "1920-02-02", "2000-12-25"],
                     'USER_PHONE': ['010-3965-4122', '010-1274-6349', '010-2910-0058',
                                   '010-9001-1004', '010-0308-1734'],
                     'USER_SEX': [True, True, False, False, True],
                     'USER_MAIL': ['lee0101@naver.com', 'hong0321@naver.com','sinsa0815@daum.net',
                                   'you0202@naver.com', 'hang1225@google.com'],
                     'USER_IMEGE': ['person1.png', 'person2.png','person3.png','person4.png','person5.png'],
                     'USER_RENT_CNT': [0, 0, 0, 0, 0],
                     'USER_WARN': [0, 0, 0, 0, 0]})
user = pd.concat([user, add_user])

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
        print(re_IF.re_book)
        if re_IF.re_user==None:
            messagebox.showwarning('도서관리시스템', '회원이 선택되지 않았습니다.')
        elif len(re_IF.re_book)==0:
            messagebox.showwarning('도서관리시스템', '반납할 도서를 선택해주십시오.')
        else:
            msg_Ans = messagebox.askokcancel('도서관리시스템', "반납하시겠습니까?")  #부울값 반환 -> ok:True, cancel:False
            if msg_Ans:
                re_IF.Rent_return()
                re_IF.to_csv()
                messagebox.showinfo('도서관리시스템', "반납 처리되었습니다.\n반납예정일:{}\n반납일:{}".format(re_IF.re_due_day, re_IF.re_day))
                Return_Screen(window, new_win)

    new_win.Choice_base()
    #회원 선택 버튼/선택한 회원 정보 출력
    new_win.Choice('회원 선택', 45, lambda:User_Choice(window, new_win, rent_info, True))
    #반납/취소 버튼
    new_win.under_button('반납', new_win.Base, bt3_def=lambda:main_menu(window, new_win), bt2_def=lambda:re_acc(rent_info,window,new_win))
    #대여 목록 출력
    new_win.rent_list()

#회원 선택 기능
def chkU_def(win, root_win, rent, re=False):
    if len(win.chk_list)==0:
        messagebox.showwarning("회원 선택", "회원을 선택하십니오.", parent=win.newWindow)
    elif len(win.chk_list)==1:
        root_win.userinfo.config(text=win.chk_list[0][0]+' | '+win.chk_list[0][1]+' | '+win.chk_list[0][2])
        if re:
            rent_DF = rent.existence(win.chk_list[0][2])
            rent.re_user = win.chk_list[0][2]   #반납할 회원 정보 rent 객체에 저장
            book_list = list()
            for i in rent_DF['BOOK_ISBN']:
                rent_book = rent.book[rent.book['BOOK_ISBN']==i]
                idx = rent_book.index
                book_list.append([rent_book.loc[idx[0],'BOOK_TITLE'],rent_book.loc[idx[0],'BOOK_AUTHOR'],rent_book.loc[idx[0],'BOOK_PUB'],rent_book.loc[idx[0],'BOOK_ISBN']])
            root_win.info_list(text_del=1, list=book_list)
        else:
            root_win.rentU_label.config(text="대여인:"+win.chk_list[0][0])
            rent.rent_user = win.chk_list[0][2] #대출정보에 사용할 회원 전화번호 데이터 저장
            root_win.rent_day.config(text="대여일:{}".format(dt.datetime.now().date()))
            root_win.re_day.config(text="반납예정일:{}".format(dt.datetime.now().date()+dt.timedelta(days=7)))
        win.newWindow.withdraw()
    else:
        messagebox.showwarning("회원 선택", "회원 선택은 1명만 가능합니다.", parent=win.newWindow)
        
#도서 선택 기능
def chkB_def(win, root_win, rent):
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
    root_win.re_day.config(text="반납예정일:{}".format(dt.datetime.now().date()+dt.timedelta(days=7)))
    win.newWindow.withdraw()

#회원 선택창
def User_Choice(window, root_win, rent, re=False):
    new_win = new_window()
    new_win.make_window(window, '회원 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win, book, user))
    #확인/취소 버튼
    new_win.under_button_R(lambda:chkU_def(new_win, root_win, rent, re))
    #회원 목록이 출력될 프레임
    user_list = list()      #user 출력형 리스트 생성
    #전체 user를 출력형 list에 append -> 탈퇴회원을 제외하고 출력하도록 변경할 것
    user = rent.user[rent.user['USER_QUIT_DATE'].isna()]    #탈퇴회원을 제외한 회원 목록
    for i in user.index:
        user_list.append([user.loc[i,'USER_NAME'],user.loc[i,'USER_BIRTH'],user.loc[i,'USER_PHONE']])
    new_win.list_print("\t이름\t\t생년월일\t전화번호", user_list)

#도서 선택창
def Book_Choice(window, root_win, rent):
    new_win = new_window()
    new_win.make_window(window, '도서 선택')
    #검색창 설정
    new_win.Search_bar(13, lambda:search_info(new_win, book, user, False))
    #확인/취소 버튼
    new_win.under_button_R(lambda:chkB_def(new_win, root_win, rent))
    #도서 목록이 출력될 프레임
    book_list = list()      #book 출력형 리스트 생성
    #전체 book를 출력형 list에 append -> 대출 중인 도서를 제외하고 출력하도록 변경할 것
    for i in rent.book.index:
        #대출 정보에 존재하는 도서인지 확인
        if not rent.rent['BOOK_ISBN'].isin([rent.book['BOOK_ISBN'][i]]).any():
            book_list.append([rent.book.loc[i,'BOOK_TITLE'],rent.book.loc[i,'BOOK_AUTHOR'],rent.book.loc[i,'BOOK_PUB'],rent.book.loc[i,'BOOK_ISBN']])
        #반납된 도서인지 확인
        elif not rent.rent[rent.rent['BOOK_ISBN']==rent.book['BOOK_ISBN'][i]]['RETURN_DATE'].isna().any():
            book_list.append([rent.book.loc[i,'BOOK_TITLE'],rent.book.loc[i,'BOOK_AUTHOR'],rent.book.loc[i,'BOOK_PUB'],rent.book.loc[i,'BOOK_ISBN']])
    new_win.list_print("\t제목\t저자\t출판사\tISBN\t대출여부", book_list)