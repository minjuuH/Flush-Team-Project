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
        # creatWindow.__init__(self, title) # create window 불러오기
        # 테스트 파일 self.book
        self.book_data = pd.DataFrame(columns=['BOOK_ISBN', 'BOOK_TITLE', 'BOOK_AUTHOR', 'BOOK_PUB', 'BOOK_PRICE', 'BOOK_LINK', 'BOOK_IMAGE', 'BOOK_DESCRIPTION'])

        # self.book_data.to_csv('BOOK.csv', encoding='utf-8')
        # self.book.to_csv('BOOK.csv', encoding='utf-8')
        # self.book_data = pd.read_csv('BOOK.csv') # 데이터 프레임 불러오기

    # entry : width + 5 / 메인 창 크기 : 1060x720 
    # 등록되어 있는 도서 출력
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
                # intext = np.append(intext, [set_str(out_data.iloc[i]['BOOK_TITLE']), set_str(out_data.iloc[i]['BOOK_AUTHOR']), set_str(out_data.iloc[i]['BOOK_PUB'], 25), set_str(str(out_data.iloc[i]['BOOK_ISBN']), 13)])
                # intext = np.append(intext, [set_str(self.book_data.iloc[i]['BOOK_TITLE']) + set_str(self.book_data.iloc[i]['BOOK_AUTHOR'], 24) + set_str(self.book_data.iloc[i]['BOOK_PUB'], 15) +  set_str(str(self.book_data.iloc[i]['BOOK_ISBN']), 13)])
                # intext = np.append(intext, [set_str(self.book_data.iloc[i]['BOOK_TITLE']) + '\t\t' + set_str(self.book_data.iloc[i]['BOOK_AUTHOR']) + '\t\t' + set_str(self.book_data.iloc[i]['BOOK_PUB']) + '\t\t' + set_str(str(self.book_data.iloc[i]['BOOK_ISBN']))])
        return intext

    # 도서 등록
    def Book_in(self, in_data=[]) :
        isbn=in_data[3] 
        title=in_data[0] 
        author=in_data[1] 
        pub=in_data[2] 
        price=in_data[4] 
        link=in_data[5] 
        description=in_data[6]
        
        if isbn in self.book_data['BOOK_ISBN'] : # 이미 중복확인을 했음에도 중복 ISBN으로 등록했을 경우
            messagebox.showinfo('도서관리프로그램', '이미 등록되어있는 도서입니다.')
        
        elif in_data[0] == '':      # 정보 미입력 예외처리
            if in_data[1] == '':
                if in_data[2] == '':
                    if in_data[3] == '':
                        if in_data[4] == '':
                            if in_data[5] == '':
                                if in_data[6] == '':
                                    messagebox.showerror('도서관리프로그램', '모든 정보를 입력해주세요')
                                else:
                                    messagebox.showerror('도서관리프로그램', '제목, 저자, 출판사, ISBN, 가격, 관련링크를 입력해주세요')
                            else:
                                messagebox.showerror('도서관리프로그램', '제목, 저자, 출판사, ISBN, 가격을 입력해주세요')
                        else:
                            messagebox.showerror('도서관리프로그램', '제목, 저자, 출판사를 입력해주세요')
                    else:
                        messagebox.showerror('도서관리프로그램', '제목, 저자를 입력해주세요')
                else:
                    messagebox.showerror('도서관리프로그램', '제목을 입력해주세요')

        elif in_data[1] == '':      # 제목 입력 됨
            if in_data[2] == '':
                if in_data[3] == '':
                    if in_data[4] == '':
                        if in_data[5] == '':
                            if in_data[6] == '':
                                messagebox.showerror('도서관리프로그램', '저자, 출판사, ISBN, 가격, 관련링크, 도서 설명을 입력해주세요')
                            else:
                                messagebox.showerror('도서관리프로그램', '저자, 출판사, ISBN, 가격, 관련링크를 입력해주세요')
                        else:
                            messagebox.showerror('도서관리프로그램', '저자, 출판사, ISBN, 가격을 입력해주세요')
                    else:
                        messagebox.showerror('도서관리프로그램', '저자, 출판사, ISBN을 입력해주세요')
                else: 
                    messagebox.showerror('도서관리프로그램', '저자, 출판사를 입력해주세요')
            else:
                messagebox.showerror('도서관리프로그램', '저자를 입력해주세요')

        elif in_data[2] == '':      # 제목, 저자 입력 됨
            if in_data[3] == '':
                if in_data[4] == '':
                    if in_data[5] == '':
                        if in_data[6] == '':
                            messagebox.showerror('도서관리프로그램', '출판사, ISBN, 가격, 관련링크, 도서 설명을 입력해주세요')
                        else:
                            messagebox.showerror('도서관리프로그램', '출판사, ISBN, 가격, 관련링크를 입력해주세요')
                    else:
                        messagebox.showerror('도서관리프로그램', '출판사, ISBN, 가격을 입력해주세요')
                else:
                    messagebox.showerror('도서관리프로그램', '출판사, ISBN을 입력해주세요')
            else:
                messagebox.showerror('도서관리프로그램', '출판사를 입력해주세요')

        elif in_data[3] == '':      # 제목, 저자, 출판사
            if in_data[4] == '':
                if in_data[5] == '':
                    if in_data[6] == '':
                        messagebox.showerror('도서관리프로그램', 'ISBN, 가격, 관련링크, 도서 설명을 입력해주세요')
                    else:
                        messagebox.showerror('도서관리프로그램', 'ISBN, 가격, 관련링크를 입력해주세요')
                else:
                    messagebox.showerror('도서관리프로그램', 'ISBN, 가격를 입력해주세요')
            else:
                messagebox.showerror('도서관리프로그램', 'ISBN을 입력해주세요')
        
        elif in_data[4] == '':      # 제목, 저자, 출판사, ISBN
            if in_data[5] == '':
                if in_data[6] == '':
                    messagebox.showerror('도서관리프로그램', '가격, 관련링크, 도서 설명을 입력해주세요')
                else:
                    messagebox.showerror('도서관리프로그램', '가격, 관련링크를 입력해주세요')
            else:
                messagebox.showerror('도서관리프로그램', '가격을 입력해주세요')

        elif in_data[5] == '' :     # 제목, 저자, 출판사, ISBN, 가격
            if in_data[6] == '':
                messagebox.showerror('도서관리프로그램', '관련링크, 도서 설명을 입력해주세요')
            else:
                messagebox.showerror('도서관리프로그램', '관련링크를 입력해주세요')

        elif in_data[6] == '' :     # 도서 설명 외 모든 정보 입력 됨
            messagebox.showerror('도서관리프로그램', '도서 설명을 입력해주세요')

        else :
            check = messagebox.askquestion('도서관리프로그램', '도서를 등록하시겠습니까?')

            if check=='yes':
                new_data = pd.DataFrame({'BOOK_ISBN' : [isbn], 'BOOK_TITLE' : [title], 'BOOK_AUTHOR' : [author], 'BOOK_PUB' : [pub], 'BOOK_PRICE' :[price], 'BOOK_LINK' : [link], 'BOOK_DESCRIPTION' : [description]})
                self.book_data = pd.concat([self.book_data, new_data])
                self.book_data.sort_values('BOOK_TITLE')
                messagebox.showinfo('도서관리프로그램', '도서가 등록되었습니다.')
                return True
                # self.book_data.to_csv('BOOK.CSV', encoding='utf-8', index = False)

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
        if (self.book_data['BOOK_ISBN'] == int(isbn)).any():
            messagebox.showerror('중복확인', '\n 중복된 ISBN입니다.')
        else:
            messagebox.showinfo('중복확인', '\n 등록가능한 ISBN입니다.')

    # 도서 수정 isbn 중복 예외처리
    def Check_reisbn(self, bf_isbn, af_isbn):
        if af_isbn == bf_isbn:
            messagebox.showerror('도서관리프로그램', '같은 ISBN으로 수정할 수 없습니다.')

        else:
            if (self.book_data['BOOK_ISBN'] == int(af_isbn)).any():
                messagebox.showerror('중복확인', '\n 중복된 ISBN입니다.')
            else:
                messagebox.showinfo('중복확인', '\n 등록가능한 ISBN입니다.')

    # 도서 수정
    def Book_modi(self, check_isbn, modi_data=[]) :
        # check_isbn : 기존 데이터 입력받아 해당 데이터 지정
        # print(modi_data)
        #modi_data의 원소들이 알맞은 변수에 지정될 수 있도록 수정
        isbn=modi_data[3]
        title=modi_data[0]
        author=modi_data[1]
        pub=modi_data[2]
        price=modi_data[4]
        link=modi_data[5]
        # image=modi_data[6]
        description=modi_data[6]

        if (self.book_data['BOOK_ISBN']==check_isbn).any():
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

        else:
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



