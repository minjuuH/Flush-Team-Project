from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#창 클래스
class windowtool:
    def __init__(self, title): #생성자
        self.window = Toplevel(window)
        self.window.title(title)
        self.window.geometry("960x720")
        self.window.resizable(width = False, height = False)
        
    def labeltool(self, intext = None, inimage = None, x = 0, y = 0): #라벨
        label = Label(self.window, text = intext, image = inimage, width = x, height = y)
        return label

    def entrytool(self): #검색창
        entry = Entry(self.window, width = 40, font = ('돋움', 20))
        return entry

    def buttontool(self, intext, x = 0, y = 0, incommand = None): #버튼
        button = Button(self.window, text = intext, width = x, height = y, command = incommand)
        return button

    def ttktool(self, columns, x = 170): #표 위젯 tkinter의 ttk 클래스 요구
        TTK = ttk.Treeview(self.window, column = columns, displaycolumns = columns) #표 컬럼 설정
        for i in range(5):
            TTK.column(columns[i], width = x, anchor="center") #컬럼 상세 설정
            TTK.heading(columns[i], text = columns[i], anchor = "center") #표 헤더 설정
        TTK["show"] = "headings" #표 헤더만 표시하도록 만듬 
        return TTK

def ch_buttontool(name, varname, nomber, window): #체크버튼
    for i in range(nomber):
        globals()['{}{}'.format(varname, i)] = IntVar()
        globals()['{}{}'.format(name, i)] = Checkbutton(window, variable = eval(varname+str(i)))

#상황별 기능을 가장한 메세지창
def Message_in_book():
    messagebox.showinfo("도서 등록", "도서 등록입니다.")

def Message_rent_book():
    messagebox.showinfo("도서 대출", "도서 대출입니다.")

def Message_in_user():
    messagebox.showinfo("회원 등록", "회원 등록입니다.")

def Message_ch_user():
    messagebox.showinfo("회원 선택", "회원 선택입니다.")

def Message_ch_book():
    messagebox.showinfo("도서 선택", "도서 선택입니다.")

def Message_remove_user():
    messagebox.showinfo("회원 삭제", "회원 삭제입니다.")

def Message_cancel():
    messagebox.showinfo("취소", "취소 선택입니다.")

#도서 조회창
def bookwindow(title):
    book = windowtool(title)
    bookentry = book.entrytool()
    serchbutton = book.buttontool("도서 등록", incommand = Message_in_book)
    rentbutton = book.buttontool("도서 수정", incommand = Message_rent_book)
    bookttk = book.ttktool(bookcolumn)
    bookttk.column("제목", width = 230, anchor="center")
    bookttk.heading("제목", text = "제목", anchor = "center")
    for i in range(len(bookinfo)):
        bookttk.insert('', "end",text = i, values = bookinfo[i], iid = i)
    bookentry.place(x = 20, y = 30)
    serchbutton.place(x = 700, y = 32)
    rentbutton.place(x = 780, y = 32)
    bookttk.place(x = 40, y = 200)

#회원 조회창
def userwindow():
    user = windowtool('회원 조회')
    userentry = user.entrytool()
    addbutton = user.buttontool("회원 등록", incommand = Message_in_user)
    modibutton = user.buttontool("회원 수정", incommand = userwindowmodi)
    removebutton = user.buttontool("회원 삭제", incommand = userwindowremove)
    userttk = user.ttktool(usercolumn, x = 182)
    for i in range(len(userinfo)):
        userttk.insert('', "end",text = i, values = userinfo[i], iid = i)
    userentry.place(x = 20, y = 30)
    addbutton.place(x = 700, y = 32)
    modibutton.place(x = 780, y = 32)
    removebutton.place(x = 860, y = 32)
    userttk.place(x = 40, y = 200)
    
#회원 수정
def userwindowmodi():
    user = windowtool('회원 수정')
    userbutton = user.buttontool("회원 선택", incommand = Message_ch_user)
    userbutton.pack(anchor = "center")
#회원 등록
def userwindowadd():
    user = windowtool('회원 등록')
    userbutton = user.buttontool("등록", incommand = Message_in_user)
    userbutton.pack(anchor = "center")
#회원 삭제 
def userwindowremove():
    user = windowtool('회원 삭제')
    userbutton = user.buttontool("삭제", incommand = Message_remove_user)
    userbutton.pack(anchor = "center")
    
    

#대출 창
def rentwindow(title):
    rent = windowtool(title)
    userbutton = rent.buttontool("회원 선택", incommand = Message_ch_user)
    bookbutton = rent.buttontool("도서 선택", incommand = Message_ch_book)
    rentbutton = rent.buttontool("대출", incommand = Message_rent_book)
    cancelbutton = rent.buttontool("취소", incommand = Message_cancel)
    labeluser = rent.labeltool(x = 35, y = 37)
    labelbook = rent.labeltool(x = 35, y = 37)
    labeluser.configure(bg = 'white')
    labelbook.configure(bg = 'white')
    userbutton.place(x = 110, y = 100)
    bookbutton.place(x = 360, y = 100)
    labeluser.place(x = 10, y = 150)
    labelbook.place(x = 270, y = 150)
    rentbutton.place(x = 700, y = 600)
    cancelbutton.place(x = 780, y = 600)
    
            
#want~~부분은 객체변수 작성
def pack(wantpack, where = "top", x = 0, y = 0):
    wantpack.pack(side = where, padx = x, pady = y)

def place(wantplace, X = 0, Y = 0):
        wantplace.place(x = X, y = Y)

def configure(wantconfig, intext):
        wantconfig.configure(text = intext)

#책 정보
bookcolumn = ['제목', '저자', '출판사', 'ISBN', '대출여부']
bookinfo = [("따라하면서 배우는 파이썬과 데이터 과학", "천인국, 박동규, 강영민", "생능출판사", 9788970504773, "대출가능"),
            ("Do it! 점프 투 파이썬", "박응용", "이지스퍼블리싱", 979116303911, "대출불가"),
            ("1일 1로그 100일 완성 IT 지식", "브라이언 W.커니헨", "인사이트", 9788966263301, "대출가능")]
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
