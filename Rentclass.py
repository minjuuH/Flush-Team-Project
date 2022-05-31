import pandas as pd
from datetime import datetime, timedelta
from os.path import isfile


# output은 추후 UI구현 완료 후 수정


class rent:
    # 생성자로 데이터 프레임 생성
    def __init__(self):
        self.book = pd.read_csv('BOOK.csv', encoding='utf-8')
        self.user = pd.read_csv('USER.csv', encoding='utf-8')
        self.rent = pd.DataFrame(columns=['BOOK_ISBN', 'USER_PHONE',
                                          'RENT_DATE', 'RETURN_DUE_DATE', 'RETURN_DATE'])

        # RENT.csv가 없으면 csv 파일 생성
        if not isfile("RENT.csv"):
            rent.to_csv('RENT.csv', index=False, encoding='utf-8')

    def Rent_Add(self, userinfo, book1, book2=None):

        # 한 회원이 두 권의 책을 빌리려고 하는 경우
        if(book2 != None):
            # book1, book2는 ISBN 정보
            rent_book = [book1, book2]
            # 대출회원의 정보는 해당 회원의 전화번호로 저장
            rent_user = userinfo
            # 대출 기능을 수행하는 당일을 대출일로 저장
            rent_day = [datetime.now().date()]*2
            re_day = [datetime.now().date()+timedelta(days=7)] * \
                2  # 대출일로부터 7일 뒤를 반납예정일로 저장
            add_rent = pd.DataFrame({'BOOK_ISBN': rent_book,
                                     'USER_PHONE': [rent_user]*2,
                                     'RENT_DATE': rent_day,
                                     'RETURN_DUE_DATE': re_day})

        # 한 권의 책을 빌리는 경우
        else:
            rent_book = book1                                           # book1은 ISBN 정보
            # 대출회원의 정보는 해당 회원의 전화번호로 저장
            rent_user = userinfo
            # 대출 기능을 수행하는 당일을 대출일로 저장
            rent_day = datetime.now().date()
            re_day = datetime.now().date()+timedelta(days=7)    # 대출일로부터 7일 뒤를 반납예정일로 저장

            add_rent = pd.DataFrame({'BOOK_ISBN': rent_book,
                                     'USER_PHONE': rent_user,
                                     'RENT_DATE': rent_day,
                                     'RETURN_DUE_DATE': re_day})

        for i in add_rent.index:
            if (self.rent['BOOK_ISBN'] == add_rent['BOOK_ISBN'][i]).any():
                add_rent = add_rent.drop([i])
                # 이미 저장된 도서는 중복 저장할 수 없으므로 목록에서 삭제
                output = "대출 불가능한 도서입니다."

        self.rent = pd.concat([self.rent, add_rent], ignore_index=True)
        # 도서를 대출하는 회원의 도서대출권수를 대출한 도서만큼 더해준다.
        self.user.loc[self.user['USER_PHONE'] == rent_user,
                      'USER_RENT_CNT'] += len(add_rent)


def Rent_return(self, reUserInfo):

    user_phone = reUserInfo
    # 선택한 회원의 대출 정보가 있는지 검사
    if (self.rent['USER_PHONE'] == user_phone).any:
        output = self.rent[self.rent['USER_PHONE']
                           == user_phone]       # output은 추후 UI이후 수정
    else:
        output = '대출 정보가 없습니다.'

    re_day = datetime.now().date()

    overdue = timedelta()
    # for i in self.rent[self.rent['USER_PHONE'] == user_phone].index:
    #     self.rent.loc[i, 'RETURN_DATE'] = re_day
    #     # 도서를 반납하는만큼 회원의 도서대출권수를 줄여준다.
    #     self.user.loc[self.user['USER_PHONE']
    #                   == user_phone, 'USER_RENT_CNT'] -= 1

    #     re_due_day = datetime.strptime(
    #         self.rent['RETURN_DUE_DATE'][i], '%Y-%m-%d').date()
    #     # 더 많이 연체된 날짜만큼 대출가능일을 늦추기 위해
    #     if overdue < re_day-re_due_day:
    #         overdue = re_day-re_due_day

    if overdue <= timedelta(0):
        print('연체된 도서가 없습니다.')
    else:
        # 대출가능일 지정
        self.user.loc[self.user['USER_PHONE'] == user_phone,
                      'USER_RENT_ALW'] = re_day+overdue
        # 경고횟수 추가
        self.user.loc[self.user['USER_PHONE'] == user_phone, 'USER_WARN'] += 1
        output = '연체되었습니다.'
        output = '대출가능일 : {}'.format((re_day+overdue).strftime('%Y.%m.%d'))

    def __del__(self):
        self.rent.to_csv('RENT.csv', index=False, encoding='utf-8')
        self.user.to_csv('USER.csv', index=False, encoding='utf-8')
