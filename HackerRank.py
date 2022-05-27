grades=[35,38,43,67,61,77]
final_grades=[]
for i in grades:
    if i <38:
        final_grades.append(i)
    else:
        if i%5>=3:
            i=(((i//5)*5)+5)
            final_grades.append(i)

        else :
            final_grades.append(i)

print(final_grades)

