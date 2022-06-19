import pandas as pd
import os.path
import datetime as dt

class Rent_DF:
    def __init__(self):
        self.book = pd.read_csv('BOOK.csv', encoding = 'utf-8')
        self.user = pd.read_csv('USER.csv', encoding = 'utf-8')
        self.rent = pd.DataFrame(columns=['BOOK_ISBN', 'USER_PHONE', 'RENT_DATE', 'RETURN_DUE_DATE', 'RETURN_DATE'])
        #대출 시 사용할 멤버변수
        self.rent_book = list()
        self.rent_user = None
        #반납 시 사용할 멤버변수
        self.re_book = list()
        self.re_user = None

    def read_csv(self):
        if os.path.isfile('RENT.csv'):
            self.rent = pd.read_csv('RENT.csv', encoding = 'utf-8')

    def to_csv(self):
        self.user.to_csv('USER.csv', index = False, encoding = 'utf-8')
        self.rent.to_csv('RENT.csv', index = False, encoding = 'utf-8')

    def Rent_Add(self):
        rent_day = [dt.datetime.now().date()]*len(self.rent_book)                     #대출 기능을 수행하는 당일을 대출일로 저장
        re_day = [dt.datetime.now().date()+dt.timedelta(days=7)]*len(self.rent_book)  #대출일로부터 7일 뒤를 반납예정일로 저장

        self.add_rent = pd.DataFrame({'BOOK_ISBN' : self.rent_book,
                            'USER_PHONE' : [self.rent_user]*len(self.rent_book),
                            'RENT_DATE' : rent_day,
                            'RETURN_DUE_DATE' : re_day})

        self.rent = pd.concat([self.rent, self.add_rent], ignore_index=True)
        #도서를 대출하는 회원의 도서대출권수를 대출한 도서만큼 더해준다.
        self.user.loc[self.user['USER_PHONE']==self.rent_user, 'USER_RENT_CNT'] += len(self.add_rent)

    def existence(self, user_phone):
        #선택한 회원의 대출 정보 검사
        if (self.rent['USER_PHONE']==user_phone).any:
            info = self.rent[self.rent['USER_PHONE']==user_phone]
            return info[info['RETURN_DATE'].isna()]    #반납되지 않은 대출 정보만 리턴

    #선택한 회원이 대출 가능한 상태인지 확인
    def rent_allow(self, user_phone):
        rent_user = self.user[self.user['USER_PHONE']==user_phone]
        idx = rent_user.index
        if rent_user['USER_RENT_ALW'].isna().all():
            return True
        else:
            alw_day = dt.datetime.strptime(rent_user.loc[idx[0],'USER_RENT_ALW'], '%Y-%m-%d').date()
            if alw_day <= dt.datetime.today().date():
                return True
            else:
                return False

    def Rent_return(self):
        self.re_day = dt.datetime.now().date()
        
        overdue = dt.timedelta()
        for i in self.existence(self.re_user).index:
            if self.rent.loc[i,'BOOK_ISBN'] in self.re_book:    #선택된 도서만 반납되도록 함
                self.rent.loc[i, 'RETURN_DATE'] = self.re_day
                #도서를 반납하는만큼 회원의 도서대출권수를 줄여준다. -> 계산 오류로 인한 수정
                self.user.loc[self.user['USER_PHONE']==self.re_user, 'USER_RENT_CNT'] -= 1

                #대출 정보에 문자열로 저장된 반납예정일 데이터를 date 타입으로 변경
                self.re_due_day = dt.datetime.strptime(self.rent['RETURN_DUE_DATE'][i], '%Y-%m-%d').date()
                #더 많이 연체된 날짜만큼 대출가능일을 늦추기 위해
                if overdue < self.re_day-self.re_due_day: 
                    overdue = self.re_day-self.re_due_day

        if overdue <= dt.timedelta(0):
            return True
        else:
            #대출가능일 지정
            self.alw_day = self.re_day+overdue
            self.user.loc[self.user['USER_PHONE']==self.re_user, 'USER_RENT_ALW']=self.alw_day
            #경고횟수 추가
            self.user.loc[self.user['USER_PHONE']==self.re_user, 'USER_WARN']+=1
            return False

    def Rent_replus(self, isbn):
        info = self.rent[self.rent['BOOK_ISBN']==isbn]
        idx = info[info['RETURN_DATE'].isna()].index
        re_due_day = dt.datetime.strptime(self.rent.loc[idx[0], 'RETURN_DUE_DATE'], '%Y-%m-%d').date()
        self.rent.loc[idx[0], 'RETURN_DUE_DATE'] = re_due_day+dt.timedelta(days=7)  #연장할 도서 선택
        return self.rent.loc[idx[0], 'RETURN_DUE_DATE']
