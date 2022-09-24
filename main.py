import time as t
import win10toast as w

print('Вас приветствует программа будильник!')
print('на сколько вы бы хотели поставить будильник?')
hours=int(input('часы: '))
minut=int(input('минуты: '))
while True:
    hours1 = t.localtime()
    hours1 = hours1.tm_hour
    minut1 = t.localtime()
    minut1 = minut1.tm_min
    if hours==hours1 and minut==minut1:
        toast=w.ToastNotifier()
        toast.show_toast("Будильник",'Вы поставили будильник на',)
        quit()
    else:
        #print('ждём')
        print(hours1,minut1)
        print(hours,minut)
        continue