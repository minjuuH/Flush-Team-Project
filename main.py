from tkinter import *
import menubar as mb
import Rent_View as rv
import Book_def as Bd
import User_View as uv

#메인메뉴 창 생성
window = Tk()
window.title("도서관리시스템")              #윈도창 제목 지정
window.geometry("960x720")                  #화면 사이즈 지정
window.resizable(width=False, height=False) #가로세로 크기 변경 불가

#command로 전달하는 명령 함수에 인자 전달 받는 법 -> lambda: 사용
Book = Button(window, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:Bd.createNewWindow_book_s("도서 조회", window))
User = Button(window, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:uv.userwindow(window))
Rent = Button(window, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window))

Book.place(x=110, y=265)
User.place(x=360, y=265)
Rent.place(x=610, y=265)

#메뉴바 설정
mb.MenuBar(window)

window.mainloop()