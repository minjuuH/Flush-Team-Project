from tkinter import *
import Rent_View as rv
import Book_def as Bd
import User_View as uv
from UI_Class import *

def MenuBar(window, base_win=None):
    menubar = Menu(window)
    window.config(menu=menubar)

    bookmenu=Menu(menubar, tearoff=0)       #tearoff=0 -> 하위메뉴미리보기?를 없애준다
    menubar.add_cascade(label="도서관리", menu=bookmenu)
    bookmenu.add_command(label="도서등록", command=lambda: Bd.createNewWindow_book_r(base_win, 1))
    bookmenu.add_command(label="도서조회", command=lambda: Bd.createNewWindow_book_s(base_win, 1))
    bookmenu.add_command(label="도서수정", command=lambda: Bd.createNewWindow_book_m(base_win, 1))
    bookmenu.add_command(label="도서삭제", command=lambda: Bd.createNewWindow_book_del(base_win, 1))

    usermenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="회원관리", menu=usermenu)
    usermenu.add_command(label="회원등록", command =lambda: uv.userwindowadd(window))
    usermenu.add_command(label="회원조회", command =lambda: uv.userwindow(window))
    usermenu.add_command(label="회원수정", command =lambda: uv.re_userwindow(window))
    usermenu.add_command(label="회원삭제", command =lambda: uv.del_userwindow(window))

    rentmenu=Menu(menubar, tearoff=0)
    menubar.add_cascade(label="대출", menu=rentmenu)
    rentmenu.add_command(label="도서대출", command=lambda:rv.Rent_Screen(base_win, 1))
    rentmenu.add_command(label="도서반납", command=lambda:rv.Return_Screen(base_win, 1))