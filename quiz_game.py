import mysql.connector

mydb = mysql.connector.connect(host = "127.0.0.1",user="arun",password="karthi@123",auth_plugin ="mysql_native_password",port="3306",database="newdb")

mycursor = mydb.cursor()
mycursor.execute("select * from quiz_questions")

playing = input("Do you want to play? ")
if playing.lower() != 'yes':
    quit()
print("Okay! Lets's play :)")

crt_point,total_point = 0,0

for i in mycursor:

    answer = input(i[1])
    total_point += 1
    if answer.lower() == i[2]:
        print('correct!')
        crt_point += 1
    else:
        print('Incorrect')
print("You got "+str(crt_point)+' out of '+str(total_point)+" questions correct!")
print("percentage " + str(round((crt_point/total_point)*100))+ "%")

ques_ans=input("Did you want to see answers? (yes/no)")

if ques_ans.lower()=="yes":
    mycursor.execute("select * from quiz_questions")
    for i in mycursor:
        print(str(i[0])+" . "+str(i[1])+"  Ans : "+str(i[2]))
else:
    print('thankyou')
