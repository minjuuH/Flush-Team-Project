from tkinter import *
from tkinter import messagebox
import menubar as mb

class createWindow:
    def __init__(self, window, title):
        self.newWindow = Toplevel(window)
        self.newWindow.title(title)
        self.newWindow.geometry("960x720")
        self.newWindow.resizable(width=False, height=False)

    def reSelf(self):
        return self.newWindow

    def baseLabel(self, h, w):
        label = Label(self.newWindow, width=w, height=h)
        return label

    def createLabel(self, h, t=' '):
        label = Label(self.newWindow, relief="ridge", height=h, bg='white', text=t, font=('돋움', 15), anchor=E)
        label.pack(fill=X)

    def createEntry(self, window):
        input_text = Entry(window, width=40, font=('돋움', 20))
        input_text.pack(side=RIGHT, padx=5, pady=10, ipadx=5, ipady=5)

    def createButton(self, window, showText):
        def msg():
            messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
        button = Button(window, text=showText, font=('돋움', 20), bg='gray', fg='white', command=msg)
        button.pack(side=RIGHT, padx=2, pady=10)

def BookSearch(window):
    new_win = createWindow(window, "도서 조회")
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label = new_win.baseLabel(80, 20)
    label.pack()
    new_win.createButton(label, "도서 등록")
    new_win.createButton(label, "대출")
    new_win.createEntry(label)
    new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t대출여부 ")
    new_win.createLabel(27)
    #label = Label(WD, relief="ridge", height=h, bg='white', text=t, font=('돋움', 15), anchor=E)
    #label.pack(fill=X)

def UserSearch(window):
    new_win = createWindow(window, "회원 조회")
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label = new_win.baseLabel(80, 20)
    label.pack()
    new_win.createButton(label, "회원 등록")
    new_win.createEntry(label)
    choiceBar = Label(WD, relief="ridge", bg='white')
    choiceBar.pack(fill=X)
    #new_win.createLabel(2)
    chk1=IntVar()
    chk2=IntVar()
    Check = Checkbutton(choiceBar, text="일반회원", variable=chk1, bg="white")
    QuitCheck = Checkbutton(choiceBar, text="탈퇴회원", variable=chk2, bg="white")
    Check.pack(side=RIGHT, pady=10)
    QuitCheck.pack(side=RIGHT)
    new_win.createLabel(27)

def BookSearch_revise(window):
    new_win = createWindow(window, "도서 조회(수정)")
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label = new_win.baseLabel(80, 20)
    label.pack()
    new_win.createButton(label, "검색")
    new_win.createEntry(label)
    new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t\t")
    new_win.createLabel(27)

def BookSearch_del(window):
    new_win = createWindow(window, "도서 조회(삭제)")
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label = new_win.baseLabel(80, 20)
    label.pack()
    new_win.createButton(label, "삭제")
    new_win.createButton(label, "검색")
    new_win.createEntry(label)
    new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t대출여부 ")
    new_win.createLabel(27)