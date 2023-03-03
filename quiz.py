cdate = '1980-01-19'
x = cdate.split('-')
# print(x)
years = int(x[0])
months = int(x[1])
days = int(x[2])
sumyears = years + months + days
print(sumyears)