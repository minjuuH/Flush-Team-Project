from tkinter import *
from tkinter import messagebox
import menubar as mb

#외부창을 생성하고 반환해주는 함수
def create_Window(window, title, geo="960x720"):
    newWindow = Toplevel(window)
    newWindow.title(title)
    newWindow.geometry(geo)
    newWindow.resizable(width=False, height=False)
    return newWindow

#메시지창 띄우는 이벤트
def msg(showText, win=0):
        messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
        if win != 0:        #win의 인자를 전달받았을 경우(win이 0이 아닐 경우)
            win.withdraw()  #withdraw():Toplevel의 메소드. Toplevel()로 생성한 외부창을 화면에서 제거해준다.

#도서 대출 화면
def Rent_Screen(window):
    new_win = create_Window(window, "도서 대출")

    #메뉴바 설정
    mb.MenuBar(new_win)

    Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
    Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
    #회원 선택 버튼/선택한 회원 정보 출력
    listLabel1 = Label(Baseframe, bg="white", height=50)
    listLabel1.pack(fill=X)
    userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:User_Choice(new_win))
    userChoice.pack(side=LEFT, padx=5, pady=5)
    userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1) #회원 정보를 출력할 자리 frame으로 지정
    userlist.pack(fill="both", padx=5, pady=5)

    #도서 선택 버튼/선택한 도서 정보 출력
    listLabel2 = Label(Baseframe, bg="white", height=50)
    listLabel2.pack(fill=X)
    bookChoice = Button(listLabel2, text="도서 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:Book_Choice(new_win))
    bookChoice.pack(side=LEFT, padx=5, pady=5)
    booklist = Frame(listLabel2, relief="solid", height=200, bd=1)          #도서 정보를 출력할 자리 frame으로 지정
    booklist.pack(fill="both", padx=5, pady=5)

    #대출 정보 출력
    rentlabel = Label(Baseframe, text="대출도서:\n대여인:\n대여일:\n반납예정일\n", font=('돋움', 15), height=14)
    rentlabel.pack(fill=X)

    #대출/취소 버튼
    buttonBase = Label(Baseframe, height=50)
    buttonBase.pack()
    RentButton = Button(buttonBase, text="대출", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('대출'))
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    RentButton.pack(side=LEFT, padx=5, pady=5)
    CancelButton.pack(side=LEFT, padx=5, pady=5)

#도서 반납 화면
def Return_Screen(window):
    new_win = create_Window(window, "도서 반납")

    #메뉴바 설정
    mb.MenuBar(new_win)

    Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
    Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
    #회원 선택 버튼/선택한 회원 정보 출력
    listLabel1 = Label(Baseframe, bg="white", height=50)
    listLabel1.pack(fill=X)
    userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:User_Choice(new_win))
    userChoice.pack(side=LEFT, padx=5, pady=5)
    userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1) #회원 정보를 출력할 자리 frame으로 지정
    userlist.pack(fill="both", padx=5, pady=5)

    #반납/취소 버튼
    buttonBase = Label(Baseframe, height=50)
    buttonBase.pack(side=BOTTOM)
    RentButton = Button(buttonBase, text="반납", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('반납'))
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    RentButton.pack(side=LEFT, padx=5, pady=5)
    CancelButton.pack(side=LEFT, padx=5, pady=5)

    #대여 목록 출력
    rentlist = Label(Baseframe, bg="white", text="  대여 목록", font=('돋움', 15), anchor=NW)
    rentlist.pack(fill=X)
    listLabel2 = Label(Baseframe, bg="white")
    listLabel2.pack(fill=BOTH, expand=True)
    booklist = Frame(listLabel2, relief="solid", height=450, bd=1)          #대여 목록을 출력할 자리 frame으로 지정
    booklist.pack(fill=BOTH, padx=5, pady=5)

#회원 선택창
def User_Choice(window):
    new_win = create_Window(window, "회원 선택", "800x600")
    #검색창 설정
    baseLabel = Label(new_win)
    baseLabel.pack()
    S_button = Button(baseLabel, text="검색", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg('검색'))
    S_button.pack(side=RIGHT, padx=5, pady=5)
    input_text = Entry(baseLabel, width=40, font=('돋움', 15))
    input_text.pack(side=RIGHT, padx=5, pady=5)

    #확인/취소 버튼
    buttonBase = Label(new_win, height=20)
    buttonBase.pack(side=BOTTOM, fill=X)
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    CancelButton.pack(side=RIGHT, padx=5, pady=5)
    RentButton = Button(buttonBase, text="확인", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg('확인', new_win))
    RentButton.pack(side=RIGHT, padx=5, pady=5)

    #회원 목록이 출력될 프레임
    listFrame = Frame(new_win, relief="solid", height=50, bd=1, bg="white")
    listFrame.pack(fill=BOTH, expand=True)

    labelBar = Label(listFrame, bg="white", relief='ridge', text="\t이름\t생년월일\t전화번호", font=('돋움', 13), anchor=W)
    labelBar.pack(fill=BOTH)

#도서 선택창
def Book_Choice(window):
    new_win = create_Window(window, "도서 선택", "800x600")
    #검색창 설정
    baseLabel = Label(new_win)
    baseLabel.pack()
    S_button = Button(baseLabel, text="검색", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg('검색'))
    S_button.pack(side=RIGHT, padx=5, pady=5)
    input_text = Entry(baseLabel, width=40, font=('돋움', 15))
    input_text.pack(side=RIGHT, padx=5, pady=5)

    #확인/취소 버튼
    buttonBase = Label(new_win, height=20)
    buttonBase.pack(side=BOTTOM, fill=X)
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    CancelButton.pack(side=RIGHT, padx=5, pady=5)
    RentButton = Button(buttonBase, text="확인", font=('돋움', 13), bg='gray', fg='white', command=lambda:msg('확인', new_win))
    RentButton.pack(side=RIGHT, padx=5, pady=5)

    #회원 목록이 출력될 프레임
    listFrame = Frame(new_win, relief="solid", height=50, bd=1, bg="white")
    listFrame.pack(fill=BOTH, expand=True)

    labelBar = Label(listFrame, bg="white", relief='ridge', text="제목\t저자\t출판사\tISBN\t대출여부", font=('돋움', 13), anchor=E)
    labelBar.pack(fill=BOTH)

    # #체크박스 18개가 화면에 출력되는 최대 개수
    # for i in range(18):
    #     check = Checkbutton(listFrame, bg='white', relief='ridge', text="제목\t저자\t출판사\tISBN\t대출여부", font=('돋움', 13), anchor=W)
    #     check.pack(anchor=NW, fill=X)