from tkinter import *
from tkinter import messagebox
import menubar as mb
import test_class as tc
import Rent_View as rv

#팝업창에 메뉴바 띄울지 결정 -> 띄운다면 팝업창에서 메뉴바 이용할 때는 해당 창을 끄고 새로운 창을 여는 방식..?
#팝업창 객체가 생성되는 클래스
# class createWindow:
#     def __init__(self, window, title):
#         self.newWindow = Toplevel(window)
#         self.newWindow.title(title)
#         self.newWindow.geometry("960x720")
#         self.newWindow.resizable(width=False, height=False)

#     def reSelf(self):
#         return self.newWindow

#     def baseLabel(self, h, w):
#         label = Label(self.newWindow, width=w, height=h)
#         return label

#     def createLabel(self, h, t=' '):
#         label = Label(self.newWindow, relief="ridge", height=h, bg='white', text=t, font=('돋움', 15), anchor=E)
#         label.pack(fill=X)

#     def createEntry(self, window):
#         input_text = Entry(window, width=40, font=('돋움', 20))
#         input_text.pack(side=RIGHT, padx=5, pady=10, ipadx=5, ipady=5)

#     def createButton(self, window, showText):
#         def msg():
#             messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
#         button = Button(window, text=showText, font=('돋움', 20), bg='gray', fg='white', command=msg)
#         button.pack(side=RIGHT, padx=2, pady=10)

# def MenuBar(window):
#     menubar = Menu(window)
#     window.config(menu=menubar)

#     bookmenu=Menu(menubar, tearoff=0)       #tearoff=0 -> 하위메뉴미리보기?를 없애준다
#     menubar.add_cascade(label="도서관리", menu=bookmenu)
#     bookmenu.add_command(label="도서등록")
#     bookmenu.add_command(label="도서조회", command=lambda:BookSearch(window))
#     bookmenu.add_command(label="도서수정", command=lambda:BookSearch_revise(window))
#     bookmenu.add_command(label="도서삭제", command=lambda:BookSearch_del(window))

#     usermenu=Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="회원관리", menu=usermenu)
#     usermenu.add_command(label="회원등록")
#     usermenu.add_command(label="회원조회")
#     usermenu.add_command(label="회원수정")
#     usermenu.add_command(label="회원삭제")

#     rentmenu=Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="대출", menu=rentmenu)
#     rentmenu.add_command(label="도서대출", command=lambda:Rent_Screen(window))
#     rentmenu.add_command(label="도서반납")

# def BookSearch(window):
#     new_win = createWindow(window, "도서 조회")
#     WD = new_win.reSelf()
#     mb.MenuBar(WD)
#     label = new_win.baseLabel(80, 20)
#     label.pack()
#     new_win.createButton(label, "도서 등록")
#     new_win.createButton(label, "대출")
#     new_win.createEntry(label)
#     new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t대출여부 ")
#     new_win.createLabel(27)
#     #label = Label(WD, relief="ridge", height=h, bg='white', text=t, font=('돋움', 15), anchor=E)
#     #label.pack(fill=X)

# def UserSearch(window):
#     new_win = createWindow(window, "회원 조회")
#     WD = new_win.reSelf()
#     mb.MenuBar(WD)
#     label = new_win.baseLabel(80, 20)
#     label.pack()
#     new_win.createButton(label, "회원 등록")
#     new_win.createEntry(label)
#     choiceBar = Label(WD, relief="ridge", bg='white')
#     choiceBar.pack(fill=X)
#     #new_win.createLabel(2)
#     chk1=IntVar()
#     chk2=IntVar()
#     Check = Checkbutton(choiceBar, text="일반회원", variable=chk1, bg="white")
#     QuitCheck = Checkbutton(choiceBar, text="탈퇴회원", variable=chk2, bg="white")
#     Check.pack(side=RIGHT, pady=10)
#     QuitCheck.pack(side=RIGHT)
#     new_win.createLabel(27)

# def BookSearch_revise(window):
#     new_win = createWindow(window, "도서 조회(수정)")
#     WD = new_win.reSelf()
#     mb.MenuBar(WD)
#     label = new_win.baseLabel(80, 20)
#     label.pack()
#     new_win.createButton(label, "검색")
#     new_win.createEntry(label)
#     new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t\t")
#     new_win.createLabel(27)

# def BookSearch_del(window):
#     new_win = createWindow(window, "도서 조회(삭제)")
#     WD = new_win.reSelf()
#     mb.MenuBar(WD)
#     label = new_win.baseLabel(80, 20)
#     label.pack()
#     new_win.createButton(label, "삭제")
#     new_win.createButton(label, "검색")
#     new_win.createEntry(label)
#     new_win.createLabel(2, "제목\t\t저자\t\t출판사\t\tISBN\t대출여부 ")
#     new_win.createLabel(27)

