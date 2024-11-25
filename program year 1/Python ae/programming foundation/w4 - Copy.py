from cmath import sqrt
from tabnanny import check
def check_dk(a, b, c):
    return a + b > c and b + c > a and c + a > b

def triangle_area(a, b, c):
    if a > 0 and b > 0 and c > 0 and check_dk(a, b, c):
        p = (a+b+c) / 2
        semi_total = p*(p-a)*(p-b)*(p-c)
        total = sqrt(semi_total)
        return total
    else:
        return 0

nhap_a = int(input('enter a: '))
nhap_b = int(input('enter b: '))
nhap_c = int(input('enter c: '))


