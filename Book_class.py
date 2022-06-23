from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import *
import pandas as pd
import numpy as np
from UI_Class import*
from unicodedata import*
import Rent_Dataframe as RD
pd.options.display.max_columns = None

# 데이터프레임 사용
class Book_DataFrame():
    def __init__(self):

        self.book_data = pd.DataFrame(columns=['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK', 'BOOK_DESCRIPTION', 'BOOK_IMAGE'])


    def Book_list_all(self) :
        intext = []
        # intext = np.empty((0, len(self.book_data['BOOK_ISBN'])))
        for i in range(len(self.book_data['BOOK_ISBN'])):
            # intext = np.append(intext, [set_str(self.book_data.iloc[i]['BOOK_TITLE']) + set_str(self.book_data.iloc[i]['BOOK_AUTHOR']) + set_str(self.book_data.iloc[i]['BOOK_PUB'], 25) +  set_str(str(self.book_data.iloc[i]['BOOK_ISBN']), 13)])
            intext.append([self.book_data.iloc[i]['BOOK_TITLE'], self.book_data.iloc[i]['BOOK_AUTHOR'], self.book_data.iloc[i]['BOOK_PUB'], str(self.book_data.iloc[i]['BOOK_ISBN'])])
        
        return intext


    # 도서 검색
    def Book_Search(self, keyword) :
        out_data = self.book_data.loc[self.book_data['BOOK_TITLE'].str.contains(keyword) | self.book_data['BOOK_AUTHOR'].str.contains(keyword)]
        # intext = np.empty((0, len(out_data['BOOK_ISBN'])))
        intext = []
        # print(out_data)
        if self.book_data['BOOK_TITLE'].str.contains(keyword).any() or self.book_data['BOOK_AUTHOR'].str.contains(keyword).any():
            
            for i in range(len(out_data['BOOK_ISBN'])):
                intext.append([out_data.iloc[i]['BOOK_TITLE'], out_data.iloc[i]['BOOK_AUTHOR'], out_data.iloc[i]['BOOK_PUB'], str(out_data.iloc[i]['BOOK_ISBN'])])

        return intext

    # 도서 등록ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ예외처리 완료ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    def Book_in(self, in_data=[]) :

        if in_data[0] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        
        elif in_data[1] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif in_data[2] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif in_data[3] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif in_data[4] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif in_data[5] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        
        elif in_data[6] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        
        elif in_data[7] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        

        try:
            if in_data[3] == '':
                return 0

            else:
                isbn=int(in_data[3])

        except:
            messagebox.showerror('형식오류', 'ISBN은 숫자로 이루어져 있어야 합니다.')

        else:                            # 가격 문자 예외처리
            try:
                title=in_data[0] 
                author=in_data[1] 
                pub=in_data[2] 
                price=int(in_data[4])
                link=in_data[5] 
                description=in_data[6]
                image = in_data[7]

            except ValueError:
                if in_data[4] == '' :
                    return 0

                else:
                    messagebox.showerror('형식오류', '가격은 숫자로 이루어져 있어야 합니다.')

            else:
                if int(in_data[3]) in self.book_data['BOOK_ISBN'] :      # 이미 중복확인을 했음에도 중복 ISBN으로 등록했을 경우
                    messagebox.showinfo('도서관리프로그램', '이미 등록되어있는 도서입니다.')

                else:
                    check = messagebox.askquestion('도서관리프로그램', '도서를 등록하시겠습니까?')

                    if check=='yes':
                        new_data = pd.DataFrame({'BOOK_ISBN' : [isbn], 'BOOK_TITLE' : [title], 'BOOK_AUTHOR' : [author], 'BOOK_PUB' : [pub], 'BOOK_PRICE' :[price], 'BOOK_LINK' : [link], 'BOOK_DESCRIPTION' : [description], 'BOOK_IMAGE' : [image]})
                        self.book_data = pd.concat([self.book_data, new_data])
                        self.book_data.sort_values('BOOK_TITLE')
                        messagebox.showinfo('도서관리프로그램', '도서가 등록되었습니다.')
                        return True

                    else :
                        messagebox.showinfo('도서관리프로그램', '등록이 취소되었습니다.')
        
    # 특정 도서 정보 확인    
    def Book_info(self, select) :
        data = self.book_data.loc[self.book_data['BOOK_ISBN']==int(select)]
        idx = data.index    #isbn에 따라 인덱스값이 다르기 때문에 index로 찾은 도서 정보의 인덱스 값을 추출
        
        intext = list()

        for i in data:
            intext.append(data.loc[idx[0], i])

        return intext

    # ISBN 중복확인
    def Check_isbn(self, isbn):
        try:                            # 문자에 대한 예외처리
            isbn = int(isbn)
            if (self.book_data['BOOK_ISBN'] == isbn).any():
                messagebox.showerror('중복확인', '\n 중복된 ISBN입니다.')
            else:
                messagebox.showinfo('중복확인', '\n 등록가능한 ISBN입니다.')

        except:
            messagebox.showerror('형식오류', 'ISBN은 숫자로 이루어져 있어야 합니다.\n ex) 9788970504773')
        

    # 도서 수정 isbn 중복 예외처리
    def Check_reisbn(self, bf_isbn, af_isbn):
        try:
            af_isbn = int(af_isbn)
            if af_isbn == bf_isbn:
                messagebox.showerror('도서관리프로그램', '같은 ISBN으로 수정할 수 없습니다.')

            else:
                if (self.book_data['BOOK_ISBN'] == int(af_isbn)).any():
                    messagebox.showerror('중복확인', '\n 중복된 ISBN입니다.')
                else:
                    messagebox.showinfo('중복확인', '\n 등록가능한 ISBN입니다.')
        except:
            messagebox.showerror('형식오류', 'ISBN은 숫자로 이루어져 있어야 합니다.\n ex) 9788970504773')

    # 도서 수정
    def Book_modi(self, check_isbn, modi_data=[]) :
        # check_isbn : 기존 데이터 입력받아 해당 데이터 지정
        # print(modi_data)
        #modi_data의 원소들이 알맞은 변수에 지정될 수 있도록 수정
        if modi_data[0] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        
        elif modi_data[1] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif modi_data[2] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif modi_data[3] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif modi_data[4] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        elif modi_data[5] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')
        
        elif modi_data[6] == '':
            messagebox.showerror('도서관리프로그램', '입력되지 않은 정보가 존재합니다!')

        try:
            if modi_data[3] == '':
                return 0

            else:
                isbn=int(modi_data[3])          # isbn 문자 예외처리

        except:
            messagebox.showerror('형식오류', 'ISBN은 숫자로 이루어져 있어야 합니다.')

        else:
            try:
                if modi_data[4] == '' :
                    return 0

                else:
                    title=modi_data[0] 
                    author=modi_data[1] 
                    pub=modi_data[2] 
                    price=int(modi_data[4])
                    link=modi_data[5] 
                    description=modi_data[6]

            except ValueError:
                messagebox.showerror('형식오류', '가격은 숫자로 이루어져 있어야 합니다.')

            else:
                
                ans = messagebox.askquestion('도서관리프로그램', '해당 도서를 수정하시겠습니까?')

                if ans == 'yes':    
                    self.book_data.loc[(self.book_data['BOOK_ISBN']==int(check_isbn)), ('BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK', 'BOOK_DESCRIPTION')] = (isbn, title, author, pub, price, link, description)
                    self.book_data.to_csv('BOOK.csv', encoding='utf-8', index=False)  #현재 테스트용의 데이터를 사용하고 있으므로 추후 csv 파일을 연결하면 해당 코드 활성화
                    messagebox.showinfo('도서관리프로그램', '도서가 수정되었습니다.')
                    return True

                elif ans:
                    messagebox.showinfo('도서관리프로그램', '도서 수정이 취소되었습니다.')

                else:
                    isbn=int(modi_data[3])
                    title=modi_data[0]
                    author=modi_data[1]
                    pub=modi_data[2]
                    price=int(modi_data[4])
                    link=modi_data[5]
                    # image=modi_data[6]
                    description=modi_data[6]

                    if isbn == int(check_isbn) : # 기능 정의서에는 같은 isbn으로 수정할 수 없게 되어있음
                        messagebox.showerror('도서관리프로그램', '같은 ISBN으로 수정할 수 없습니다.')

                    else: 
                        ans = messagebox.askquestion('도서관리프로그램', '해당 도서를 수정하시겠습니까?')

                        if ans == 'yes':    
                            self.book_data.loc[(self.book_data['BOOK_ISBN']==int(check_isbn)), ('BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK', 'BOOK_DESCRIPTION')] = (isbn, title, author, pub, price, link, description)
                            self.book_data.to_csv('BOOK.csv', encoding='utf-8', index=False)  #현재 테스트용의 데이터를 사용하고 있으므로 추후 csv 파일을 연결하면 해당 코드 활성화
                            messagebox.showinfo('도서관리프로그램', '도서가 수정되었습니다.')
                            return True

                        elif ans:
                            messagebox.showinfo('도서관리프로그램', '도서 수정이 취소되었습니다.')


    # 도서 삭제
    def Book_del(self, isbn) :
        rent = RD.Rent_DF()
        rent.read_csv()
        for i in range(len(isbn)):
            isbn[i] = int(isbn[i])
        if self.book_data['BOOK_ISBN'].isin(isbn).any():
            #대출 중인 도서인지 확인
            if rent.rent['BOOK_ISBN'].isin(isbn).any() and rent.rent.loc[rent.rent['BOOK_ISBN'].isin(isbn),'RETURN_DATE'].isna().any():
                messagebox.showinfo('도서관리프로그램', '※대여중인 도서는 삭제할 수 없습니다.')
            else:
                ask = messagebox.askquestion('도서관리프로그램', '도서를 삭제하시겠습니까?')
                if ask=='yes':
                    if self.book_data['BOOK_ISBN'].isin(isbn).any():
                        self.book_data.drop(self.book_data.loc[self.book_data['BOOK_ISBN'].isin(isbn)].index, inplace=True)
                    # self.book_data.to_csv('BOOK_csv', encoding='utf-8', index=False)
                    messagebox.showinfo('도서관리프로그램', '도서가 삭제되었습니다.')
                    return True
                else:
                    messagebox.showinfo('도서관리프로그램', '취소되었습니다.')

    def readcsv(self):
        self.book_data = pd.read_csv('BOOK.csv', encoding='utf-8')

    def tocsv(self):
        self.book_data.to_csv('BOOK.csv', encoding='utf-8', index=False)


# # 한글, 영어 자리수 맞추기 함수
def set_str(input_s, max_size=26, fill_char=' '):
    l = 0
    for chr in input_s:
        if east_asian_width(chr) in ['F', 'W']:
            l+=2
        else :
            l+=1
    return input_s+fill_char*(max_size-l)


# a = Book_DataFrame()
# a.tocsv()