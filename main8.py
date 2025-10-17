
jns = input("Jinsingizni kiriting (erkak yoki ayol): ").lower()
yosh = int(input("yoshingizni kiriting : "))
if 0 <= yosh <= 120 :
    if jns == "erkak" and yosh >= 60:
        ny = yosh - 60
        if ny == 0 :
            print(f"Bobo siz nafaqa chiqgansiz . \nNafaqaga shu yili chiqgansiz")
        else:
            print(f"Bobo siz nafaqa yoshidasiz . \nNafaqaga chgiqganingizga {ny} yil bo'ldi")
    elif jns == "erkak" and yosh < 60 :
        nafaqa_yosh_erkak = 60 - yosh
        print(f"Hurmatli foydalanuvchi siz hali nafaqaga chiqmagansiz . \nNafaqaga chiqishingizga {nafaqa_yosh_erkak} yil bor .")
    elif jns == "ayol" and yosh < 60 :
        nafaqa_yosh_ayol = yosh - 60
        print(f"Hurmatli foydalanuvchi siz hali nafaqaga chiqmagansiz . \nNafaqaga chiqishingizga {nafaqa_yosh_ayol} yil bor .")
    elif jns == "ayol" and yosh >= 60 :
        nafaqa_yoshiga_yetgan = yosh - 60
        if nafaqa_yoshiga_yetgan == 0 :
            print(f"Buvi siz nafaqa yoshidasiz . \nNafaqaga yaqinda chiqdingiz")
        else:
            print(f"Buvi siz nafaqa yoshidasiz .\nNafaqaga chgiqganingizga {nafaqa_yoshiga_yetgan} yil bo'ldi")
    else:
        print("Hurmatli foydalanuvchi siz jinsingizni to'g'ri kiritishingiz kerak")
else:
    print("Yoshingizni to'g'ri kiriting ! ")