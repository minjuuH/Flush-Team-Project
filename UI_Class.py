from tkinter import *
from tkinter import messagebox
import menubar as mb

class new_window:
    #생성자
    def __init__(self):
        self.newWindow = None       #이후에 Toplavel 객체를 저장할 변수 지정
        self.base_frame = None      #이후에 화면의 베이스가 되는 프레임 객체를 저장할 변수 지정

    #외부창 생성(외부창이 아닐 경우에 사용)
    def make_window(self, base_win, title, geo="960x720"):
        self.newWindow = Toplevel(base_win)
        self.newWindow.title(title)
        self.newWindow.geometry(geo)
        self.newWindow.resizable(width=False, height=False)
        if geo=="960x720":
            mb.MenuBar(self.newWindow, self)
        self.make_Frame()

    #창 화면의 베이스가 되는 프레임 객체 생성
    def make_Frame(self):
        self.base_frame = Frame(self.newWindow)
        self.base_frame.pack(fill=BOTH, expand=True)

    #창의 프레임 전환을 위한 함수(외부창일 경우에 사용)
    def Change_Frame(self, title):
        if self.base_frame != None:
            self.base_frame.destroy()
            self.make_Frame()
            self.newWindow.title(title)

    #검색바 설정
    def Search_bar(self, font_size=20):
        self.baseLabel = Label(self.base_frame)
        self.baseLabel.pack()
        input_text = Entry(self.baseLabel, width=40, font=('돋움', font_size+2))
        input_text.pack(side=LEFT, padx=5, pady=5)
        S_button = Button(self.baseLabel, text="검색", font=('돋움', font_size), bg='gray', fg='white', command=lambda:msg('검색'))
        S_button.pack(side=LEFT, padx=5, pady=5)

    #화면 구성을 위한 베이스 프레임[대출]
    def Choice_base(self):
        self.Base = Frame(self.base_frame, relief="solid", bd=1)     #bd : 테두리 굵기 설정
        self.Base.pack(fill=BOTH, pady=50, expand=True)

    #회원/도서 선택창[대출]
    def Choice(self, button_text, h, CM):
        listLabel = Label(self.Base, bg="white", height=50)
        listLabel.pack(fill=X, expand=True)
        userChoice = Button(listLabel, text=button_text, font=('돋움', 20), bg='gray', fg='white', command=lambda:CM(self.newWindow))
        userChoice.pack(side=LEFT, padx=5, pady=5)
        userlist = Frame(listLabel, relief="solid", height=h, bd=1) #회원 정보를 출력할 자리 frame으로 지정
        userlist.pack(fill=X, padx=5, pady=5)

    #대출 정보 출력[대출]
    def rent_info(self):
        rentlabel = Label(self.Base, text="대출도서:\n대여인:\n대여일:\n반납예정일\n", font=('돋움', 15), height=14)
        rentlabel.pack(fill=X)

    #최종 버튼(가운데 정렬)
    def under_button(self, menu_text, base):
        buttonBase = Label(base, height=50)
        buttonBase.pack(side=BOTTOM)
        RentButton = Button(buttonBase, text=menu_text, font=('돋움', 20), bg='gray', fg='white', command=lambda:msg(menu_text))
        CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소", self.newWindow))
        RentButton.pack(side=LEFT, padx=5, pady=5)
        CancelButton.pack(side=LEFT, padx=5, pady=5)

    #최종 버튼(오른쪽 정렬)[대출-회원/도서 선택]
    def under_button_R(self):
        buttonBase = Label(self.base_frame, height=20)
        buttonBase.pack(side=BOTTOM, fill=X)
        CancelButton = Button(buttonBase, text="취소", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg("취소", self.newWindow))
        CancelButton.pack(side=RIGHT, padx=5, pady=5)
        RentButton = Button(buttonBase, text="확인", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg('확인', self.newWindow))
        RentButton.pack(side=RIGHT, padx=5, pady=5)

    #선택한 회원의 대출 목록을 출력시켜주는 함수[대출]
    def rent_list(self):
        rentlist = Label(self.Base, bg="white", text="  대여 목록", font=('돋움', 15), anchor=NW)
        rentlist.pack(fill=X)
        listLabel2 = Label(self.Base, bg="white")
        listLabel2.pack(fill=BOTH, expand=True)
        booklist = Frame(listLabel2, relief="solid", height=450, bd=1)          #대여 목록을 출력할 자리 frame으로 지정
        booklist.pack(fill=BOTH, padx=5, pady=5)

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

    #체크박스 없는 리스트
    def Nocheck_list(self, frame, command_def, font_size=13):
        sb = Scrollbar(frame)
        text = Text(frame, width=40, height=20, yscrollcommand=sb.set, font=('돋움', font_size), spacing1=3, spacing2=3, spacing3=3)    #spacing1~3:줄 사이 간격 지정
        sb.config(command=text.yview)
        sb.pack(side=RIGHT, fill=Y)
        text.pack(side=TOP, fill=BOTH, expand=True)

        # if len(list)==0:  #출력할 데이터가 존재하지 않을 경우
        #     text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        #     lb = Label(text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
        #     text.window_create("end", window=lb)
        # else:             #출력할 데이터가 존재할 경우
        for i in range(30):
            text.insert('end', '도서 정보')   
            bt = Button(text, text="수정", font=('돋움', font_size-3), command=command_def)
            text.window_create('end', window=bt)
            text.insert('end', '\n')
        # text.insert('end', '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        # lb = Label(text, text='등록된 정보가 없습니다.', font=('돋움', font_size), bg='white', anchor=CENTER, width=90)
        # text.window_create("end", window=lb)
        text.configure(state=DISABLED)  #텍스트를 수정하지 못하게 상태 변경
    #추가해야하는 기능 : 검색했을 때 출력된 텍스트 목록 비우고 검색된 정보만 출력하도록 설정/출력할 정보를 인자로 받아야함

    #회원, 도서 목록 리스트 출력
    def list_print(self, bar_text, list):   #list:출력할 정보 리스트
        listFrame = Frame(self.base_frame, relief="solid", height=50, bd=1, bg="white")
        listFrame.pack(fill=BOTH, expand=True)

        labelBar = Label(listFrame, bg="white", relief='ridge', text=bar_text, font=('돋움', 13), anchor=W)
        labelBar.pack(fill=BOTH)

        self.check_list(listFrame)

    #버튼 생성[도서,회원]
    def createButton(self, showText, window):   #window=self.baseLabel
        def msg():
            messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
        button = Button(window, text=showText, font=('돋움', 20), bg='gray', fg='white', command=msg)
        button.pack(side=LEFT, padx=2, pady=10)

    #도서 목록 출력[도서]
    def Book_list(self, bar_text, command_def=None, choice=True):
        label_bar = Label(self.base_frame, relief="ridge", height=2, bg='white', text=bar_text, font=('돋움', 15), anchor=E)
        label_bar.pack(fill=X)
        label = Label(self.base_frame, relief="ridge", height=37, bg='white')
        label.pack(fill=BOTH, expand=True)
        if choice==True:
            self.check_list(label, 15)
        else:
            self.Nocheck_list(label, command_def, 15)

    #등록 화면 설정[도서/회원]
    def input_set(self, t):
        txt = Label(self.base_frame, text=t, font=('돋움', 20, 'bold'))
        txt.pack(anchor=NW, padx=10, pady=5)
        self.Base = Frame(self.base_frame, relief='solid', bg='white', bd=2)
        self.Base.pack(fill=BOTH, pady=10, expand=True)
        pic_base = Label(self.Base, bg='white')
        #pic_base.pack(anchor=NW, side=LEFT)
        pic_base.grid(row=0, column=0, rowspan=20)
        pic_frame = Frame(pic_base, width=180, height=220, relief='solid', bd=1)
        pic_frame.pack(anchor=NW, padx=30, pady=30, expand=True, side=TOP)
        pic_frame.propagate(0)  #frame 크기를 고정시켜 줌
        pic_bt = Button(pic_base, text='사진 선택', font=('돋움', 13))
        pic_bt.pack(fill=X, padx=30)
        pic = Label(pic_frame, text='사진 등록', font=('돋움', 15))
        pic.pack(pady=90)

        #빈레이블로 사용하지 않을 부분 채워주기
        x_label = Label(self.Base, height=1, bg='white')
        x_label.grid(row=0, column=1)

    #입력칸 생성[도서/회원]
    def entry_set(self, t, r, ol=False):
        txt = Label(self.Base, text=t, font=('돋움', 15), bg='white')
        txt.grid(row=r, column=1, sticky=W)     #sticky : 지정된 칸 크기가 위젯 크기보다 클 경우, 정렬 방식을 지정
        entry = Entry(self.Base, width=55, font=('돋움', 13), relief='solid', bd=1)
        entry.grid(row=r, column=2, padx=5, ipady=3)
        if ol==True:
            overlap_bt = Button(self.Base, text='중복확인', font=('돋움', 13))
            overlap_bt.grid(row=r, column=3)
            check_overlap = Label(self.Base, text='중복확인을 위한 레이블입니다.', fg='blue', font=('돋움', 13), bg='white')
            check_overlap.grid(row=r+1, column=2, sticky=W)

    #도서 설명 입력칸[도서]
    def book_ex(self):
        info_label = Label(self.Base, text='도서 설명', font=('돋움', 15), bg='white')
        info_label.grid(row=20, column=0, sticky=W, padx=30, pady=20)
        entry = Entry(self.Base, width=100, font=('돋움', 13), relief='solid', bd=1)
        entry.grid(row=21, column=0, columnspan=4, sticky=W, padx=30, ipady=60)


#메시지창 띄우는 이벤트
def msg(showText, win=0):
        messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
        if win != 0:        #win의 인자를 전달받았을 경우(win이 0이 아닐 경우)
            win.withdraw()  #withdraw():Toplevel의 메소드. Toplevel()로 생성한 외부창을 화면에서 제거해준다.