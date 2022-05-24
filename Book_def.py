from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import menubar as mb
import Rent_View as rv

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
def createNewWindow_book_s(title, window):
    new_win = creatWindow(title, window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    Top_frame = Frame(label1)              #  프레임으로 영역 나누기 - 상단
    Top_frame.pack(side=TOP, expand=True)  
    Bottom_frame = Frame(label1)              # 프레임으로 영역 나누기 - 하단
    Bottom_frame.pack(side=BOTTOM, expand=True)
    new_win.createEntryButton(Top_frame, RIGHT, "도서 등록", cm=lambda:creaNewWindow_book_r('도서 등록', window))
    new_win.createEntryButton(Top_frame, RIGHT,  "대출", cm=lambda:creaNewWindow_book_info('도서 정보', window))
    new_win.createEntry(Top_frame, 40, RIGHT, RIGHT, "도서 조회")
    new_win.createbookinfo(Bottom_frame)

# 도서 등록
def creaNewWindow_book_r(title, window):
    new_win = creatWindow(title,window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    
    # 정보입력
    Top_frame=Frame(label1)
    Top_frame.pack(side=TOP, fill="both")
    # 사진 선택 프레임
    Top_lframe=Frame(Top_frame)
    Top_lframe.pack(side=LEFT, fill='both')
    new_win.photoLabel(Top_lframe, TOP)
    new_win.createNormalButton(Top_lframe, TOP, '사진 선택')
    # 제목 프레임
    sor_frame1 = Frame(Top_frame)
    sor_frame1.pack(fill='both')
    new_win.createEntry(sor_frame1, 30, RIGHT, RIGHT, '제목   ')
    # 저자 프레임
    sor_frame2 = Frame(Top_frame)
    sor_frame2.pack(fill='both')
    new_win.createEntry(sor_frame2, 30, RIGHT, RIGHT, '저자   ')
    # 출판사 프레임
    sor_frame3 = Frame(Top_frame)
    sor_frame3.pack(fill='both')
    new_win.createEntry(sor_frame3, 30, RIGHT, RIGHT, '출판사')
    # ISBN 프레임
    sor_frame4 =Frame(Top_frame)
    sor_frame4.pack(fill='both')
    new_win.createEntryButton(sor_frame4,  RIGHT, '중복확인', cm=lambda: clickButton('중복확인'))
    new_win.createEntry(sor_frame4, 26, RIGHT, RIGHT, 'ISBN  ')
    # 가격 프레임
    sor_frame5 = Frame(Top_frame)
    sor_frame5.pack(fill='both')
    new_win.createEntry(sor_frame5, 30, RIGHT, RIGHT, '가격   ')
    # 저자 프레임
    sor_frame5 = Frame(Top_frame)
    sor_frame5.pack(fill='both')
    new_win.createEntry(sor_frame5, 30, RIGHT, RIGHT, '저자   ')
    # 분류 프레임
    sor_frame6 = Frame(Top_frame)
    sor_frame6.pack(fill='both')
    new_win.createEntry(sor_frame6, 30, RIGHT, RIGHT, '분류   ')
    # 도서 설명
    new_win.createEntry(Top_frame, 50, BOTTOM, LEFT, '도서 설명')
    # 등록/취소 버튼
    Bottom_frame=Frame(label1)
    Bottom_frame.pack(side=BOTTOM)
    new_win.createNormalButton(Bottom_frame, LEFT, '등록')
    new_win.createNormalButton(Bottom_frame, LEFT, '취소')

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
def creaNewWindow_book_info_re(title, window):
    new_win = creatWindow(title, window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    
    # 정보입력
    Top_frame=Frame(label1)
    Top_frame.pack(side=TOP, fill="both")
    # 사진 선택 프레임
    Top_lframe=Frame(Top_frame)
    Top_lframe.pack(side=LEFT, fill='both')
    new_win.photoLabel(Top_lframe, TOP)
    new_win.createNormalButton(Top_lframe, TOP, '사진 선택')
    # 제목 프레임
    sor_frame1 = Frame(Top_frame)
    sor_frame1.pack(fill='both')
    new_win.createEntry(sor_frame1, 30, RIGHT, RIGHT, '제목   ')
    # 저자 프레임
    sor_frame2 = Frame(Top_frame)
    sor_frame2.pack(fill='both')
    new_win.createEntry(sor_frame2, 30, RIGHT, RIGHT, '저자   ')
    # 출판사 프레임
    sor_frame3 = Frame(Top_frame)
    sor_frame3.pack(fill='both')
    new_win.createEntry(sor_frame3, 30, RIGHT, RIGHT, '출판사')
    # ISBN 프레임
    sor_frame4 =Frame(Top_frame)
    sor_frame4.pack(fill='both')
    new_win.createEntryButton(sor_frame4,  RIGHT, '중복확인', cm=lambda: clickButton('중복확인'))
    new_win.createEntry(sor_frame4, 26, RIGHT, RIGHT, 'ISBN  ')
    # 가격 프레임
    sor_frame5 = Frame(Top_frame)
    sor_frame5.pack(fill='both')
    new_win.createEntry(sor_frame5, 30, RIGHT, RIGHT, '가격   ')
    # 저자 프레임
    sor_frame5 = Frame(Top_frame)
    sor_frame5.pack(fill='both')
    new_win.createEntry(sor_frame5, 30, RIGHT, RIGHT, '저자   ')
    # 링크 프레임
    sor_frame6 = Frame(Top_frame)
    sor_frame6.pack(fill='both')
    new_win.createEntry(sor_frame6, 30, RIGHT, RIGHT, '관련링크')
    # 분류 프레임
    sor_frame7 = Frame(Top_frame)
    sor_frame7.pack
    new_win.createEntry(sor_frame7, 30, RIGHT, RIGHT, '분류   ')
    # 대출여부 프레임
    sor_frame8 = Frame(Top_frame)
    sor_frame8.pack(fill='both')
    new_win.createEntry(sor_frame8, 30, RIGHT, RIGHT, '대출여부')
    # 도서 설명
    new_win.createEntry(Top_frame, 50, BOTTOM, LEFT, '도서 설명')
    # 완료,취소 버튼
    Bottom_frame=Frame(label1)
    Bottom_frame.pack(side=BOTTOM)
    new_win.createNormalButton(Bottom_frame, LEFT, '완료')
    new_win.createNormalButton(Bottom_frame, LEFT, '취소')
    

# 도서수정
def createNewWindow_book_m(title, window):
    new_win = creatWindow(title, window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    Top_frame = Frame(label1)                 #  프레임으로 영역 나누기 - 상단
    Top_frame.pack(side=TOP, expand=True)  
    Bottom_frame = Frame(label1)              # 프레임으로 영역 나누기 - 하단
    Bottom_frame.pack(side=BOTTOM, expand=True)
    new_win.createEntryButton(Top_frame, RIGHT,  "수정", cm=lambda:creaNewWindow_book_info_re('도서 정보 수정', window))
    new_win.createEntry(Top_frame, 40, RIGHT, RIGHT, "도서 수정")
    new_win.createbookinfo(Bottom_frame)
    
# 도서 삭제
def createNewWindow_book_del(title, window):
    new_win = creatWindow(title, window)
    WD = new_win.reSelf()
    mb.MenuBar(WD)
    label1 = new_win.createLabel(80, 20)
    label1.pack()
    Top_frame = Frame(label1)              #  프레임으로 영역 나누기 - 상단
    Top_frame.pack(side=TOP, expand=True)  
    Bottom_frame = Frame(label1)              # 프레임으로 영역 나누기 - 하단
    Bottom_frame.pack(side=BOTTOM, expand=True)
    new_win.createEntryButton(Top_frame, RIGHT,  "삭제", cm=lambda: clickButton('삭제'))
    new_win.createEntry(Top_frame, 40,  RIGHT, RIGHT,"도서 삭제")
    new_win.createbookinfo(Bottom_frame)