#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ출력 테스트ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# # 등록되어 있는 도서 출력
# book_data=pd.DataFrame({'BOOK_ISBN':[9788970504773,9791163030911,9788966263301, 9791160507812], 
#                     'BOOK_TITLE':['파이썬과 데이터 과학', '점프투파이썬', 'it 지식', '모두의 데이터분석'],
#                     'BOOK_AUTHOR':['천인국, 박동규, 강영민', '박응용', '브라이언', '송석리, 이현아'], 
#                     'BOOK_PUB':['생능출판사','이지스퍼블리싱','인사이트','길벗'], 
#                     'BOOK_PRICE':[26000, 18800, 20000, 19000], 
#                     'BOOK_LINK':['http://www.yes24.com','http://www.yes24.com','http://www.yes24.com','http://www.yes24.com'],
#                     'BOOK_DESCRIPTION':['파이썬 교재','파이썬 교재','it 교재','파이선 데이터 분석']})
# def Book_list_all() :
#     intext = np.empty((0, len(book_data['BOOK_ISBN'])))
#     for i in range(len(book_data['BOOK_ISBN'])):
#         intext = np.append(intext, [set_str(book_data.iloc[i]['BOOK_TITLE']) + set_str(book_data.iloc[i]['BOOK_AUTHOR'], 24) + set_str(book_data.iloc[i]['BOOK_PUB'], 15) +  set_str(str(book_data.iloc[i]['BOOK_ISBN']), 13)])
#     return intext
# print(Book_list_all())


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 논리 테스트(Select 함수) ㅡㅡㅡㅡㅡㅡㅡㅡ
# import numpy as np
# a = np.array([[1,2,3], [4,5,6]])
# b = []
# for i in range(len(a)):
#     b.append({i : a[i][0]})
# for i in range(len(b)):
#     #print(b[i].keys())
#     for j in b[i].values():
#         print(j)

    # # 도서 검색
    # def Book_Search(self, keyword) :
    #     out_data = self.book_data.loc[self.book_data['BOOK_TITLE'].str.contains(keyword) | self.book_data['BOOK_AUTHOR'].str.contains(keyword)]
    #     # intext = np.empty((0, len(out_data['BOOK_ISBN'])))
    #     intext = []
    #     print(out_data)
    #     if self.book_data['BOOK_TITLE'].str.contains(keyword).any() or self.book_data['BOOK_AUTHOR'].str.contains(keyword).any():
            
    #         for i in range(len(out_data['BOOK_ISBN'])):
    #             intext.append([out_data.iloc[i]['BOOK_TITLE'], out_data.iloc[i]['BOOK_AUTHOR'], out_data.iloc[i]['BOOK_PUB'], str(out_data.iloc[i]['BOOK_ISBN'])])
    #             # intext = np.append(intext, [set_str(out_data.iloc[i]['BOOK_TITLE']), set_str(out_data.iloc[i]['BOOK_AUTHOR']), set_str(out_data.iloc[i]['BOOK_PUB'], 25), set_str(str(out_data.iloc[i]['BOOK_ISBN']), 13)])
    #             # intext = np.append(intext, [set_str(self.book_data.iloc[i]['BOOK_TITLE']) + set_str(self.book_data.iloc[i]['BOOK_AUTHOR'], 24) + set_str(self.book_data.iloc[i]['BOOK_PUB'], 15) +  set_str(str(self.book_data.iloc[i]['BOOK_ISBN']), 13)])
    #             # intext = np.append(intext, [set_str(self.book_data.iloc[i]['BOOK_TITLE']) + '\t\t' + set_str(self.book_data.iloc[i]['BOOK_AUTHOR']) + '\t\t' + set_str(self.book_data.iloc[i]['BOOK_PUB']) + '\t\t' + set_str(str(self.book_data.iloc[i]['BOOK_ISBN']))])
    #     return intext
# a = Book_DataFrame()
# a.readcsv()
# # print(a.Book_Search('지식'))
# print()