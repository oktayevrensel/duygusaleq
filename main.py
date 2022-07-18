import tkinter as tk

MainWindow=tk.Tk()
MainWindow.geometry("500x500+250+100")
MainWindow.title("Duygusal Zeka Ölçeği")
score=0
title=tk.Label(MainWindow,text="Duygusal Zeka Ölçeği Testine Hoşgeldiniz",font=["Segoe UI",16])
title.place(x=45,y=120)
content1=tk.Label(MainWindow,text="DUYGUSAL ZEKA ÖZELLİĞİ ÖLÇEĞİ(TEIQue-SF)KISA FORM",font=["Segoe UI",12])
content2=tk.Label(MainWindow,text="Lütfen aşağıdaki her ifadeyi o ifadeye katılma ya da katılmama derecenizi yansıtan rakamı",font=["Segoe UI",8])
content3=tk.Label(MainWindow,text="daire içine alarak cevaplayınız",font=["Segoe UI",8])
content4=tk.Label(MainWindow,text="İfadelerin tam anlamı hakkında çok uzun düşünmeyiniz. Hızlı ilerleyiniz ve kesin cevaplar",font=["Segoe UI",8])
content5=tk.Label(MainWindow,text="vermeye çalışınız. Doğru ya da yanlış cevap yoktur.",font=["Segoe UI",8])
content6=tk.Label(MainWindow,text="1- Katılmıyorum",font=["Segoe UI",8])
content7=tk.Label(MainWindow,text="5- Tamamen Katılıyorum",font=["Segoe UI",8])
content1.place(x=36,y=160)
content2.place(x=10,y=190)
content3.place(x=5,y=205)
content4.place(x=5,y=220)
content5.place(x=5,y=235)
content6.place(x=15,y=250)
content7.place(x=15,y=265)
def soru1():
    def total1():
        global score
        total01=score1.get()
        if total01 == 1:
            score +=1
        elif total01 == 2:
            score +=2
        elif total01 == 3:
            score +=3
        elif total01 == 4:
            score += 4
        else:
            score +=5
    ui1=tk.Toplevel()
    ui1.geometry("500x500+250+100")
    headline1=tk.Label(ui1,text="Soru 1: ",font=["Segoe UI",16])
    question1=tk.Label(ui1,text="Genel anlamda, yüksek motivasyonlu birisiyim.",font=["Segoe UI",12])
    score1=tk.IntVar()
    one1=tk.Radiobutton(ui1,text="1",font=["Segoe UI",12],variable=score1,value=1,command=total1)
    two1=tk.Radiobutton(ui1,text="2",font=["Segoe UI",12],variable=score1,value=2,command=total1)
    three1=tk.Radiobutton(ui1,text="3",font=["Segoe UI",12],variable=score1,value=3,command=total1)
    four1=tk.Radiobutton(ui1,text="4",font=["Segoe UI",12],variable=score1,value=4,command=total1)
    five1=tk.Radiobutton(ui1,text="5",font=["Segoe UI",12],variable=score1,value=5,command=total1)
    def soru2():
        def total2():
            global score
            total02=score2.get()
            if total02 == 1:
                score +=1
            elif total02 == 2:
                score +=2
            elif total02 == 3:
                score +=3
            elif total02 == 4:
                score += 4
            else:
                score +=5
        ui2=tk.Toplevel()
        ui2.geometry("500x500+250+100")
        headline2=tk.Label(ui2,text="Soru 2: ",font=["Segoe UI",16])
        question2=tk.Label(ui2,text="Duygularımı düzenlemekte zorlanmam.",font=["Segoe UI",12])
        score2=tk.IntVar()
        one2=tk.Radiobutton(ui2,text="1",font=["Segoe UI",12],variable=score2,value=1,command=total2)
        two2=tk.Radiobutton(ui2,text="2",font=["Segoe UI",12],variable=score2,value=2,command=total2)
        three2=tk.Radiobutton(ui2,text="3",font=["Segoe UI",12],variable=score2,value=3,command=total2)
        four2=tk.Radiobutton(ui2,text="4",font=["Segoe UI",12],variable=score2,value=4,command=total2)
        five2=tk.Radiobutton(ui2,text="5",font=["Segoe UI",12],variable=score2,value=5,command=total2)
        def soru3():
            def total3():
                global score
                total03=score3.get()
                if total03 == 1:
                    score +=1
                elif total03 == 2:
                    score +=2
                elif total03 == 3:
                    score +=3
                elif total03 == 4:
                    score += 4
                else:
                    score +=5
            ui3=tk.Toplevel()
            ui3.geometry("500x500+250+100")
            headline3=tk.Label(ui3,text="Soru 3: ",font=["Segoe UI",16])
            question3=tk.Label(ui3,text="İnsanlarla etkin bir biçimde baş edebilirim.",font=["Segoe UI",12])
            score3=tk.IntVar()
            one3=tk.Radiobutton(ui3,text="1",font=["Segoe UI",12],variable=score3,value=1,command=total3)
            two3=tk.Radiobutton(ui3,text="2",font=["Segoe UI",12],variable=score3,value=2,command=total3)
            three3=tk.Radiobutton(ui3,text="3",font=["Segoe UI",12],variable=score3,value=3,command=total3)
            four3=tk.Radiobutton(ui3,text="4",font=["Segoe UI",12],variable=score3,value=4,command=total3)
            five3=tk.Radiobutton(ui3,text="5",font=["Segoe UI",12],variable=score3,value=5,command=total3)
            def soru4():
                def total4():
                    global score
                    total04=score4.get()
                    if total04 == 1:
                        score +=1
                    elif total04 == 2:
                        score +=2
                    elif total04 == 3:
                        score +=3
                    elif total04 == 4:
                        score += 4
                    else:
                        score +=5
                ui4=tk.Toplevel()
                ui4.geometry("500x500+250+100")
                headline4=tk.Label(ui4,text="Soru 4: ",font=["Segoe UI",16])
                question4=tk.Label(ui4,text="Verdiğim kararlarımı sıklıkla değiştirme \neğilimim yoktur.",font=["Segoe UI",12])
                score4=tk.IntVar()
                one4=tk.Radiobutton(ui4,text="1",font=["Segoe UI",12],variable=score4,value=1,command=total4)
                two4=tk.Radiobutton(ui4,text="2",font=["Segoe UI",12],variable=score4,value=2,command=total4)
                three4=tk.Radiobutton(ui4,text="3",font=["Segoe UI",12],variable=score4,value=3,command=total4)
                four4=tk.Radiobutton(ui4,text="4",font=["Segoe UI",12],variable=score4,value=4,command=total4)
                five4=tk.Radiobutton(ui4,text="5",font=["Segoe UI",12],variable=score4,value=5,command=total4)
                def soru5():
                    def total5():
                        global score
                        total05=score5.get()
                        if total05 == 1:
                            score +=1
                        elif total05 == 2:
                            score +=2
                        elif total05 == 3:
                            score +=3
                        elif total05 == 4:
                            score += 4
                        else:
                            score +=5
                    ui5=tk.Toplevel()
                    ui5.geometry("500x500+250+100")
                    headline5=tk.Label(ui5,text="Soru 5: ",font=["Segoe UI",16])
                    question5=tk.Label(ui5,text="Çoğu zaman hangi duyguyu hissettiğimi ayırt edebilirim.",font=["Segoe UI",12])
                    score5=tk.IntVar()
                    one5=tk.Radiobutton(ui5,text="1",font=["Segoe UI",12],variable=score5,value=1,command=total5)
                    two5=tk.Radiobutton(ui5,text="2",font=["Segoe UI",12],variable=score5,value=2,command=total5)
                    three5=tk.Radiobutton(ui5,text="3",font=["Segoe UI",12],variable=score5,value=3,command=total5)
                    four5=tk.Radiobutton(ui5,text="4",font=["Segoe UI",12],variable=score5,value=4,command=total5)
                    five5=tk.Radiobutton(ui5,text="5",font=["Segoe UI",12],variable=score5,value=5,command=total5)
                    def soru6():
                        def total6():
                            global score
                            total06=score6.get()
                            if total06 == 1:
                                score +=1
                            elif total06 == 2:
                                score +=2
                            elif total06 == 3:
                                score +=3
                            elif total06 == 4:
                                score += 4
                            else:
                                score +=5
                        ui6=tk.Toplevel()
                        ui6.geometry("500x500+250+100")
                        headline6=tk.Label(ui6,text="Soru 6: ",font=["Segoe UI",16])
                        question6=tk.Label(ui6,text="Birçok iyi özelliğe sahip olduğumu düşünüyorum.",font=["Segoe UI",12])
                        score6=tk.IntVar()
                        one6=tk.Radiobutton(ui6,text="1",font=["Segoe UI",12],variable=score6,value=1,command=total6)
                        two6=tk.Radiobutton(ui6,text="2",font=["Segoe UI",12],variable=score6,value=2,command=total6)
                        three6=tk.Radiobutton(ui6,text="3",font=["Segoe UI",12],variable=score6,value=3,command=total6)
                        four6=tk.Radiobutton(ui6,text="4",font=["Segoe UI",12],variable=score6,value=4,command=total6)
                        five6=tk.Radiobutton(ui6,text="5",font=["Segoe UI",12],variable=score6,value=5,command=total6)
                        def soru7():
                            def total7():
                                global score
                                total07=score7.get()
                                if total07 == 1:
                                    score +=1
                                elif total07 == 2:
                                    score +=2
                                elif total07 == 3:
                                    score +=3
                                elif total07 == 4:
                                    score += 4
                                else:
                                    score +=5
                            ui7=tk.Toplevel()
                            ui7.geometry("500x500+250+100")
                            headline7=tk.Label(ui7,text="Soru 7: ",font=["Segoe UI",16])
                            question7=tk.Label(ui7,text="Haklarımı savunmak benim için genellikle kolaydır",font=["Segoe UI",12])
                            score7=tk.IntVar()
                            one7=tk.Radiobutton(ui7,text="1",font=["Segoe UI",12],variable=score7,value=1,command=total7)
                            two7=tk.Radiobutton(ui7,text="2",font=["Segoe UI",12],variable=score7,value=2,command=total7)
                            three7=tk.Radiobutton(ui7,text="3",font=["Segoe UI",12],variable=score7,value=3,command=total7)
                            four7=tk.Radiobutton(ui7,text="4",font=["Segoe UI",12],variable=score7,value=4,command=total7)
                            five7=tk.Radiobutton(ui7,text="5",font=["Segoe UI",12],variable=score7,value=5,command=total7)
                            def soru8():
                                def total8():
                                    global score
                                    total08=score8.get()
                                    if total08 == 1:
                                        score +=1
                                    elif total08 == 2:
                                        score +=2
                                    elif total08 == 3:
                                        score +=3
                                    elif total08 == 4:
                                        score += 4
                                    else:
                                        score +=5
                                ui8=tk.Toplevel()
                                ui8.geometry("500x500+250+100")
                                headline8=tk.Label(ui8,text="Soru 8: ",font=["Segoe UI",16])
                                question8=tk.Label(ui8,text="Diğer insanların duygularını bir şekilde \netkileyebilme yeteneğim vardır.",font=["Segoe UI",12])
                                score8=tk.IntVar()
                                one8=tk.Radiobutton(ui8,text="1",font=["Segoe UI",12],variable=score8,value=1,command=total8)
                                two8=tk.Radiobutton(ui8,text="2",font=["Segoe UI",12],variable=score8,value=2,command=total8)
                                three8=tk.Radiobutton(ui8,text="3",font=["Segoe UI",12],variable=score8,value=3,command=total8)
                                four8=tk.Radiobutton(ui8,text="4",font=["Segoe UI",12],variable=score8,value=4,command=total8)
                                five8=tk.Radiobutton(ui8,text="5",font=["Segoe UI",12],variable=score8,value=5,command=total8)
                                def soru9():
                                    def total9():
                                        global score
                                        total09=score9.get()
                                        if total09 == 1:
                                            score +=1
                                        elif total09 == 2:
                                            score +=2
                                        elif total09 == 3:
                                            score +=3
                                        elif total09 == 4:
                                            score += 4
                                        else:
                                            score +=5
                                    ui9=tk.Toplevel()
                                    ui9.geometry("500x500+250+100")
                                    headline9=tk.Label(ui9,text="Soru 9: ",font=["Segoe UI",16])
                                    question9=tk.Label(ui9,text="Olayların akışına göre hayatımı düzenlemek benim için \ngenellikle Kolaydır",font=["Segoe UI",12])
                                    score9=tk.IntVar()
                                    one9=tk.Radiobutton(ui9,text="1",font=["Segoe UI",12],variable=score9,value=1,command=total9)
                                    two9=tk.Radiobutton(ui9,text="2",font=["Segoe UI",12],variable=score9,value=2,command=total9)
                                    three9=tk.Radiobutton(ui9,text="3",font=["Segoe UI",12],variable=score9,value=3,command=total9)
                                    four9=tk.Radiobutton(ui9,text="4",font=["Segoe UI",12],variable=score9,value=4,command=total9)
                                    five9=tk.Radiobutton(ui9,text="5",font=["Segoe UI",12],variable=score9,value=5,command=total9)
                                    def soru10():
                                        def total10():
                                            global score
                                            total010=score10.get()
                                            if total010 == 1:
                                                score +=1
                                            elif total010 == 2:
                                                score +=2
                                            elif total010 == 3:
                                                score +=3
                                            elif total010 == 4:
                                                score += 4
                                            else:
                                                score +=5
                                        ui10=tk.Toplevel()
                                        ui10.geometry("500x500+250+100")
                                        headline10=tk.Label(ui10,text="Soru 10: ",font=["Segoe UI",16])
                                        question10=tk.Label(ui10,text="Genelde stresle baş edebilirim.",font=["Segoe UI",12])
                                        score10=tk.IntVar()
                                        one10=tk.Radiobutton(ui10,text="1",font=["Segoe UI",12],variable=score10,value=1,command=total10)
                                        two10=tk.Radiobutton(ui10,text="2",font=["Segoe UI",12],variable=score10,value=2,command=total10)
                                        three10=tk.Radiobutton(ui10,text="3",font=["Segoe UI",12],variable=score10,value=3,command=total10)
                                        four10=tk.Radiobutton(ui10,text="4",font=["Segoe UI",12],variable=score10,value=4,command=total10)
                                        five10=tk.Radiobutton(ui10,text="5",font=["Segoe UI",12],variable=score10,value=5,command=total10)
                                        def soru11():
                                            def total11():
                                                global score
                                                total011=score11.get()
                                                if total011 == 1:
                                                    score +=1
                                                elif total011 == 2:
                                                    score +=2
                                                elif total011 == 3:
                                                    score +=3
                                                elif total011 == 4:
                                                    score += 4
                                                else:
                                                    score +=5
                                            ui11=tk.Toplevel()
                                            ui11.geometry("500x500+250+100")
                                            headline11=tk.Label(ui11,text="Soru 11: ",font=["Segoe UI",16])
                                            question11=tk.Label(ui11,text="Yakınlarıma, duygularımı göstermekte genelde Zorlanmam.",font=["Segoe UI",12])
                                            score11=tk.IntVar()
                                            one11=tk.Radiobutton(ui11,text="1",font=["Segoe UI",12],variable=score11,value=1,command=total11)
                                            two11=tk.Radiobutton(ui11,text="2",font=["Segoe UI",12],variable=score11,value=2,command=total11)
                                            three11=tk.Radiobutton(ui11,text="3",font=["Segoe UI",12],variable=score11,value=3,command=total11)
                                            four11=tk.Radiobutton(ui11,text="4",font=["Segoe UI",12],variable=score11,value=4,command=total11)
                                            five11=tk.Radiobutton(ui11,text="5",font=["Segoe UI",12],variable=score11,value=5,command=total11)
                                            def soru12():
                                                def total12():
                                                    global score
                                                    total012=score12.get()
                                                    if total012 == 1:
                                                        score +=1
                                                    elif total012 == 2:
                                                        score +=2
                                                    elif total012 == 3:
                                                        score +=3
                                                    elif total012 == 4:
                                                        score += 4
                                                    else:
                                                        score +=5
                                                ui12=tk.Toplevel()
                                                ui12.geometry("500x500+250+100")
                                                headline12=tk.Label(ui12,text="Soru 12: ",font=["Segoe UI",16])
                                                question12=tk.Label(ui12,text="Motivasyonumu devam ettirmekte zorlanmam",font=["Segoe UI",12])
                                                score12=tk.IntVar()
                                                one12=tk.Radiobutton(ui12,text="1",font=["Segoe UI",12],variable=score12,value=1,command=total12)
                                                two12=tk.Radiobutton(ui12,text="2",font=["Segoe UI",12],variable=score12,value=2,command=total12)
                                                three12=tk.Radiobutton(ui12,text="3",font=["Segoe UI",12],variable=score12,value=3,command=total12)
                                                four12=tk.Radiobutton(ui12,text="4",font=["Segoe UI",12],variable=score12,value=4,command=total12)
                                                five12=tk.Radiobutton(ui12,text="5",font=["Segoe UI",12],variable=score12,value=5,command=total12)
                                                def soru13():
                                                    def total13():
                                                        global score
                                                        total013=score13.get()
                                                        if total013 == 1:
                                                            score +=1
                                                        elif total013 == 2:
                                                            score +=2
                                                        elif total013 == 3:
                                                            score +=3
                                                        elif total013 == 4:
                                                            score += 4
                                                        else:
                                                            score +=5
                                                    ui13=tk.Toplevel()
                                                    ui13.geometry("500x500+250+100")
                                                    headline13=tk.Label(ui13,text="Soru 13: ",font=["Segoe UI",16])
                                                    question13=tk.Label(ui13,text="Kişisel donanımlarımın, güçlü yönlerimin \ntam olduğuna inanıyorum.",font=["Segoe UI",12])
                                                    score13=tk.IntVar()
                                                    one13=tk.Radiobutton(ui13,text="1",font=["Segoe UI",12],variable=score13,value=1,command=total13)
                                                    two13=tk.Radiobutton(ui13,text="2",font=["Segoe UI",12],variable=score13,value=2,command=total13)
                                                    three13=tk.Radiobutton(ui13,text="3",font=["Segoe UI",12],variable=score13,value=3,command=total13)
                                                    four13=tk.Radiobutton(ui13,text="4",font=["Segoe UI",12],variable=score13,value=4,command=total13)
                                                    five13=tk.Radiobutton(ui13,text="5",font=["Segoe UI",12],variable=score13,value=5,command=total13)
                                                    def soru14():
                                                        def total14():
                                                            global score
                                                            total014=score14.get()
                                                            if total014 == 1:
                                                                score +=1
                                                            elif total014 == 2:
                                                                score +=2
                                                            elif total014 == 3:
                                                                score +=3
                                                            elif total014 == 4:
                                                                score += 4
                                                            else:
                                                                score +=5
                                                        ui14=tk.Toplevel()
                                                        ui14.geometry("500x500+250+100")
                                                        headline14=tk.Label(ui14,text="Soru 14: ",font=["Segoe UI",16])
                                                        question14=tk.Label(ui14,text="Genel olarak, hayatımdan memnunum.",font=["Segoe UI",12])
                                                        score14=tk.IntVar()
                                                        one14=tk.Radiobutton(ui14,text="1",font=["Segoe UI",12],variable=score14,value=1,command=total14)
                                                        two14=tk.Radiobutton(ui14,text="2",font=["Segoe UI",12],variable=score14,value=2,command=total14)
                                                        three14=tk.Radiobutton(ui14,text="3",font=["Segoe UI",12],variable=score14,value=3,command=total14)
                                                        four14=tk.Radiobutton(ui14,text="4",font=["Segoe UI",12],variable=score14,value=4,command=total14)
                                                        five14=tk.Radiobutton(ui14,text="5",font=["Segoe UI",12],variable=score14,value=5,command=total14)
                                                        def soru15():
                                                            def total15():
                                                                global score
                                                                total015=score15.get()
                                                                if total015 == 1:
                                                                    score +=1
                                                                elif total015 == 2:
                                                                    score +=2
                                                                elif total015 == 3:
                                                                    score +=3
                                                                elif total015 == 4:
                                                                    score += 4
                                                                else:
                                                                    score +=5
                                                            ui15=tk.Toplevel()
                                                            ui15.geometry("500x500+250+100")
                                                            headline15=tk.Label(ui15,text="Soru 15: ",font=["Segoe UI",16])
                                                            question15=tk.Label(ui15,text="Genellikle, hayatımda işlerin yolunda gideceğine inanırım.",font=["Segoe UI",12])
                                                            score15=tk.IntVar()
                                                            one15=tk.Radiobutton(ui15,text="1",font=["Segoe UI",12],variable=score15,value=1,command=total15)
                                                            two15=tk.Radiobutton(ui15,text="2",font=["Segoe UI",12],variable=score15,value=2,command=total15)
                                                            three15=tk.Radiobutton(ui15,text="3",font=["Segoe UI",12],variable=score15,value=3,command=total15)
                                                            four15=tk.Radiobutton(ui15,text="4",font=["Segoe UI",12],variable=score15,value=4,command=total15)
                                                            five15=tk.Radiobutton(ui15,text="5",font=["Segoe UI",12],variable=score15,value=5,command=total15)
                                                            def soru16():
                                                                def total16():
                                                                    global score
                                                                    total016=score16.get()
                                                                    if total016 == 1:
                                                                        score +=1
                                                                    elif total016 == 2:
                                                                        score +=2
                                                                    elif total016 == 3:
                                                                        score +=3
                                                                    elif total016 == 4:
                                                                        score += 4
                                                                    else:
                                                                        score +=5
                                                                ui16=tk.Toplevel()
                                                                ui16.geometry("500x500+250+100")
                                                                headline16=tk.Label(ui16,text="Soru 16: ",font=["Segoe UI",16])
                                                                question16=tk.Label(ui16,text="Genellikle, yeni çevreye uyum sağlama yeteneğim vardır.",font=["Segoe UI",12])
                                                                score16=tk.IntVar()
                                                                one16=tk.Radiobutton(ui16,text="1",font=["Segoe UI",12],variable=score16,value=1,command=total16)
                                                                two16=tk.Radiobutton(ui16,text="2",font=["Segoe UI",12],variable=score16,value=2,command=total16)
                                                                three16=tk.Radiobutton(ui16,text="3",font=["Segoe UI",12],variable=score16,value=3,command=total16)
                                                                four16=tk.Radiobutton(ui16,text="4",font=["Segoe UI",12],variable=score16,value=4,command=total16)
                                                                five16=tk.Radiobutton(ui16,text="5",font=["Segoe UI",12],variable=score16,value=5,command=total16)
                                                                def soru17():
                                                                    def total17():
                                                                        global score
                                                                        total017=score17.get()
                                                                        if total017 == 1:
                                                                            score +=1
                                                                        elif total017 == 2:
                                                                            score +=2
                                                                        elif total017 == 3:
                                                                            score +=3
                                                                        elif total017 == 4:
                                                                            score += 4
                                                                        else:
                                                                            score +=5
                                                                    ui17=tk.Toplevel()
                                                                    ui17.geometry("500x500+250+100")
                                                                    headline17=tk.Label(ui17,text="Soru 17: ",font=["Segoe UI",16])
                                                                    question17=tk.Label(ui17,text="Bana çok yakın olan kişilerle , aramda bağ \noluşturmak benim için kolaydır",font=["Segoe UI",12])
                                                                    score17=tk.IntVar()
                                                                    one17=tk.Radiobutton(ui17,text="1",font=["Segoe UI",12],variable=score17,value=1,command=total17)
                                                                    two17=tk.Radiobutton(ui17,text="2",font=["Segoe UI",12],variable=score17,value=2,command=total17)
                                                                    three17=tk.Radiobutton(ui17,text="3",font=["Segoe UI",12],variable=score17,value=3,command=total17)
                                                                    four17=tk.Radiobutton(ui17,text="4",font=["Segoe UI",12],variable=score17,value=4,command=total17)
                                                                    five17=tk.Radiobutton(ui17,text="5",font=["Segoe UI",12],variable=score17,value=5,command=total17)
                                                                    def soru18():
                                                                        def total18():
                                                                            global score
                                                                            total018=score18.get()
                                                                            if total018 == 1:
                                                                                score +=1
                                                                            elif total018 == 2:
                                                                                score +=2
                                                                            elif total018 == 3:
                                                                                score +=3
                                                                            elif total018 == 4:
                                                                                score += 4
                                                                            else:
                                                                                score +=5
                                                                        ui18=tk.Toplevel()
                                                                        ui18.geometry("500x500+250+100")
                                                                        headline18=tk.Label(ui18,text="Soru 18: ",font=["Segoe UI",16])
                                                                        question18=tk.Label(ui18,text="Sıklıkla duraksar ve hissettiklerimi düşünürüm.",font=["Segoe UI",12])
                                                                        score18=tk.IntVar()
                                                                        one18=tk.Radiobutton(ui18,text="1",font=["Segoe UI",12],variable=score18,value=1,command=total18)
                                                                        two18=tk.Radiobutton(ui18,text="2",font=["Segoe UI",12],variable=score18,value=2,command=total18)
                                                                        three18=tk.Radiobutton(ui18,text="3",font=["Segoe UI",12],variable=score18,value=3,command=total18)
                                                                        four18=tk.Radiobutton(ui18,text="4",font=["Segoe UI",12],variable=score18,value=4,command=total18)
                                                                        five18=tk.Radiobutton(ui18,text="5",font=["Segoe UI",12],variable=score18,value=5,command=total18)
                                                                        def soru19():
                                                                            def total19():
                                                                                global score
                                                                                total019=score19.get()
                                                                                if total019 == 1:
                                                                                    score +=1
                                                                                elif total019 == 2:
                                                                                    score +=2
                                                                                elif total019 == 3:
                                                                                    score +=3
                                                                                elif total019 == 4:
                                                                                    score += 4
                                                                                else:
                                                                                    score +=5
                                                                            ui19=tk.Toplevel()
                                                                            ui19.geometry("500x500+250+100")
                                                                            headline19=tk.Label(ui19,text="Soru 19: ",font=["Segoe UI",16])
                                                                            question19=tk.Label(ui19,text="Duygularımı düzenlemekte ve ifade genellikle zorlanmam",font=["Segoe UI",12])
                                                                            score19=tk.IntVar()
                                                                            one19=tk.Radiobutton(ui19,text="1",font=["Segoe UI",12],variable=score19,value=1,command=total19)
                                                                            two19=tk.Radiobutton(ui19,text="2",font=["Segoe UI",12],variable=score19,value=2,command=total19)
                                                                            three19=tk.Radiobutton(ui19,text="3",font=["Segoe UI",12],variable=score19,value=3,command=total19)
                                                                            four19=tk.Radiobutton(ui19,text="4",font=["Segoe UI",12],variable=score19,value=4,command=total19)
                                                                            five19=tk.Radiobutton(ui19,text="5",font=["Segoe UI",12],variable=score19,value=5,command=total19)
                                                                            def last():
                                                                                ui20=tk.Toplevel()
                                                                                ui20.geometry("500x500+250+100")
                                                                                headline20=tk.Label(ui20,text="Tebrikler Testi Tamamladınız",font=["Segoe UI",16])
                                                                                headline20.place(x=45,y=120)
                                                                                content_last=tk.Label(ui20,text="Test Sonucunuz:",font=["Segoe UI",14])
                                                                                content_last.place(x=20,y=150)
                                                                                content_score=tk.Label(ui20,text=str(score),font=["Segoe UI",14])
                                                                                content_score.place(x=200,y=150)
                                                                                
                                                                                result_print=tk.Label(ui20,text="Skorunuz 100 ile 60 arasında ise; \nYüksek Bir Duygusal Zekaya Sahipsiniz.\nSkorunuz 60 ile 30 arasında ise; \nOrtalama Bir Duygusal Zekaya Sahipsiniz. \nSkorunuz 30 altında ise; \nDüşük Duygusal Zekaya Sahipsiniz.",font=["Segoe UI",14],fg="red")
                                                                                result_print.place(x=20,y=250)
                                                                                ui19.withdraw()

                                                                            btn_next19=tk.Button(ui19,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=last)
                                                                            headline19.place(x=5,y=5)
                                                                            question19.place(x=5,y=50)
                                                                            one19.place(x=5,y=80)
                                                                            two19.place(x=5,y=120)
                                                                            three19.place(x=5,y=160)
                                                                            four19.place(x=5,y=200)
                                                                            five19.place(x=5,y=240)
                                                                            btn_next19.place(x=300,y=350)
                                                                            ui18.withdraw()

                                                                        btn_next18=tk.Button(ui18,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru19)
                                                                        headline18.place(x=5,y=5)
                                                                        question18.place(x=5,y=50)
                                                                        one18.place(x=5,y=80)
                                                                        two18.place(x=5,y=120)
                                                                        three18.place(x=5,y=160)
                                                                        four18.place(x=5,y=200)
                                                                        five18.place(x=5,y=240)
                                                                        btn_next18.place(x=300,y=350)
                                                                        ui17.withdraw()

                                                                    btn_next17=tk.Button(ui17,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru18)
                                                                    headline17.place(x=5,y=5)
                                                                    question17.place(x=5,y=50)
                                                                    one17.place(x=5,y=90)
                                                                    two17.place(x=5,y=130)
                                                                    three17.place(x=5,y=170)
                                                                    four17.place(x=5,y=210)
                                                                    five17.place(x=5,y=250)
                                                                    btn_next17.place(x=300,y=350)
                                                                    ui16.withdraw()

                                                                btn_next16=tk.Button(ui16,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru17)
                                                                headline16.place(x=5,y=5)
                                                                question16.place(x=5,y=50)
                                                                one16.place(x=5,y=80)
                                                                two16.place(x=5,y=120)
                                                                three16.place(x=5,y=160)
                                                                four16.place(x=5,y=200)
                                                                five16.place(x=5,y=240)
                                                                btn_next16.place(x=300,y=350)
                                                                ui15.withdraw()

                                                            btn_next15=tk.Button(ui15,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru16)
                                                            headline15.place(x=5,y=5)
                                                            question15.place(x=5,y=50)
                                                            one15.place(x=5,y=80)
                                                            two15.place(x=5,y=120)
                                                            three15.place(x=5,y=160)
                                                            four15.place(x=5,y=200)
                                                            five15.place(x=5,y=240)
                                                            btn_next15.place(x=300,y=350)
                                                            ui14.withdraw()

                                                        btn_next14=tk.Button(ui14,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru15)
                                                        headline14.place(x=5,y=5)
                                                        question14.place(x=5,y=50)
                                                        one14.place(x=5,y=80)
                                                        two14.place(x=5,y=120)
                                                        three14.place(x=5,y=160)
                                                        four14.place(x=5,y=200)
                                                        five14.place(x=5,y=240)
                                                        btn_next14.place(x=300,y=350)
                                                        ui13.withdraw()

                                                    btn_next13=tk.Button(ui13,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru14)
                                                    headline13.place(x=5,y=5)
                                                    question13.place(x=5,y=50)
                                                    one13.place(x=5,y=90)
                                                    two13.place(x=5,y=130)
                                                    three13.place(x=5,y=170)
                                                    four13.place(x=5,y=210)
                                                    five13.place(x=5,y=250)
                                                    btn_next13.place(x=300,y=350)
                                                    ui12.withdraw() 

                                                btn_next12=tk.Button(ui12,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru13)
                                                headline12.place(x=5,y=5)
                                                question12.place(x=5,y=50)
                                                one12.place(x=5,y=80)
                                                two12.place(x=5,y=120)
                                                three12.place(x=5,y=160)
                                                four12.place(x=5,y=200)
                                                five12.place(x=5,y=240)
                                                btn_next12.place(x=300,y=350)
                                                ui11.withdraw()

                                            btn_next11=tk.Button(ui11,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru12)
                                            headline11.place(x=5,y=5)
                                            question11.place(x=5,y=50)
                                            one11.place(x=5,y=80)
                                            two11.place(x=5,y=120)
                                            three11.place(x=5,y=160)
                                            four11.place(x=5,y=200)
                                            five11.place(x=5,y=240)
                                            btn_next11.place(x=300,y=350)
                                            ui10.withdraw()

                                        btn_next10=tk.Button(ui10,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru11)
                                        headline10.place(x=5,y=5)
                                        question10.place(x=5,y=50)
                                        one10.place(x=5,y=80)
                                        two10.place(x=5,y=120)
                                        three10.place(x=5,y=160)
                                        four10.place(x=5,y=200)
                                        five10.place(x=5,y=240)
                                        btn_next10.place(x=300,y=350)
                                        ui9.withdraw()

                                    btn_next9=tk.Button(ui9,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru10)
                                    headline9.place(x=5,y=5)
                                    question9.place(x=5,y=50)
                                    one9.place(x=5,y=90)
                                    two9.place(x=5,y=130)
                                    three9.place(x=5,y=170)
                                    four9.place(x=5,y=210)
                                    five9.place(x=5,y=250)
                                    btn_next9.place(x=300,y=350)
                                    ui8.withdraw()

                                btn_next8=tk.Button(ui8,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru9)
                                headline8.place(x=5,y=5)
                                question8.place(x=5,y=50)
                                one8.place(x=5,y=90)
                                two8.place(x=5,y=130)
                                three8.place(x=5,y=170)
                                four8.place(x=5,y=210)
                                five8.place(x=5,y=250)
                                btn_next8.place(x=300,y=350)
                                ui7.withdraw()

                            btn_next7=tk.Button(ui7,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru8)
                            headline7.place(x=5,y=5)
                            question7.place(x=5,y=50)
                            one7.place(x=5,y=80)
                            two7.place(x=5,y=120)
                            three7.place(x=5,y=160)
                            four7.place(x=5,y=200)
                            five7.place(x=5,y=240)
                            btn_next7.place(x=300,y=350)
                            ui6.withdraw()
                             
                        btn_next6=tk.Button(ui6,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru7)
                        headline6.place(x=5,y=5)
                        question6.place(x=5,y=50)
                        one6.place(x=5,y=80)
                        two6.place(x=5,y=120)
                        three6.place(x=5,y=160)
                        four6.place(x=5,y=200)
                        five6.place(x=5,y=240)
                        btn_next6.place(x=300,y=350)
                        ui5.withdraw()

                    btn_next5=tk.Button(ui5,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru6)
                    headline5.place(x=5,y=5)
                    question5.place(x=5,y=50)
                    one5.place(x=5,y=80)
                    two5.place(x=5,y=120)
                    three5.place(x=5,y=160)
                    four5.place(x=5,y=200)
                    five5.place(x=5,y=240)
                    btn_next5.place(x=300,y=350)
                    ui4.withdraw()

                btn_next4=tk.Button(ui4,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru5)
                headline4.place(x=5,y=5)
                question4.place(x=5,y=50)
                one4.place(x=5,y=80)
                two4.place(x=5,y=120)
                three4.place(x=5,y=160)
                four4.place(x=5,y=200)
                five4.place(x=5,y=240)
                btn_next4.place(x=300,y=350)
                ui3.withdraw()

            btn_next3=tk.Button(ui3,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru4)
            headline3.place(x=5,y=5)
            question3.place(x=5,y=50)
            one3.place(x=5,y=80)
            two3.place(x=5,y=120)
            three3.place(x=5,y=160)
            four3.place(x=5,y=200)
            five3.place(x=5,y=240)
            btn_next3.place(x=300,y=350)
            ui2.withdraw()

        btn_next2=tk.Button(ui2,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru3)
        headline2.place(x=5,y=5)
        question2.place(x=5,y=50)
        one2.place(x=5,y=80)
        two2.place(x=5,y=120)
        three2.place(x=5,y=160)
        four2.place(x=5,y=200)
        five2.place(x=5,y=240)
        btn_next2.place(x=300,y=350)
        ui1.withdraw()

    btn_next1=tk.Button(ui1,text="İlerle",bg="green",fg="white",font=["Segoe UI",14],command=soru2)
    headline1.place(x=5,y=5)
    question1.place(x=5,y=50)
    one1.place(x=5,y=80)
    two1.place(x=5,y=120)
    three1.place(x=5,y=160)
    four1.place(x=5,y=200)
    five1.place(x=5,y=240)
    btn_next1.place(x=300,y=350)
    MainWindow.withdraw()

start=tk.Button(MainWindow,text="BAŞLA",font=["Segoe UI",14],bg="green",fg="white",command=soru1)
start.place(x=200,y=350)
MainWindow.mainloop()