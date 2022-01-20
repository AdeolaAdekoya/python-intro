print("welcome to python")


# chcking types
print(type("5"))
print( type(5))
print( type(5.0))


# changing types

print(type( int ("5")))

# you can chang from intiger, intiger to string
# string to float to string
#  intiger - float and intiger
# float- intiger- float
# clause- the value has to be a number to change 


print(type(9))
print(type("82"))
print(type(3.9))


print(type(str(9)))
print(type(int("9")))
print(type(float(9)))

a = "hii"

print(a)



easypace = ((8 * 60) + 15) * 2
tempopace = ((7 * 60) + 12) * 3

my_runtime = easypace + tempopace
print(my_runtime)

my_answer = my_runtime / 3600
start = 6 + (52/60)
print (my_answer + start)



volume= (4/3)*3.14*(5**3)
print(volume)


price_for_60 = (24.95 * 60 ) * 0.6
shipping = 3 + (0.75*59)

print(price_for_60+shipping)

area= 20
cost_of_carpet = 24.99
cost_of_cushioning_pad = 2.99
cost_of_labour = 18


total_cost = (cost_of_carpet * 20) + (cost_of_cushioning_pad * 20) + (cost_of_labour * 20) + (35)


print(total_cost)


# print("class two")

# print("3" + "3")

# my_string = "i am a boy"

# print(my_string [3])
# print(my_string [3:])
# print(my_string [:5])
# print(my_string [-9:-5: 2])

# our_string = "This is 1000 naira"
# st2 = "This 500 is lovely"

# print( our_string [8:12])
# print(st2 [5:8])


# string2 =  our_string [8:12]
# string4 =  st2 [5:8]

# # print(int(string2) + int(string4) )
# added = int(string2) + int(string4) 

# # or
# print(eval(string2) + eval(string4))


#  f string 

# print(f"The sum of  {string2} and {string4} is {added}")


# another way to format a string is 


# print(f"The sum of %s and %s is %d" % (string2, string4, added))


print("this is ayo's book")
print('this is ayo\'s book')


print("dear, buhari.\nplease don'f run for president again.\n\tYours in the Country.\n\t,Astroverse Team. ")

#  this is called documentation

print(""" This is a wonderful string



                Yours in County.
                The Astroverse team. """)


a = "aaboy"



print(a.index("a"))

print(a.rindex("a"))
print(a.find("a"))
print(a.count("a"))
print(a.replace("a", "w"))

# lists


sen = "ada is a girl and tunde loves ice cream but, ada does not give him"
print(sen.split(','))

my_sentence = " a quick brown fox jumos over a lazy dog"

a = my_sentence.split()

print(a)


name = "tunde.pdf"

print(name.split('.')[-1])


num = ['0','4','3','2']

otp = "".join(num)

print(otp)


s1 = "Ault"
s2 = " Kelly"


print("original strings are", s1, s2)

# middle index number of s1
mi = len(s1) // 2

#  get character from 0 to the middle index number from s1

x = s1[:mi]  + s2 + s1[mi:]

print(x)



# sum2 =  
# print(sum2)

my_sentence = " a quick brown fox jumos over a lazy dog"

a = my_sentence.split()

print(a)


str1 = "welcome to USA. usa awesome, isin't it ?"

a =  str1.lower()


print(a.count("usa"))



srt2 = "Emma is a data scientist who knows python. Emma works at google"


print(srt2.rfind("Emma"))



srt3 = "Emma is a data scientist"

print(srt3.replace(" ", "-"))



srt4 = "Emma-is-a-data-scientist"

print(srt4.replace("_", " "))


# using split 

# print(" ".join(str1.split('-')))



# srt5 = "/*Jon is @developer & musician"

# final_answer  = srt5.replace("/", "").replace("*", "").replace("@", "").replace("& ", "")

# print(final_answer)


# concat lists


my_list = ["i", "am", "good"]

a_list = ["she", "is", "a", "queen" ]

print(my_list + a_list)


new_list = ["i","am","good","she"," is","a","queen"]

print(new_list [0: : 2])

# or [::2]



#  given the list below 

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

print(list1[2][2][0] + list1[2][3])








