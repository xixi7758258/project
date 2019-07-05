#存放日期处理的函数
import datetime

def expire(expire_time):
    #获取当前日期
    now = datetime.date.today()
    #获取到期日期
    after = datetime.date(expire_time.year,expire_time.month,expire_time.day)
    
    delta = after - now
    return delta.days

