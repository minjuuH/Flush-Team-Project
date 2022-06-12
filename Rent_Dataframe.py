import pandas as pd
import os.path
import datetime as dt

class Rent_DF:
    def __init__(self):
        self.book = pd.read_csv('BOOK.csv', encoding = 'utf-8')
        self.user = pd.read_csv('USER.csv', encoding = 'utf-8')
        self.rent = pd.DataFrame(columns=['BOOK_ISBN', 'USER_PHONE', 'RENT_DATE', 'RETURN_DUE_DATE', 'RETURN_DATE'])
        self.rent_book = list()
        self.rent_user = None

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
            return self.rent[self.rent['USER_PHONE']==user_phone]
        else:
            print('대출 정보가 없습니다.')
    
    #작업 중인 코드
    # def changeB(self, book_isbn):
    #     self.book[self.book['BOOK_ISBN']==book_isbn]

    def Rent_return(self, user_phone):
        # user_phone = user['USER_PHONE'][3]

        #외부에서 작업할 내역
        #선택한 회원의 대출 정보가 있는지 검사
        # if (self.rent['USER_PHONE']==user_phone).any:
        #     print(rent[rent['USER_PHONE']==user_phone])
        # else:
        #     print('대출 정보가 없습니다.')
        #     quit()

        re_day = dt.datetime.now().date()
        
        overdue = dt.timedelta()
        for i in self.rent[self.rent['USER_PHONE']==user_phone].index:
            self.rent.loc[i, 'RETURN_DATE'] = re_day
            #도서를 반납하는만큼 회원의 도서대출권수를 줄여준다.
            self.user.loc[self.user['USER_PHONE']==user_phone, 'USER_RENT_CNT'] -= 1

            #대출 정보에 문자열로 저장된 반납예정일 데이터를 date 타입으로 변경
            re_due_day = dt.datetime.strptime(self.rent['RETURN_DUE_DATE'][i], '%Y-%m-%d').date()
            #더 많이 연체된 날짜만큼 대출가능일을 늦추기 위해
            if overdue < re_day-re_due_day:     
                overdue = re_day-re_due_day

        if overdue <= dt.timedelta(0):
            print('연체된 도서가 없습니다.')
            return True
        else:
            #대출가능일 지정
            self.user.loc[self.user['USER_PHONE']==user_phone, 'USER_RENT_ALW']=re_day+overdue
            #경고횟수 추가
            self.user.loc[self.user['USER_PHONE']==user_phone, 'USER_WARN']+=1
            #print('연체되었습니다.')
            #print('대출가능일 : {}'.format((re_day+overdue).strftime('%Y.%m.%d')))
            return False

    def Rent_replus(self, user_phone):
        # user_phone = user['USER_PHONE'][1]
        
        # #선택한 회원의 대출 정보가 있는지 검사
        # if (rent['USER_PHONE']==user_phone).any:
        #     print(rent[rent['USER_PHONE']==user_phone])
        # else:
        #     print('대출 정보가 없습니다.')
        #     quit()

        idx = self.rent[self.rent['USER_PHONE']==user_phone].index
        #print(idx[0])
        re_due_day = dt.datetime.strptime(self.rent.loc[idx[0], 'RETURN_DUE_DATE'], '%Y-%m-%d').date()
        self.rent.loc[idx[0], 'RETURN_DUE_DATE'] = re_due_day+dt.timedelta(days=7)  #연장할 도서 선택
        #print('연장 완료되었습니다.')
        #print('반납예정일 : {}'.format((rent.loc[idx[0], 'RETURN_DUE_DATE']).strftime('%Y.%m.%d')))


# book = pd.read_csv('BOOK.csv', encoding = 'utf-8')
# user = pd.read_csv('USER.csv', encoding = 'utf-8')

# #초기 대출 정보 설정
# rent_user = user['USER_PHONE'][3]
# rent = pd.DataFrame(columns=['BOOK_ISBN', 'USER_PHONE', 'RENT_DATE', 'RETURN_DUE_DATE', 'RETURN_DATE'])
# rent = pd.DataFrame({'BOOK_ISBN' : [book['BOOK_ISBN'][0], book['BOOK_ISBN'][1]],
#                      'USER_PHONE' : [rent_user]*2,
#                      'RENT_DATE' : [dt.date(2022, 5, 8),dt.date(2022, 5, 13)],
#                      'RETURN_DUE_DATE' : [dt.date(2022, 5, 15),dt.date(2022, 5, 20)],
#                      'RETURN_DATE': [None]*2})

# user.loc[user['USER_PHONE']==rent_user, 'USER_RENT_CNT'] += len(rent)

# rent.to_csv('RENT.csv', index = False, encoding = 'utf-8')
# user.to_csv('USER.csv', index = False, encoding = 'utf-8')

# #대출 정보 추가
# def Rent_Add():
#     book = pd.read_csv('BOOK.csv', encoding = 'utf-8')
#     user = pd.read_csv('USER.csv', encoding = 'utf-8')
#     rent = pd.read_csv('RENT.csv', encoding = 'utf-8')

