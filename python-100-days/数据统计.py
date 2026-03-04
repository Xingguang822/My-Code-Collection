def ptp(date):
    return max(date)-min(date)
def mean(date):
    return sum(date)/len(date)
def median(date):
    temp,size=sorted(date),len(date)
    if len(date)%2==0:
        return mean(temp[size // 2 - 1:size // 2 + 1])
    else:
        return date[len(date)//2]
def var(date):
    x_bar=mean(date)
    temp=[(num-x_bar)**2 for num in date]
    return sum(temp)/(len(date)-1)
def std(date):
    return var(date)**0.5
def cv(date):
    return std(date)/mean(date)
def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

date_=[i for i in range(1,11)]
describe(date_)
