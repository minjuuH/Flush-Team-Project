from re import T
from tkinter import *
from tkinter import messagebox
import Rent_View as rv
import UI_Class as UC

class creatWindow:
    def __init__(self, title, window):
        self.newWindow = Toplevel(window)
        self.newWindow.title(title)
        self.newWindow.geometry("960x720")
        
    def createLabel(self, w, h):
        label = Label(self.newWindow, width=w, height=h)
        return label

    def reSelf(self):
        return self.newWindow

    def photoLabel(self, window, pos):
        #Img = PhotoImage(adress)
        label=Label(master = window, text= '사진', width=30, height=20)
        label.pack(side=pos)

    def createEntry(self, window, size, pos, tpos,showText):
        Entry_title = Label(window, text = showText)
        input_text = Entry(window, width=size, bd = 3, font=('돋움', 20))
        input_text.pack(side = pos, padx=5, pady=10)
        Entry_title.pack(side=tpos) 
        
    def createEntryButton(self, window, pos, showText, cm=None):
        button = Button(window, text=showText, command=cm)
        button.pack(side=pos, padx=5, pady=10)
        #button.bind("<Button>", clickButton)

    def createNormalButton(self, window, pos, showText) :
        def clickButton(event) :
            messagebox.showinfo(showText, '버튼이 실행되었습니다.')
        nor_button = Button(window, text=showText)
        nor_button.pack(side=pos, ipadx=20, ipady=20)
        nor_button.bind("<Button>", clickButton)

    def createbookinfo(self, window) :
        col = ['','','','','']
        book_info = ttk.Treeview(window, columns = ['','','','',''], displaycolumns=['','','','',''])
        for i in range(5):
            book_info.column(col[i], width = 200, anchor="center") #컬럼 상세 설정
            book_info.heading(col[i], text = col[i], anchor = "center") #표 헤더 설정

        # for i in range(len(book_data)) :
        #     book_info.insert('', 'end', text = i, values = book_data[i])
        book_info['show'] = 'headings'
        book_info.pack(expand=1, anchor=CENTER)

#메시지창 출력 이벤트
def clickButton(showText) :
    messagebox.showinfo(showText, "버튼이 실행되었습니다.")

# 도서조회
def createNewWindow_book_s(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 조회')
    else:
        new_win=window
        new_win.Change_Frame('도서 조회')

    new_win.Search_bar()
    new_win.createButton('등록', new_win.baseLabel)
    new_win.createButton('대출', new_win.baseLabel)
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ")


# 도서 등록
def createNewWindow_book_r(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 등록')
    else:
        new_win=window
        new_win.Change_Frame('도서 등록')

    new_win.input_set('도서 등록')
    new_win.entry_set('제목', 1)
    new_win.entry_set('저자', 2)
    new_win.entry_set('출판사', 3)
    new_win.entry_set('ISBN', 4, True)
    new_win.entry_set('가격', 6)
    new_win.entry_set('관련링크', 7)
    new_win.book_ex()
    new_win.under_button('등록', new_win.base_frame)

# 도서 정보
def creaNewWindow_book_info(title, window):
    new_win = creatWindow(title, window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    
    # 정보입력
    Top_frame=Frame(label1)
    Top_frame.pack(side=TOP, fill="both")
    # 사진 선택 프레임
    new_win.photoLabel(Top_frame, LEFT)
    # 도서 정보 출력
    data_frame1 = Frame(Top_frame)
    data_frame1.pack(side=LEFT, fill='both')
    new_win.createbookinfo(data_frame1)
    # 도서 설명
    data_frame2=Frame(Top_frame)
    data_frame2.pack(side=BOTTOM, fill='both')
    new_win.createbookinfo(data_frame1)   
    # 대출, 수정, 삭제, 닫기 버튼
    Bottom_frame=Frame(label1)
    Bottom_frame.pack(side=BOTTOM, fill="both")
    Bottom_bframe=Frame(Bottom_frame)
    Bottom_bframe.pack(anchor=CENTER, fill='both')
    # 대출 프레임
    mo_frame = Frame(Bottom_bframe)
    mo_frame.pack(side=LEFT, fill='both')
    new_win.createEntryButton(mo_frame, BOTTOM, '대출', cm=lambda:rv.Rent_Screen(window))
    # 수정 프레임
    re_frame = Frame(Bottom_bframe)
    re_frame.pack(side=LEFT, fil='both')
    new_win.createEntryButton(re_frame, BOTTOM, '수정', cm=lambda:creaNewWindow_book_info_re('도서 정보 수정', window))
    # 삭제 프레임
    del_frame = Frame(Bottom_bframe)
    del_frame.pack(side=LEFT, fil='both')
    new_win.createNormalButton(del_frame, BOTTOM, '삭제')
    # 닫기 프레임
    close_frame = Frame(Bottom_bframe)
    close_frame.pack(side=LEFT, fil='both')
    new_win.createNormalButton(close_frame, BOTTOM, '닫기')

# 도서 정보 수정
def creaNewWindow_book_info_re(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 수정')
    else:
        new_win=window
        new_win.Change_Frame('도서 수정')

    new_win.input_set('도서 수정')
    new_win.entry_set('제목', 1)
    new_win.entry_set('저자', 2)
    new_win.entry_set('출판사', 3)
    new_win.entry_set('ISBN', 4, True)
    new_win.entry_set('가격', 6)
    new_win.entry_set('관련링크', 7)
    new_win.book_ex()
    new_win.under_button('완료', new_win.base_frame)
    

# 도서조회(수정)
def createNewWindow_book_m(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 수정')
    else:
        new_win=window
        new_win.Change_Frame('도서 수정')

    new_win.Search_bar()
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t\t", lambda:creaNewWindow_book_info_re(new_win, 1), False)
    
# 도서조회(삭제)
def createNewWindow_book_del(window, choice=None):
    new_win = UC.new_window()
    if choice == None:
        new_win.make_window(window, '도서 삭제')
    else:
        new_win=window
        new_win.Change_Frame('도서 삭제')

    new_win.Search_bar()
    new_win.createButton('삭제', new_win.baseLabel)
    new_win.Book_list("제목\t\t저자\t\t출판사\t\tISBN\t대출여부     ")