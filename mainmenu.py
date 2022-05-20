from tkinter import *
from tkinter import messagebox
#from functools import partial

#팝업창 객체가 생성되는 클래스
class creatWindow:
    def __init__(self, title):
        self.newWindow = Toplevel(window)
        self.newWindow.title(title)
        self.newWindow.geometry("960x720")
        self.newWindow.resizable(width=False, height=False)

    def createLabel(self, w, h):
        label = Label(self.newWindow, width=w, height=h)
        return label

    def createEntry(self, window):
        input_text = Entry(window, width=40, font=('돋움', 20))
        input_text.pack(side=RIGHT, padx=5, pady=10)

    def createButton(self, window, showText):
        button = Button(window, text=showText)
        button.pack(side=RIGHT, padx=5, pady=10)

def createNewWindow(title):
    new_win = creatWindow(title)
    label = new_win.createLabel(80, 20)
    label.pack()
    new_win.createButton(label, "도서 등록")
    new_win.createButton(label, "대출")
    new_win.createEntry(label)

window = Tk()
window.title("도서관리시스템")              #윈도창 제목 지정
window.geometry("960x720")                  #화면 사이즈 지정
window.resizable(width=False, height=False) #가로세로 크기 변경 불가

#insert 메소드를 사용하여 Entry의 기본 텍스트 설정 가능
#bind 메소드로 입력키에 따른 이벤트 지정 가능
input_text = Entry(window, width=50, font=('돋움', 20))
#input_text.insert(0, "기본 텍스트")
input_text.pack()

#command로 전달하는 명령 함수에 인자 전달 받는 법 -> lamda: 사용
Book = Button(window, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: createNewWindow("도서 조회"))
User = Button(window, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: createNewWindow("회원 조회"))
Rent = Button(window, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: createNewWindow("도서 대출"))

Book.place(x=110, y=265)
User.place(x=360, y=265)
Rent.place(x=610, y=265)

#메뉴바 설정
menubar = Menu(window)
window.config(menu=menubar)

bookmenu=Menu(menubar, tearoff=0)       #tearoff=0 -> 하위메뉴미리보기?를 없애준다
menubar.add_cascade(label="도서관리", menu=bookmenu)
bookmenu.add_command(label="도서등록")
bookmenu.add_command(label="도서조회")
bookmenu.add_command(label="도서수정")
bookmenu.add_command(label="도서삭제")

usermenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="회원관리", menu=usermenu)
usermenu.add_command(label="회원등록")
usermenu.add_command(label="회원조회")
usermenu.add_command(label="회원수정")
usermenu.add_command(label="회원삭제")

rentmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="대출", menu=rentmenu)
rentmenu.add_command(label="도서대출")
rentmenu.add_command(label="도서반납")

window.mainloop()