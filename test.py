import pyupbit

access = "uqgnR2Eq0CsmeaGNqVgl9ylYUdbIckB3HB9bbRoO"          # 본인 값으로 변경
secret = "xzoPtVqneXo3BJjxNsxjxxKsXCwKimutqE9uc7hr"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-IGNIS"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회