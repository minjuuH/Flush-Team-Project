from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#창생성 클래스
class windowtool:
    def __init__(self, title): #새창 생성자
        self.window = Toplevel(window)
        self.window.title(title)
        self.window.geometry("960x720")
        self.window.resizable(width = False, height = False)
        
    def labeltool(self, inwindow, intext = None, inimage = None, color = None, x = 0, y = 0): #라벨 생성함수
        label = Label(inwindow, text = intext, image = inimage, bg = color, width = x, height = y)
        return label

    def entrytool(self, inwindow): #검색창 생성함수
        entry = Entry(inwindow, width = 40, font = ('돋움', 20))
        return entry

    def buttontool(self, inwindow, intext = None, x = 0, y = 0, incommand = None): #버튼 생성함수
        button = Button(inwindow, text = intext, width = x, height = y, command = incommand)
        return button

    def ttktool(self, inwindow, columns, x = 170): #표생성 함수 tkinter의 ttk 클래스 요구
        TTK = ttk.Treeview(inwindow, column = columns, displaycolumns = columns) #표 컬럼 설정
        for i in range(5):
            TTK.column(columns[i], width = x, anchor="center") #컬럼 상세 설정
            TTK.heading(columns[i], text = columns[i], anchor = "center") #표 헤더 설정
        TTK["show"] = "headings" #표 헤더만 표시하도록 만듬 
        return TTK

def ch_buttontool(name, varname, nomber, window): #체크버튼 생성함수
    for i in range(nomber):
        globals()['{}{}'.format(varname, i)] = IntVar()
        globals()['{}{}'.format(name, i)] = Checkbutton(window, variable = eval(varname+str(i)))

#상황별 기능을 가장한 메세지창
def buttonevent():
    messagebox.showinfo('실행', "버튼이 실행되었습니다.")
    
#회원 조회창
def userwindow():
    user = windowtool('회원 조회')
    cast = user.labeltool(user.window)
    cast.pack()
    
    Topframe = Frame(cast)
    Topframe.pack(side = TOP, expand=True)
    Bottomframe = Frame(cast)
    Bottomframe.pack(side = BOTTOM, expand=True)
    
    userentry = user.entrytool(Topframe)
    addbutton = user.buttontool(Topframe, "회원 등록", incommand = userwindowadd)
    serchbutton = user.buttontool(Topframe, "회원 선택", incommand = userwindowinfo)
    userttk = user.ttktool(Bottomframe, usercolumn,182)
    for i in range(len(userinfo)):
        userttk.insert('', "end",text = i, values = userinfo[i], iid = i)
        
    userentry.pack(side = LEFT, padx = 5, pady = 10)
    serchbutton.pack(side = LEFT, padx = 5, pady = 10)
    addbutton.pack(side = LEFT, padx = 5, pady = 10)
    userttk.pack(expand = 1, anchor = CENTER)
    
#회원 상세정보창
def userwindowinfo():
    user = windowtool('회원 상세정보')
    cast = user.labeltool(user.window)
    cast.pack()
    
    Topframe = Frame(cast)
    Topframe.pack(side = TOP, expand=True)
    Bottomframe = Frame(cast)
    Bottomframe.pack(side = BOTTOM, expand=True)
    buttonplace = user.labeltool(user.window)
    buttonplace.pack(side = BOTTOM)

    userimage = user.labeltool(Topframe, color = 'white', x = 20, y = 15)
    userinfo = user.labeltool(Topframe, color = 'white', x = 100, y = 15)
    rentinfo = user.labeltool(Bottomframe, color = 'gray', x = 120, y = 20)
    modibutton = user.buttontool(buttonplace, '수정', incommand = userwindowmodi)
    removebutton = user.buttontool(buttonplace, '탈퇴', incommand = userwindowremove)
    exitbutton = user.buttontool(buttonplace, '닫기', incommand = buttonevent)

    userimage.pack(side = LEFT, padx = 5, pady = 10)
    userinfo.pack(side = LEFT, padx = 5, pady = 10)
    rentinfo.pack(side = TOP, anchor = CENTER, expand = 1)
    modibutton.pack(side = LEFT,  padx = 5, pady = 10)
    removebutton.pack(side = LEFT, padx = 5, pady = 10)
    exitbutton.pack(side = LEFT, padx = 5, pady = 10)
    
    
