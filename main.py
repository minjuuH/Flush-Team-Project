from tkinter import *
import Rent_View as rv
import Book_def as Bd
import User_View as uv
import UI_Class as UC

#메인메뉴 창 생성
window = Tk()
window.title("도서관리시스템")              #윈도창 제목 지정
window.geometry("960x720")                  #화면 사이즈 지정
window.resizable(width=False, height=False) #가로세로 크기 변경 불가

#창전환을 위한 프레임 생성
Base = UC.new_window()
Base.make_Frame(window)

#command로 전달하는 명령 함수에 인자 전달 받는 법 -> lambda: 사용
Book = Button(Base.base_frame, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:Bd.createNewWindow_book_s(window, uc=Base))
User = Button(Base.base_frame, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda:uv.userwindow(window, uc=Base))
Rent = Button(Base.base_frame, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command=lambda: rv.Rent_Screen(window, uc=Base))

Book.place(x=110, y=265)
User.place(x=360, y=265)
Rent.place(x=610, y=265)

#메뉴바 설정
menubar = Menu(window)
window.config(menu=menubar)

bookmenu=Menu(menubar, tearoff=0)       #tearoff=0 -> 하위메뉴미리보기?를 없애준다
menubar.add_cascade(label="도서관리", menu=bookmenu)
bookmenu.add_command(label="도서등록", command=lambda: Bd.createNewWindow_book_r(window, uc=Base))
bookmenu.add_command(label="도서조회", command=lambda: Bd.createNewWindow_book_s(window, uc=Base))
bookmenu.add_command(label="도서수정", command=lambda: Bd.createNewWindow_book_m(window, uc=Base))
bookmenu.add_command(label="도서삭제", command=lambda: Bd.createNewWindow_book_del(window, uc=Base))

usermenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="회원관리", menu=usermenu)
usermenu.add_command(label="회원등록", command =lambda: uv.userwindowadd(window, uc=Base))
usermenu.add_command(label="회원조회", command =lambda: uv.userwindow(window, uc=Base))
usermenu.add_command(label="회원수정", command =lambda: uv.re_userwindow(window, uc=Base))
usermenu.add_command(label="회원탈퇴", command =lambda: uv.del_userwindow(window, uc=Base))

rentmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="대출", menu=rentmenu)
rentmenu.add_command(label="도서대출", command=lambda:rv.Rent_Screen(window, uc=Base))
rentmenu.add_command(label="도서반납", command=lambda:rv.Return_Screen(window, uc=Base))

window.mainloop()