# def create_Window(window, title):
#     newWindow = Toplevel(window)
#     newWindow.title(title)
#     newWindow.geometry("960x720")
#     newWindow.resizable(width=False, height=False)
#     return newWindow

# def Rent_Screen(window):
#     #메시지창 띄우는 이벤트
#     def msg(showText):
#             messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
#             #new_win.quit()
    
#     new_win = create_Window(window, "도서 대출")

#     #메뉴바 설정
#     mb.MenuBar(new_win)

#     Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
#     Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
#     listLabel1 = Label(Baseframe, bg="white", height=50)
#     listLabel1.pack(fill=X)
#     userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('회원 선택'))
#     userChoice.pack(side=LEFT, padx=5, pady=5)
#     userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1)
#     userlist.pack(fill="both", padx=5, pady=5)

#     listLabel2 = Label(Baseframe, bg="white", height=50)
#     listLabel2.pack(fill=X)
#     bookChoice = Button(listLabel2, text="도서 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('도서 선택'))
#     bookChoice.pack(side=LEFT, padx=5, pady=5)
#     booklist = Frame(listLabel2, relief="solid", height=200,bd=1)
#     booklist.pack(fill="both", padx=5, pady=5)

#     rentlabel = Label(Baseframe, text="대출도서:\n대여인:\n대여일:\n반납예정일\n", font=('돋움', 15), height=14)
#     rentlabel.pack(fill=X)

#     buttonBase = Label(Baseframe, height=50)
#     buttonBase.pack()
#     RentButton = Button(buttonBase, text="대출", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('대출'))
#     CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소"))
#     RentButton.pack(side=LEFT, padx=5, pady=5)
#     CancelButton.pack(side=LEFT, padx=5, pady=5)

# def Return_Screen(window):
#     #메시지창 띄우는 이벤트
#     def msg(showText):
#             messagebox.showinfo(showText, showText+"이(가) 클릭되었습니다.")
#             #new_win.quit()
    
#     new_win = create_Window(window, "도서 반납")

#     #메뉴바 설정
#     mb.MenuBar(new_win)

#     Baseframe = Frame(new_win, relief="solid", bd=1)     #bd : 테두리 굵기 설정
#     Baseframe.pack(fill=BOTH, pady=50, expand=True)      #expand=True -> 프레임 안에 위젯이 들어올 경우 프레임 크기가 자동조율되는 것을 방지
    
#     listLabel1 = Label(Baseframe, bg="white", height=50)
#     listLabel1.pack(fill=X)
#     userChoice = Button(listLabel1, text="회원 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('회원 선택'))
#     userChoice.pack(side=LEFT, padx=5, pady=5)
#     userlist = Frame(listLabel1, relief="solid", width=10, height=45, bd=1)
#     userlist.pack(fill="both", padx=5, pady=5)

#     listLabel2 = Label(Baseframe, bg="white", height=50)
#     listLabel2.pack(fill=X)
#     bookChoice = Button(listLabel2, text="도서 선택", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('도서 선택'))
#     bookChoice.pack(side=LEFT, padx=5, pady=5)
#     booklist = Frame(listLabel2, relief="solid", height=200,bd=1)
#     booklist.pack(fill="both", padx=5, pady=5)

#     rentlabel = Label(Baseframe, text="대출도서:\n대여인:\n대여일:\n반납예정일\n", font=('돋움', 15), height=14)
#     rentlabel.pack(fill=X)

#     buttonBase = Label(Baseframe, height=50)
#     buttonBase.pack()
#     RentButton = Button(buttonBase, text="대출", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg('대출'))
#     CancelButton = Button(buttonBase, text="취소", font=('돋움', 20), bg='gray', fg='white', command=lambda:msg("취소"))
#     RentButton.pack(side=LEFT, padx=5, pady=5)
#     CancelButton.pack(side=LEFT, padx=5, pady=5)

#메인메뉴 창 생성
window = Tk()
window.title("도서관리시스템")              #윈도창 제목 지정
window.geometry("960x720")                  #화면 사이즈 지정
window.resizable(width=False, height=False) #가로세로 크기 변경 불가

#command로 전달하는 명령 함수에 인자 전달 받는 법 -> lambda: 사용
Book = Button(window, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: tc.BookSearch(window))
User = Button(window, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: tc.UserSearch(window))
Rent = Button(window, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window))

Book.place(x=110, y=265)
User.place(x=360, y=265)
Rent.place(x=610, y=265)

#메뉴바 설정
mb.MenuBar(window)

window.mainloop()