#     #한 회원이 두 권의 책을 빌리려고 하는 경우
#     rent_book = [book['BOOK_ISBN'][2], book['BOOK_ISBN'][1]]    #대출도서의 정보는 해당 도서의 isbn으로 저장
#     rent_user = user['USER_PHONE'][1]                           #대출회원의 정보는 해당 회원의 전화번호로 저장
#     rent_day = [dt.datetime.now().date()]*2                     #대출 기능을 수행하는 당일을 대출일로 저장
#     re_day = [dt.datetime.now().date()+dt.timedelta(days=7)]*2  #대출일로부터 7일 뒤를 반납예정일로 저장

#     add_rent = pd.DataFrame({'BOOK_ISBN' : rent_book,
#                          'USER_PHONE' : [rent_user]*2,
#                          'RENT_DATE' : rent_day,
#                          'RETURN_DUE_DATE' : re_day})

#     for i in add_rent.index:
#         if (rent['BOOK_ISBN']==add_rent['BOOK_ISBN'][i]).any():
#             print("대출 불가능한 도서입니다.")
#             add_rent = add_rent.drop([i])   #이미 저장된 도서는 중복 저장할 수 없으므로 목록에서 삭제
#         else:
#             print("대출 가능한 도서입니다.")

#     rent = pd.concat([rent, add_rent], ignore_index=True)
#     #도서를 대출하는 회원의 도서대출권수를 대출한 도서만큼 더해준다.
#     user.loc[user['USER_PHONE']==rent_user, 'USER_RENT_CNT'] += len(add_rent)

#     print(rent)
#     rent.to_csv('RENT.csv', index = False, encoding = 'utf-8')
#     user.to_csv('USER.csv', index = False, encoding = 'utf-8')
    
# #대출 정보 삭제(반납)
# def Rent_return():
#     user = pd.read_csv('USER.csv', encoding = 'utf-8')
#     rent = pd.read_csv('RENT.csv', encoding = 'utf-8')

#     user_phone = user['USER_PHONE'][3]
#     #선택한 회원의 대출 정보가 있는지 검사
#     if (rent['USER_PHONE']==user_phone).any:
#         print(rent[rent['USER_PHONE']==user_phone])
#     else:
#         print('대출 정보가 없습니다.')
#         quit()

#     re_day = dt.datetime.now().date()
    
#     overdue = dt.timedelta()
#     for i in rent[rent['USER_PHONE']==user_phone].index:
#         rent.loc[i, 'RETURN_DATE'] = re_day
#         #도서를 반납하는만큼 회원의 도서대출권수를 줄여준다.
#         user.loc[user['USER_PHONE']==user_phone, 'USER_RENT_CNT'] -= 1

#         re_due_day = dt.datetime.strptime(rent['RETURN_DUE_DATE'][i], '%Y-%m-%d').date()
#         #더 많이 연체된 날짜만큼 대출가능일을 늦추기 위해
#         if overdue < re_day-re_due_day:     
#             overdue = re_day-re_due_day

#     if overdue <= dt.timedelta(0):
#         print('연체된 도서가 없습니다.')
#     else:
#         #대출가능일 지정
#         user.loc[user['USER_PHONE']==user_phone, 'USER_RENT_ALW']=re_day+overdue
#         #경고횟수 추가
#         user.loc[user['USER_PHONE']==user_phone, 'USER_WARN']+=1
#         print('연체되었습니다.')
#         print('대출가능일 : {}'.format((re_day+overdue).strftime('%Y.%m.%d')))

#     rent.to_csv('RENT.csv', index = False, encoding = 'utf-8')
#     user.to_csv('USER.csv', index = False, encoding = 'utf-8')
        
# #대출 정보 수정(반납예정일 연장)
# def Rent_replus():
#     user = pd.read_csv('USER.csv', encoding = 'utf-8')
#     rent = pd.read_csv('RENT.csv', encoding = 'utf-8')

#     user_phone = user['USER_PHONE'][1]
#     #선택한 회원의 대출 정보가 있는지 검사
#     if (rent['USER_PHONE']==user_phone).any:
#         print(rent[rent['USER_PHONE']==user_phone])
#     else:
#         print('대출 정보가 없습니다.')
#         quit()

#     idx = rent[rent['USER_PHONE']==user_phone].index
#     print(idx[0])
#     re_due_day = dt.datetime.strptime(rent.loc[idx[0], 'RETURN_DUE_DATE'], '%Y-%m-%d').date()
#     rent.loc[idx[0], 'RETURN_DUE_DATE'] = re_due_day+dt.timedelta(days=7)  #연장할 도서 선택
#     print('연장 완료되었습니다.')
#     print('반납예정일 : {}'.format((rent.loc[idx[0], 'RETURN_DUE_DATE']).strftime('%Y.%m.%d')))

#     rent.to_csv('RENT.csv', index = False, encoding = 'utf-8')
#     user.to_csv('USER.csv', index = False, encoding = 'utf-8')