#회원 수정
def userwindowmodi():
    user = windowtool('회원 수정')
    cast = user.labeltool(user.window)
    cast.pack()
    
    Topframe = Frame(cast)
    Topframe.pack(side = TOP, expand=True)
    Bottomframe = Frame(cast)
    Bottomframe.pack(side = BOTTOM, expand=True)

    userimage = user.labeltool(Topframe, color = 'white', x = 20, y = 15)
    userinfo = user.labeltool(Topframe, color = 'white', x = 80, y = 15)
    chooseimage = user.buttontool(Topframe, '사진 선택', incommand = buttonevent)
    checksame = user.buttontool(Topframe, '중복확인', incommand = buttonevent)
    Okbutton = user.buttontool(Bottomframe, '완료', incommand = buttonevent)
    Nobutton = user.buttontool(Bottomframe, '취소', incommand = buttonevent)

    userimage.pack(side = LEFT, padx = 5, pady = 10)
    chooseimage.pack(side = LEFT, padx = 5, pady = 10)
    userinfo.pack(side = LEFT, padx = 5, pady = 10)
    checksame.pack(side = LEFT, padx = 5, pady = 10)
    Okbutton.pack(side = LEFT, padx = 5, pady = 10)
    Nobutton.pack(side = LEFT, padx = 5, pady = 10)

#회원 등록
def userwindowadd():
    user = windowtool('회원 등록')
    cast = user.labeltool(user.window)
    cast.pack()
    
    Topframe = Frame(cast)
    Topframe.pack(side = TOP, expand=True)
    Bottomframe = Frame(cast)
    Bottomframe.pack(side = BOTTOM, expand=True)

    userimage = user.labeltool(Topframe, color = 'white', x = 20, y = 15)
    userinfo = user.labeltool(Topframe, color = 'white', x = 80, y = 15)
    chooseimage = user.buttontool(Topframe, '사진 선택', incommand = buttonevent)
    checksame = user.buttontool(Topframe, '중복확인', incommand = buttonevent)
    addbutton = user.buttontool(Bottomframe, '등록', incommand = buttonevent)
    Nobutton = user.buttontool(Bottomframe, '취소', incommand = buttonevent)

    userimage.pack(side = LEFT, padx = 5, pady = 10)
    chooseimage.pack(side = LEFT, padx = 5, pady = 10)
    userinfo.pack(side = LEFT, padx = 5, pady = 10)
    checksame.pack(side = LEFT, padx = 5, pady = 10)
    addbutton.pack(side = LEFT, padx = 5, pady = 10)
    Nobutton.pack(side = LEFT, padx = 5, pady = 10)
    
#회원 삭제 
def userwindowremove():
    user = windowtool('탈퇴 회원')
    cast = user.labeltool(user.window)
    cast.pack()
    
    Topframe = Frame(cast)
    Topframe.pack(side = TOP, expand=True)
    Bottomframe = Frame(cast)
    Bottomframe.pack(side = BOTTOM, expand=True)

    userimage = user.labeltool(Topframe, color = 'white', x = 20, y = 15)
    userinfo = user.labeltool(Topframe, color = 'white', x = 100, y = 15)
    backbutton = user.buttontool(Bottomframe, '복구', incommand = buttonevent)
    Nobutton = user.buttontool(Bottomframe, '취소', incommand = buttonevent)

    userimage.pack(side = LEFT, padx = 5, pady = 10)
    userinfo.pack(side = LEFT, padx = 5, pady = 10)
    backbutton.pack(side = LEFT,  padx = 5, pady = 10)
    Nobutton.pack(side = LEFT, padx = 5, pady = 10)

#회원 정보
usercolumn = ['이름', '생년월일', '성별', '전화번호', '이메일주소']
userinfo = [("ㅇㅇㅇ", "19xx-xx-xx", False, "010xxxxoooo", "xxx@xxx.xxx"),
            ("ㅁㅁㅁ", "20xx-xx-xx", True, "010xxxxoooo", "xxx@xxx.xxx"),
            ("ㅎㅎㅎ", "19xx-xx-xx", False, "010xxxxoooo", "xxx@xxx.xxx")]

window = Tk()
window.title("도서관리시스템")
window.geometry("960x770")
window.resizable(width = False, height = False)


BOOK = Button(window, text="도서", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command = lambda: bookwindow('도서 조회'))
USER = Button(window, text="회원", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command = userwindow)
RENT = Button(window, text="대출", font=("돋움", 50), fg='white', background="gray", height=2, width=6, command = lambda: rentwindow('도서 대출'))


BOOK.place(x=110, y=265)
USER.place(x=360, y=265)
RENT.place(x=610, y=265)

#메뉴
menubar = Menu(window)
window.config(menu=menubar)

bookmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="도서관리", menu=bookmenu)
bookmenu.add_command(label="도서등록")
bookmenu.add_command(label="도서조회")
bookmenu.add_command(label="도서수정")
bookmenu.add_command(label="도서삭제")

usermenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="회원관리", menu=usermenu)
usermenu.add_command(label="회원등록", command = userwindowadd)
usermenu.add_command(label="회원조회", command = userwindow)
usermenu.add_command(label="회원수정", command = userwindowmodi)
usermenu.add_command(label="회원삭제", command = userwindowremove)

rentmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="대출", menu=rentmenu)
rentmenu.add_command(label="도서대출")
rentmenu.add_command(label="도서반납")

window.mainloop()
