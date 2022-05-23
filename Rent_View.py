from tkinter import *
from tkinter import messagebox
import menubar as mb

def create_Window(window, title):
    newWindow = Toplevel(window)
    newWindow.title(title)
    newWindow.geometry("960x720")
    newWindow.resizable(width=False, height=False)
    return newWindow

#메시지창 띄우는 이벤트
def msg(showText, win=0):
        messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
        if win != 0:
            win.withdraw()

def Rent_Screen(window):
    new_win = create_Window(window, "도서 대출")

    #메뉴바 설정
    mb.MenuBar(new_win)

    Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
    Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
    listLabel1 = Label(Baseframe, bg="white", height=50)
    listLabel1.pack(fill=X)
    userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('회원 선택'))
    userChoice.pack(side=LEFT, padx=5, pady=5)
    userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1)
    userlist.pack(fill="both", padx=5, pady=5)

    listLabel2 = Label(Baseframe, bg="white", height=50)
    listLabel2.pack(fill=X)
    bookChoice = Button(listLabel2, text="도서 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('도서 선택'))
    bookChoice.pack(side=LEFT, padx=5, pady=5)
    booklist = Frame(listLabel2, relief="solid", height=200,bd=1)
    booklist.pack(fill="both", padx=5, pady=5)

    rentlabel = Label(Baseframe, text="대출도서:\n대여인:\n대여일:\n반납예정일\n", font=('돋움', 15), height=14)
    rentlabel.pack(fill=X)

    buttonBase = Label(Baseframe, height=50)
    buttonBase.pack()
    RentButton = Button(buttonBase, text="대출", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('대출'))
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    RentButton.pack(side=LEFT, padx=5, pady=5)
    CancelButton.pack(side=LEFT, padx=5, pady=5)

def Return_Screen(window):
    #메시지창 띄우는 이벤트
    def msg(showText):
            messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
            #new_win.quit()
    
    new_win = create_Window(window, "도서 반납")

    #메뉴바 설정
    mb.MenuBar(new_win)

    Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
    Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
    listLabel1 = Label(Baseframe, bg="white", height=50)
    listLabel1.pack(fill=X)
    userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('회원 선택'))
    userChoice.pack(side=LEFT, padx=5, pady=5)
    userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1)
    userlist.pack(fill="both", padx=5, pady=5)

    buttonBase = Label(Baseframe, height=50)
    buttonBase.pack(side=BOTTOM)
    RentButton = Button(buttonBase, text="반납", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('반납'))
    CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소", new_win))
    RentButton.pack(side=LEFT, padx=5, pady=5)
    CancelButton.pack(side=LEFT, padx=5, pady=5)

    rentlist = Label(Baseframe, bg="white", text="  대여 목록", font=('돋움', 15), anchor=NW)
    rentlist.pack(fill=X)

    listLabel2 = Label(Baseframe, bg="white")
    listLabel2.pack(fill=BOTH, expand=True)
    booklist = Frame(listLabel2, relief="solid", height=500, bd=1)
    booklist.pack(fill=BOTH, padx=5, pady=5)
