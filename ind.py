# 1. Напишите рекурсивную функцию, проверяющую правильность расстановки скобок в строке.
# При правильной расстановке выполняются условия:
# количество открывающих и закрывающих скобок равно.
# внутри любой пары открывающая – соответствующая закрывающая скобка, скобки
# расставлены правильно.
# Примеры неправильной расстановки: )(, ())(, ())(() и т. п

def check_brackets(stri):
    left=stri.find("(")
    right=stri.rfind(")")
    if left==-1 and right==-1:
        return True
    elif left==-1 or right==-1 or right < left: 
        return False
    else:
        return check_brackets(stri[left+1:right])
print(check_brackets(input('>>> ')))