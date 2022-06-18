from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import Book_class as bc
import User_dataframe as ud
import User_View as uv
import pandas as pd

class new_window:
    #생성자
    def __init__(self):
        self.newWindow = None       #이후에 Toplavel 객체를 저장할 변수 지정
        self.base_frame = None      #이후에 화면의 베이스가 되는 프레임 객체를 저장할 변수 지정

    #외부창 생성(외부창이 아닐 경우에 사용)
    def make_window(self, base_win, title):
        self.newWindow = Toplevel(base_win)
        self.newWindow.title(title)
        self.newWindow.geometry("800x600")
        self.newWindow.resizable(width=False, height=False)
        self.make_Frame()
    
    #목록 베이스가 되는 프레임 객체 생성(따로 추가한 함수)
    def make_label(self, base_win):
        self.label = Label(base_win, relief="ridge", height=37, bg='white')
        self.label.pack(fill=BOTH, expand=True)
        
    def Change_label(self, base_win):
        self.label.destroy()
        self.make_label(base_win)

    #창 화면의 베이스가 되는 프레임 객체 생성
    def make_Frame(self, parent=None):
        if parent==None:
            self.parent = self.newWindow
        else:
            self.parent = parent
        self.base_frame = Frame(self.parent)
        self.base_frame.pack(fill=BOTH, expand=True)

    #창의 프레임 전환을 위한 함수(외부창일 경우에 사용)
    def Change_Frame(self, title=None):
        if self.base_frame != None:
            self.base_frame.destroy()
            #self.newWindow.title(title)
        self.make_Frame()

    #검색바 설정
    def Search_bar(self, font_size=20, S_def=None):
        #S_def : 검색 클릭 시 조회 된 데이터를 출력해주는 함수
        self.baseLabel = Label(self.base_frame)
        self.baseLabel.pack()
        self.input_text = Entry(self.baseLabel, width=40, font=('돋움', font_size+2))
        self.input_text.pack(side=LEFT, padx=5, pady=5)
        S_button = Button(self.baseLabel, text="검색", font=('돋움', font_size), bg='gray', fg='white', command=S_def)
        S_button.pack(side=LEFT, padx=5, pady=5)
    
    #회원 검색어로 찾은 검색 결과를 회원 목록에 올리기 위한 작업용 함수(아래 UserSearch_bar와 병행) 
    def Searchshow(self, search, bt_text, bt_window, check_choice=True, uc=None):
            userdata = ud.user_dataframe()
            userdata.readcsv()
            searchlist = userdata.searchdata(search)
            self.userinfo_list(bt_text, searchlist, bt_window , 15, check_choice, 1, uc)

    #회원 검색바(Search_bar와 따로 만듬)        
    def UserSearch_bar(self, bt_text, bt_window, check_choice=True,font_size=20, uc=None):
        self.baseLabel = Label(self.base_frame)
        self.baseLabel.pack()
        input_text = Entry(self.baseLabel, width=40, font=('돋움', font_size+2))
        input_text.pack(side=LEFT, padx=5, pady=5)
        S_button = Button(self.baseLabel, text="검색", font=('돋움', font_size), bg='gray', fg='white', command=lambda:self.Searchshow(input_text.get(), bt_text, bt_window, check_choice, uc))
        S_button.pack(side=LEFT, padx=5, pady=5)
        

    #화면 구성을 위한 베이스 프레임[대출]
    def Choice_base(self):
        self.Base = Frame(self.base_frame, relief="solid", bd=1)     #bd : 테두리 굵기 설정
        self.Base.pack(fill=BOTH, pady=50, expand=True)

    #회원/도서 선택창[대출]
    def Choice(self, button_text, h, CM, user=True):
        listLabel = Label(self.Base, bg="white", height=50)
        listLabel.pack(fill=X, expand=True, anchor=N)
        userChoice = Button(listLabel, text=button_text, font=('돋움', 20), bg='gray', fg='white', command=CM)
        userChoice.pack(side=LEFT, padx=5, pady=5)
        userlist = Frame(listLabel, relief="solid", height=h, bd=1, bg='white') #회원 정보를 출력할 자리 frame으로 지정
        userlist.pack(fill=X, padx=5, pady=5, expand=True)
        userlist.propagate(0)  #frame 크기를 고정시켜 줌
        if user:
            self.userinfo = Label(userlist, font=('돋움', 15), bg='white')
            self.userinfo.pack(side=LEFT, ipadx=5)
        else:
            self.text_set(userlist)
            self.text.configure(state=DISABLED)
            # self.bookinfo = Label(userlist, font=('돋움', 15), bg='white', anchor=NW, justify=LEFT)
            # self.bookinfo.pack(side=LEFT, ipadx=5, ipady=5, fill=BOTH, expand=True)

    #대출 정보 출력[대출]
    def rent_info(self):
        frame_B = Frame(self.Base, height=280)
        frame_B.pack(fill=BOTH, expand=True, ipady=100)
        frame_B.propagate(0)  #frame 크기를 고정시켜 줌
        self.rentB_label = Label(frame_B, text="대출도서:", font=('돋움', 15))
        self.rentU_label = Label(frame_B, text="대여인:", font=('돋움', 15))
        self.rent_day = Label(frame_B, text="대여일:", font=('돋움', 15))
        self.re_day = Label(frame_B, text="반납예정일:", font=('돋움', 15))
        self.rentB_label.pack(fill=X, expand=True)
        self.rentU_label.pack(fill=X, expand=True)
        self.rent_day.pack(fill=X, expand=True)
        self.re_day.pack(fill=X, expand=True)

    #최종 버튼(가운데 정렬)
    def under_button(self, bt2_t, base, more=False, bt1_t=None, bt1_def=None, bt2_def=None, bt3_def=None):
        #more=True일 경우 버튼 3개 출력 / 추가되는 버튼은 command 함수를 따로 받아서 처리(bt1_def)
        buttonBase = Label(base, height=50)
        buttonBase.pack(side=BOTTOM)
        if more:
            bt1 = Button(buttonBase, text=bt1_t, font=('돋움', 20), bg='gray', fg='white', command=bt1_def)
            bt1.pack(side=LEFT, padx=5, pady=5)
        if bt2_def==None:
            bt2 = Button(buttonBase, text=bt2_t, font=('돋움', 20), bg='gray', fg='white', command=lambda:msg(bt2_t))
        else:
            bt2 = Button(buttonBase, text=bt2_t, font=('돋움', 20), bg='gray', fg='white', command=bt2_def)
        bt3 = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=bt3_def)
        bt2.pack(side=LEFT, padx=5, pady=5)
        bt3.pack(side=LEFT, padx=5, pady=5)

    #최종 버튼(오른쪽 정렬)[대출-회원/도서 선택]
    def under_button_R(self, chk_def=None, cancel_def=None):
        buttonBase = Label(self.base_frame, height=20)
        buttonBase.pack(side=BOTTOM, fill=X)
        CancelButton = Button(buttonBase, text="취소", font=('돋움', 13), bg='gray', fg='white', command=cancel_def)
        CancelButton.pack(side=RIGHT, padx=5, pady=5)
        RentButton = Button(buttonBase, text="확인", font=('돋움', 13), bg='gray', fg='white', command=chk_def)
        RentButton.pack(side=RIGHT, padx=5, pady=5)

    def text_set(self, frame, font_size=13):
        sb = Scrollbar(frame)
        self.text = Text(frame, width=40, height=20, yscrollcommand=sb.set, font=('돋움', font_size), spacing1=3, spacing2=3, spacing3=3, padx=10)    #spacing1~3:줄 사이 간격 지정
        sb.config(command=self.text.yview)
        sb.pack(side=RIGHT, fill=Y)
        self.text.pack(side=TOP, fill=BOTH, expand=True, ipadx=5)

    #선택한 회원의 대출 목록을 출력시켜주는 함수[대출]
    def rent_list(self):
        rentlist = Label(self.Base, bg="white", text="  대여 목록", font=('돋움', 15), anchor=NW)
        rentlist.pack(fill=X)
        listLabel2 = Label(self.Base, bg="white")
        listLabel2.pack(fill=BOTH, expand=True)
        booklist = Frame(listLabel2, relief="solid", height=450, bd=1)          #대여 목록을 출력할 자리 frame으로 지정
        booklist.pack(fill=BOTH, padx=5, pady=5)
        self.text_set(booklist)
        self.info_list()

    #체크박스 리스트 형식으로 출력
    def check_list(self, frame, font_size=13):
        sb = Scrollbar(frame)
        text = Text(frame, width=40, height=20, yscrollcommand=sb.set, font=('돋움', font_size), spacing1=3, spacing2=3, spacing3=3)    #spacing1~3:줄 사이 간격 지정
        sb.config(command=text.yview)
        sb.pack(side=RIGHT, fill=Y)
        text.pack(side=TOP, fill=BOTH, expand=True)

        # if len(list)==0:  #출력할 데이터가 존재하지 않을 경우
        #     text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n')
        #     lb = Label(text, text='등록된 정보가 없습니다.', font=('돋움', 13), bg='white', anchor=CENTER, width=90)
        #     text.window_create("end", window=lb)
        # else:             #출력할 데이터가 존재할 경우
            # for i in range(30):
            #     #cb = Checkbutton(text, text=list, font=('돋움', 13), bg='white')
            #     cb = Checkbutton(text, bg='white', font=('돋움', font_size))
            #     text.window_create("end", window=cb)
            #     text.insert('end', '도서 정보\n')   
        text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n')
        lb = Label(text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
        text.window_create("end", window=lb)
        text.configure(state=DISABLED)  #텍스트를 수정하지 못하게 상태 변경
    #추가해야하는 기능 : 검색했을 때 출력된 텍스트 목록 비우고 검색된 정보만 출력하도록 설정/출력할 정보를 인자로 받아야함
        
    #리스트를 출력해주는 함수[도서/회원]
    def info_list(self, bt_text=None, bt_def=None, bt_buttonlambda = None, font_size=13, choice=True, text_del=False, list=[], uc=None):
        #choice가 True일 경우 체크박스를 출력해줌 / text_del=True이면 텍스트 박스를 비워줌
        if bt_buttonlambda != None:
            bt_buttonlambda.append(self)
        
        if text_del:
            self.text.config(state=NORMAL)  #텍스트 위젯을 비워주기 위해 위젯 상태를 변경가능한 상태로 설정
            self.text.delete("1.0", "end")

        cb_list = []        #체크박스 리스트(각 줄마다 다른 데이터를 반환 받기 위해)
        self.chk_list = []       #체크박스를 클릭할 시 반환받는 값을 저장할 리스트

        def chk_command(i):
            if cb_list[i].get() != 0:
                self.chk_list.append(list[i])
            else:
                if list[i] in self.chk_list:
                    self.chk_list.remove(list[i])

        if len(list)==0:  #출력할 데이터가 존재하지 않을 경우
            self.text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n')
            lb = Label(self.text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
            self.text.window_create("end", window=lb)
        else:             #출력할 데이터가 존재할 경우
            for i in range(len(list)):
                if choice:
                    chk = IntVar()
                    cb_list.append(chk)
                    cb = Checkbutton(self.text, bg='white', font=('돋움', font_size), variable=cb_list[i], command=lambda x=i:chk_command(x))
                    self.text.window_create("end", window=cb)
                for j in range(len(list[i])):
                    self.text.insert('end', " {} ".format(list[i][j]))             #입력할 정보는 추후에 인자로 받아올 것
                    #줄이 넘어가는 것을 방지하기 위해 마지막 데이터 뒤에는 "\t\t\t"을 삽입하지 않도록 설정
                    if j!=len(list[i])-1:
                        self.text.insert('end', "\t\t\t")                
                if bt_text!=None:
                    if bt_buttonlambda == None:
                        bt = Button(self.text, text=bt_text, font=('돋움', font_size-3), command=bt_def)        # <- 원본
                    else:
                        bt = self.userButton(self.text, bt_text, font_size, bt_buttonlambda, list[i][2], uc)
                    self.text.window_create('end', window=bt)
                self.text.insert('end', '\n')
        self.text.configure(state=DISABLED)  #텍스트를 수정하지 못하게 상태 변경
    #추가해야하는 기능 : 검색했을 때 출력된 텍스트 목록 비우고 검색된 정보만 출력하도록 설정/출력할 정보를 인자로 받아야함
 
    
    def userButton(self,window, showText, font_size,def_info, phone, uc):
        if def_info[0] == 1:
            button = Button(window, text=showText, font=('돋움', font_size-3), command=lambda x=def_info[1], y = phone:uv.userwindowmodi(x, y, uc))
            return button
        elif def_info[0] == 2:
            button = Button(window, text=showText, font=('돋움', font_size-3), command=lambda x=def_info[1], y = phone:uv.del_user(x, y, uc=uc))
            return button
    
    #회원 리스트를 출력해주는 함수(회원 조회용)
    def userinfo_list(self, bt_text, bt_list, bt_window, font_size=13, choice=True, text_del = False, uc=None):
        if text_del:
            self.text.config(state=NORMAL)  #텍스트 위젯을 비워주기 위해 위젯 상태를 변경가능한 상태로 설정
            self.text.delete("1.0", "end")
        
        if len(bt_list)==0:  #출력할 데이터가 존재하지 않을 경우
            self.text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n')
            lb = Label(self.text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
            self.text.window_create("end", window=lb)
        else:
            for i in range(len(bt_list)):
                if choice:
                    cb = Checkbutton(self.text, bg='white', font=('돋움', font_size))
                    self.text.window_create("end", window=cb)
                self.text.insert('end', bt_list[i][0]+'\t\t'+bt_list[i][1]+'\t\t'+bt_list[i][2]+'\t\t'+bt_list[i][3])             #입력할 정보는 추후에 인자로 받아올 것
                bt = Button(self.text, text=bt_text, font=('돋움', font_size-3), command=lambda x = bt_list[i][2], y = bt_list[i][4]:uv.userwindowinfo(bt_window, x, uc, Quser=y))
                self.text.window_create('end', window=bt)
                self.text.insert('end', '\n')
        self.text.configure(state=DISABLED)  #텍스트를 수정하지 못하게 상태 변경
    #추가해야하는 기능 : 검색했을 때 출력된 텍스트 목록 비우고 검색된 정보만 출력하도록 설정/출력할 정보를 인자로 받아야함 << 회원 조회창에 있는 검색바 지우고 여기에 추가해서 넣었습니다.
    
    # 도서 데이터 출력 - 메인 UI_Class에 없는 함수
    def Book_info_list(self, out_data, bt_text=None, font_size=13, command_def=None, choice=True, text_del=True) :
        if text_del:
            self.text.config(state=NORMAL)
            self.text.delete('1.0', 'end')

        if len(out_data)==0:  #출력할 데이터가 존재하지 않을 경우
            self.text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n')
            lb = Label(self.text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
            self.text.window_create("end", window=lb)

        else:             #출력할 데이터가 존재할 경우
            for i in range(len(out_data)):
                if choice:
                    cb = Checkbutton(self.text, bg='white', font=('돋움', font_size))
                    self.text.window_create("end", window=cb)
                self.text.insert('end', out_data[i])             #입력할 정보는 추후에 인자로 받아올 것
                if bt_text!=None:
                    bt = Button(self.text, text=bt_text, font=('돋움', font_size-3), command=command_def)
                    self.text.window_create('end', window=bt)
                self.text.insert('end', '\n')
        self.text.configure(state=DISABLED)  #텍스트를 수정하지 못하게 상태 변경

    #도서 목록 출력[도서]
    def Book_list(self, bar_text, bt_text, book_data,command_def=None, choice=True):   #choice->리스트 앞에 체크박스 존재 여부를 결정(True:체크박스 설정)
        label_bar = Label(self.base_frame, relief="ridge", height=2, bg='white', text=bar_text, font=('돋움', 15), anchor=E)
        label_bar.pack(fill=X)
        label = Label(self.base_frame, relief="ridge", height=37, bg='white')
        label.pack(fill=BOTH, expand=True)
        self.text_set(label, 15)
        self.Book_info_list(book_data, bt_text, 15, command_def, choice)
    
    
    # #도서 목록 출력[도서]
    # def Book_list(self, bar_text, bt_text, command_def=None, choice=True):   #choice->리스트 앞에 체크박스 존재 여부를 결정(True:체크박스 설정)
    #     label_bar = Label(self.base_frame, relief="ridge", height=2, bg='white', text=bar_text, font=('돋움', 15), anchor=E)
    #     label_bar.pack(fill=X)
    #     label = Label(self.base_frame, relief="ridge", height=37, bg='white')
    #     label.pack(fill=BOTH, expand=True)
    #     self.text_set(label, 15)
    #     self.info_list(bt_text, command_def, font_size=15, choice=choice)

    #회원, 도서 목록 리스트 출력[대출]
    def list_print(self, bar_text, list=[]):   #list:출력할 정보 리스트
        listFrame = Frame(self.base_frame, relief="solid", height=50, bd=1, bg="white")
        listFrame.pack(fill=BOTH, expand=True)

        labelBar = Label(listFrame, bg="white", relief='ridge', text=bar_text, font=('돋움', 13), anchor=W)
        labelBar.pack(fill=BOTH)

        self.text_set(listFrame)
        self.info_list(list=list)

    #버튼 생성[도서,회원]
    def createButton(self, showText, window, bt_def=None):   #window=self.baseLabel
        button = Button(window, text=showText, font=('돋움', 20), bg='gray', fg='white', command=bt_def)
        button.pack(side=LEFT, padx=2, pady=10)



    #회원 목록 출력[회원]
    def User_list(self, bt_text, userlist=None, inwindow = None, command_def = None, check_choice=True, quit_choice = False, t_d=False, uc=None):
        #check_choice:체크버튼 출력 여부를 지정 / quit_choice:탈퇴회원 출력 여부를 지정(탈퇴회원도 출력한다면, 체크버튼으로 탈퇴/일반 회원을 선택할 수 있게 함)
        if quit_choice:
            self.UserSearch_bar(bt_text, inwindow, uc=uc)
        userdata = ud.user_dataframe()
        userdata.readcsv()
        showlist = []
        choiceBar = Label(self.base_frame, relief="ridge", bg='white')
        label_bar = Label(self.base_frame, relief="ridge", height=2, bg='white', text="이름\t\t생년월일\t\t전화번호     ", font=('돋움', 15), anchor=W)
        choiceBar.pack(fill=X)
        label_bar.pack(fill=X)
        

        #체크 여부에 따라 회원 출력 목록을 지정해 줄 함수
        def quitUser():
            #경우에 따라 데이터를 추가하는 방삭이면 마지막 else 문은 필요 X
            #당장 출력할 데이터를 지정해주는 것이 아닌, info_list구문에서 논리적인덱싱을 사용할 것이라면 마지막 else 문도 필요..?
            if chk1.get()==0 and chk2.get()==0:
                #출력할 데이터가 존재하지 X
                messagebox.showinfo("선택X", "해당하는 회원이 없습니다.")
                showlist = []
                self.userinfo_list(bt_text, showlist, inwindow, 15, check_choice, 1, uc)
            elif chk1.get()==0:
                #출력할 데이터에 탈퇴 회원 추가(탈퇴일 필드가 채워져 있으면 탈퇴회원)
                showlist = userdata.re_list()
                self.userinfo_list(bt_text, showlist, inwindow, 15, check_choice, 1, uc)
                #new_win.User_list('확인', check_choice=False, quit_choice=True, command_def=lambda:userwindowinfo(new_win,1,Quser=0))
            elif chk2.get()==0:
                #출력할 데이터에 일반 회원 추가
                showlist = userdata.now_list()
                self.userinfo_list(bt_text, showlist, inwindow, 15, check_choice, 1, uc)
                #self.userinfo_list(bt_text, showlist, command_def, 15, check_choice, 1)
            else:
                showlist = userdata.all_list()
                self.userinfo_list(bt_text, showlist, inwindow, 15, check_choice, 1, uc)

        if quit_choice:
            chk1=IntVar()
            chk2=IntVar()
            Check = Checkbutton(choiceBar, text="일반회원", font=('돋움', 13), variable=chk1, bg="white", command=quitUser)
            QuitCheck = Checkbutton(choiceBar, text="탈퇴회원", font=('돋움', 13), variable=chk2, bg="white", command=quitUser)
            Check.pack(side=RIGHT, pady=10)
            QuitCheck.pack(side=RIGHT)
            label = Label(self.base_frame, relief="ridge", height=37, bg='white')
            label.pack(fill=BOTH, expand=True)
            self.text_set(label, 15)
            self.userinfo_list(bt_text, showlist, inwindow, 15, check_choice, uc=uc)
        else:
            label = Label(self.base_frame, relief="ridge", height=37, bg='white')
            label.pack(fill=BOTH, expand=True)
            self.text_set(label, 15)
            self.info_list(bt_text, bt_buttonlambda = command_def, font_size = 15, choice= check_choice, list = userlist, uc=uc)

    #등록/수정/정보 화면 설정[도서/회원] showimage = 사진 주소(파일 경로)
    def input_set(self, t, open=True, showimage = '사진등록'):
        txt = Label(self.base_frame, text=t, font=('돋움', 20, 'bold'))
        txt.pack(anchor=NW, padx=10, pady=5)
        self.Base = Frame(self.base_frame, relief='solid', bg='white', bd=2)
        self.Base.pack(fill=BOTH, pady=10, expand=True)
        #위젯 배치에 편리성을 더하기 위해 상단부와 하단부를 나눠줌
        self.Base_Top = Label(self.Base, bg='white', height=60)
        self.Base_Top.pack(fill=X, side=TOP, anchor=N)
        self.Base_Bottom = Frame(self.Base, bg='white', height=60)
        self.Base_Bottom.pack(fill=X, side=TOP, anchor=N)

        #사진 입력 부분
        pic_base = Label(self.Base_Top, bg='white')
        pic_base.grid(row=0, column=0, rowspan=20)
        pic_frame = Frame(pic_base, width=180, height=220, relief='solid', bd=1)
        pic_frame.pack(anchor=NW, padx=30, pady=30, expand=True, side=TOP)
        pic_frame.propagate(0)  #frame 크기를 고정시켜 줌
        pic = Label(pic_frame, text='사진등록', font=('돋움', 15))
        pic.pack(fill= 'both', expand=True)
        if (showimage != '사진등록'):
            if(showimage != None):
                picture = PhotoImage(file = showimage)
                pic.configure(image=picture)
                pic.image = picture
        if open:
            pic_bt = Button(pic_base, text='사진 선택', font=('돋움', 13))
            pic_bt.pack(fill=X, padx=30)
            
            
            
        
        #빈레이블로 사용하지 않을 부분 채워주기
        x_label = Label(self.Base_Top, height=1, bg='white')
        x_label.grid(row=0, column=1)
        
    #입력칸 생성[도서/회원] <- 원본
    def entry_set(self, t, r, re_choice=False, ol=False, form=False):
        #t = 칸 제목, show = 데이터 정보
        txt = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)     #sticky : 지정된 칸 크기가 위젯 크기보다 클 경우, 정렬 방식을 지정
        entry = Entry(self.Base_Top, width=55, font=('돋움', 13), relief='solid', bd=1)
        if re_choice:
            entry.insert(0, '기존정보') #차후에 전달받은 데이터를 출력하는 것으로 변경
        entry.grid(row=r, column=2, padx=5, ipady=3, columnspan=3)

        #입력서식 표시
        if form:
            input_form = Label(self.Base_Top, text='ex) 0000-00-00', font=('돋움', 13), bg='white', fg='gray')
            input_form.grid(row=r, column=5)

        #중복 입력할 수 없는 데이터에 한해서 실행
        if ol==True:
            overlap_bt = Button(self.Base_Top, text='중복확인', font=('돋움', 13))
            overlap_bt.grid(row=r, column=5)
            check_overlap = Label(self.Base_Top, text='중복확인을 위한 레이블입니다.', fg='blue', font=('돋움', 13), bg='white')
            check_overlap.grid(row=r+1, column=2, sticky=W, columnspan=2)
     
         #입력칸 생성[도서/회원]
    def book_entry_set(self, t, r, re_choice=False, ol=False, text_data=None):
        book_class = bc.Book_DataFrame()
        txt = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)     #sticky : 지정된 칸 크기가 위젯 크기보다 클 경우, 정렬 방식을 지정
        if t == '가격' or t == 'ISBN':
            get_data = IntVar()

        else:
            get_data = StringVar()
        entry = Entry(self.Base_Top, width=55, textvariable= get_data, font=('돋움', 13), relief='solid', bd=1)
        if re_choice:
            entry.insert(0, text_data) #차후에 전달받은 데이터를 출력하는 것으로 변경
        entry.grid(row=r, column=2, padx=5, ipady=3, columnspan=3)
        if ol==True: 
            def com_isbn() : # 중복확인
                if entry.get() in str(book_class.book['BOOK_ISBN']): # ISBN 중복시
                    self.check_overlap = Label(self.Base_Top, text='이미 등록되어 있는 ISBN입니다.', fg='red', font=('돋움', 13), bg='white')
                    self.check_overlap.grid(row=r+1, column=2, sticky=W, columnspan=2)
                else:
                    self.check_overlap = Label(self.Base_Top, text='등록가능한 ISBN입니다.\t\t', fg='blue', font=('돋움', 13), bg='white')
                    self.check_overlap.grid(row=r+1, column=2, sticky=W, columnspan=2)

            self.overlap_bt = Button(self.Base_Top, text='중복확인', font=('돋움', 13), command=com_isbn)
            self.overlap_bt.grid(row=r, column=5)
            self.check_overlap = Label(self.Base_Top, text='중복확인을 위한 레이블입니다.', fg='blue', font=('돋움', 13), bg='white')
            self.check_overlap.grid(row=r+1, column=2, sticky=W, columnspan=2)
        return entry

    #입력칸 생성[회원]
    def u_entry_set(self, t, r, re_choice=False, show = None, ol=False, pic = False, form=False):
        #t = 칸 제목, show = 데이터 정보
        txt = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)     #sticky : 지정된 칸 크기가 위젯 크기보다 클 경우, 정렬 방식을 지정
        input = StringVar()
        entry = Entry(self.Base_Top, width=55, textvariable=input, font=('돋움', 13), relief='solid', bd=1)
        if re_choice:
            entry.insert(0, show)
        entry.grid(row=r, column=2, padx=5, ipady=3, columnspan=3)

        #입력서식 표시
        if form:
            input_form = Label(self.Base_Top, text='ex) 0000-00-00', font=('돋움', 13), bg='white', fg='gray')
            input_form.grid(row=r, column=5)

        if ol==True:
            def check():
                a = ud.user_dataframe()
                a.readcsv()
                phone = entry.get()
                if phone == show:
                    return
                elif phone == '':
                    messagebox.showerror("Err", "\n전화번호가 입력되지 않았습니다.")
                else:
                    a.checkphone(str(phone))
            overlap_bt = Button(self.Base_Top, text='중복확인', font=('돋움', 13), command = check)
            overlap_bt.grid(row=r, column=5)
            check_overlap = Label(self.Base_Top, text='중복확인을 위한 레이블입니다.', fg='blue', font=('돋움', 13), bg='white')
            check_overlap.grid(row=r+1, column=2, sticky=W, columnspan=2)
        if pic:
            def search():
                image = askopenfilename(filetypes=(("GIF 파일", "*.gif"),("모든 파일", "*.*")))
                input.set(image)
            pic_button = Button(self.Base_Top, text='사진찾기', font=('돋움', 13), command = search)
            pic_button.grid(row=r, column=5)
        return entry

    #정보값 출력[도서/회원]
    def info_output(self, t, r, show = None):
        #t = 칸 제목, show = 데이터 정보
        txt = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)
        if show != None:
            info = Label(self.Base_Top, text=show, font=('돋움', 15), bg='white', width=55, anchor=W)
        else:
            info = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white', width=55, anchor=W)      #   <-원본 
        info.grid(row=r, column=2, padx=10, ipady=3, columnspan=3)

    #도서 설명 입력칸[도서]
    def book_ex(self, re_choice=False, op_choice=False):
        info_label = Label(self.Base_Bottom, text='도서 설명', font=('돋움', 15), bg='white')
        info_label.pack(anchor=NW, padx=30, pady=10)
        entry = Entry(self.Base_Bottom, width=100, font=('돋움', 13), relief='solid', bd=1)
        if re_choice:
            entry.insert(0, '기존정보') #차후에 전달받은 데이터를 출력하는 것으로 변경
        if op_choice:
            entry.config(state=DISABLED)
        entry.pack(fill=X, padx=30, ipady=70)
        return entry

    #성별 지정 라디오버튼[회원]
    def user_gender(self, t, r, re_choice=False):
        #추후에 값을 전달하는 함수로 변경
        def test():
            if gender.get():
                self.gender = True
            else:
                self.gender = False
            
                
        txt = Label(self.Base_Top, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)
        gender = BooleanVar()
        male = Radiobutton(self.Base_Top, text="남", font=('돋움', 15), bg='white', variable=gender, value=True, command=test)
        female = Radiobutton(self.Base_Top, text="여", font=('돋움', 15), bg='white', variable=gender, value=False, command=test)

        #수정 화면일 때, 회원의 기존 성별에 따라 체크상태를 지정
        if re_choice:
            male.select()
            self.gender = True
        else:
            female.select()
            self.gender = False

        male.grid(row=r, column=2, sticky=W)
        female.grid(row=r, column=3, sticky=W)
        
    #회원 대여 도서 목록 출력[회원]
    def user_rent(self, booklist):
        rentlist = Label(self.Base, text="  \t대여 도서\t\t\t\t대여일\t반납예정일", font=('돋움', 15), anchor=NW)
        rentlist.pack(fill=X)
        listframe = Frame(self.Base, bg="white")
        listframe.pack(fill=BOTH, expand=True)
        listframe.propagate(0)      #프레임 크기 고정
        self.text_set(listframe)
        self.Book_info_list(booklist, '연장', choice=False)
          
#메시지창 띄우는 이벤트
def msg(showText, win=0):
        ask = messagebox.askquestion(showText, showText+" 하시겠습니까?")
        if ask == 'yes':
            if win != 0:        #win의 인자를 전달받았을 경우(win이 0이 아닐 경우)
                win.withdraw()  #withdraw():Toplevel의 메소드. Toplevel()로 생성한 외부창을 화면에서 제거해준다.
        else:
            return
