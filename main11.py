glades= { 'a+': 4.5, 'a': 4.0, 'b+':3.5, 'b':3.0, 'c+':2.5, 'c':2.0,'d+':1.5,'d':1.0,'f':0}
print('전체 과목 수 ')
count= int(input())

real_glade=0
total_credit=0
jechul_glade=0
jechul_credit=0
jechul_total_glade=0
ram_glade=0
for i in range(count):
    class_name= input('과목 명 입력해줭:')
    glade= input('등급 입력:')
    credit=int(input('학점 입력:'))

    if glade=='f':
        real_glade = credit* glades[glade]
        total_credit += credit
        ram_glade+=real_glade



    else:
        jechul_glade = credit * glades[glade]
        jechul_credit+=credit
        real_glade=credit*glades[glade]
        total_credit+=credit
        jechul_total_glade+=jechul_glade
        ram_glade+=real_glade

print('제출용:'+ str(jechul_total_glade/jechul_credit)+' gpa:'+str(jechul_credit))
print('열람용:'+ str(ram_glade/total_credit)+' gpa:'+str(total_credit))


