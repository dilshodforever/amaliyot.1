# class address:
#     def __init__(self, street,city,country):
#         self.street=street
#         self.city=city
#         self.country=country

#     def info(self):
#         add=address
#         add.street=input("kocha nomi: ")
#         add.city=input("shaxar nomi: ")
#         add.country=input("davlat nomi: ")
#         print(f"Street:{add.street}\nCity: {add.city}\nCountry {add.country}")
    
# class address:
#    def __init__(self, ism, yosh, email, number):
#         self.ism=ism
#         self.yoshtek(yosh)
#         self.emailtek(email)
#         self.raqam(number)
#    def yoshtek(self,yosh):
#        if 0>yosh:
#             raise ValueError("yosh hato: ")
#        self.yosh=yosh
#        return self.yosh
#    def emailtek(self,email):
#        try:
#             if  email.endswith("@gmail.com"):
#                 self.email=email
#                 return self.email
#        except:
#                      print("email hato kirittingiz: ")
#    def raqam(self,number):
#        if number[0]=='+':
#            self.number=number
#            return self.number
#    def __str__(self):
#        return f"ism: {self.ism}, yosh:{self.yosh},email:{self.email},number:{self.number}"
    
# arr=address(input("ismini kiriting: "), int(input("yoshini kiriting: ")), input("emailni kiriting: "),input("nomerni kiriting: "))
# print(arr)




# class person(address):
#     def __init__(self, ism, yosh, email, number):
#         super().__init__(ism, yosh, email, number)
#     def __str__(self):
#        return f"ism: {self.ism}, yosh:{self.yosh+5},email:{self.email},number:{self.number}"
# num=person(input("ismini kiriting: "), int(input("yoshini kiriting: ")), input("emailni kiriting: "),input("nomerni kiriting: "))
# print(num)
    
    
#                                                     #1-masala
# class talaba:
#     def __init__(self,ism, familiya,yil):
#         self.ism=ism
#         self.familiya=familiya
#         self.yil=yil
#     def __str__(self):
#         return f"ismi:{self.ism}\nfamiliya:{self.familiya}\nyili:{self.yil}"
# arr=talaba(input("ism kiriting: "), input("familya kiriting: "), input("yili: "))
# print(arr)


                                                    #3-masala
                                                    
                              #1-masala
class talaba:
    def __init__(self,ism, familiya,yil):
        self.ism=ism
        self.familiya=familiya
        self.yil=yil
    def ism(self):
        return self.ism
    def __str__(self):
        return f"ismi:{self.ism}\nfamiliya:{self.familiya}\nyili:{self.yil}"
arr=talaba(input("ism kiriting: "), input("familya kiriting: "), input("yili: "))




