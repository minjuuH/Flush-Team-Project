from tkinter import *
import Rent_View as rv

def MenuBar(window):
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
    rentmenu.add_command(label="도서대출", command=lambda:rv.Rent_Screen(window))
    rentmenu.add_command(label="도서반납", command=lambda:rv.Return_Screen(window))