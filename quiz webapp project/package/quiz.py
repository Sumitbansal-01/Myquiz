class quiz:
    '''The class is for creating quizzes in MCQ'''
    superuser=[]
    quizfile=[]
    topics=[]
    difficulty_lvl=["Easy","Intermediate","Advance"]
    
    def __init__(self):
        self.created_file=[]
        while True:
            x=input('\nIf you are a super user press 1\nIf you are a user press 2\nIf you want to exit press 9\n')
            if x=='1':
                self.super_user()
            elif x=='2':
                self.user()
            elif x=='9':
                break
            else:
                print('Invalid Input')
                
    def super_user(self):
        while True:
            a=input("\nFor creating new account press '1'\nFor login press '2'\nFor exit press 9\n")
            if a=="1" :
                self.creating_account()
            elif a=='2':
                self.login()
            elif a=='9':
                break
            else:
                print('Invalid Input')
                
    def creating_account(self):
        self.name=input("\nName: ")
        a=self.name
        self.phonenumber=input("Phone number: ")
        b=self.phonenumber
        password=input("Password: ")
        while True:
            d=input("Confirm your password: ")
            if password==d:
                c=d
                self.password=c
                break
            else:
                print("Password didn't match")
        print("Your account is created successfully\n")
        e=a+b+c
        if e not in quiz.superuser:
            quiz.superuser.append(e)
            self.menu1()
        else:
            print('Your account is already present please try to LOGIN')
            
    def login(self):
        a=input("\nName: ")
        b=input("Password: ")
        c=input('Phone Number: ')
        d=a+c+b
        for obj in quiz.superuser:
            if d==obj:
                print("You have login successfully")
                self.name=a
                self.password=b
                self.phonenumber=c
                self.menu1()
                break
        else:
            print("Your account didn't found either name or password didn't match")
            
    def menu1(self):
        while True:
            y=input('\nFor creating quiz press 1\nFor editing any of your quiz press 2\nFor exit press 9\n')
            if y=='1':
                self.create_quiz()
            elif y=='2':
                self.edit()
            elif y=='9':
                break
            else:
                print('Invalid Input')
                
    def create_quiz(self):
        t=input("\nEnter the topic: ")
        while True:
            d=input("\nEnter the difficulty level\nPress 1 for Easy\nPress 2 for Intermediate\nPress 3 for Advance\n")
            if d=="1" :
                a="Easy"
                break
            elif d=='2' :
                a="Intermediate"
                break
            elif d=='3' :
                a="Advance"
                break
            else :
                print("Please enter the correct key")
        f=t+" "+a
        self.created_file.append(f)
        file_name=self.name+self.phonenumber+self.password+f
        quiz.quizfile.append(file_name)
        quiz.topics.append(t)
        fp=open(file_name,"w")
        while True:
            n=input("\nEnter the number of questions: ")
            if n.isdigit():
                n=int(n)
                break
        for i in range(1,n+1):
            print('\n')
            fp.write(f'Q)-\t{input("Enter the question?: ")}\n')
            fp.write(input("Enter the first option: ")+"\n")
            fp.write(input("Enter the second option: ")+"\n")
            fp.write(input("Enter the third option: ")+"\n")
            fp.write(input("Enter the fourth option: ")+"\n")
            while True:
                answer=input("Enter the correct option number: ")
                if answer.isdigit():
                    break
                else:
                    print('Invalid Input')
            fp.write(f"{answer}\n")
        fp.close()
        
    def edit(self):
        print('Name of the quizes are:-\n')
        for j in self.created_file:
            print(j)
        file_name=input("\nEnter your quiz name from the above want to be edit: ")
        real_file_name=self.name+self.phonenumber+self.password+file_name
        if real_file_name in quiz.quizfile:
            fp=open(real_file_name,'a')
            while True:
                n=input("\nEnter the number of questions to be added: ")
                if n.isdigit():
                    n=int(n)
                    break
            for i in range(1,n+1):
                print('\n')
                fp.write(f'Q)-\t{input("Enter the question?: ")}\n')
                fp.write(input("Enter the first option: ")+"\n")
                fp.write(input("Enter the second option: ")+"\n")
                fp.write(input("Enter the third option: ")+"\n")
                fp.write(input("Enter the fourth option: ")+"\n")
                while True:
                    answer=input("Enter the correct option number: ")
                    if answer.isdigit():
                        break
                    else:
                        print('Invalid Input')
                fp.write(f"{answer}\n")
            fp.close()
        else:
            print("You enter the wrong name or this quiz is not your")
            
    def user(self):
        self.name=input("Enter your name: ")
        self.email=input("Enter your email: ")
        while True:
            c=input('\nFor quiz press 1\nFor exit press 9\n')
            if c=='1':
                self.start_quiz()
            elif c=='9':
                break
            else:
                print('Enter wrong key')
                
    def start_quiz(self):
        print("Choose the topic name from below by typing their name")
        for i in quiz.topics:
            print(i)
        a=input("\nEnter the topic name here: ")
        if a in quiz.topics:
            self.topic=a
            print("\nSelect the difficulty level")
            for j in quiz.difficulty_lvl:
                print(j)
            b=input("\nEnter the difficulty level here: ")
            if b in quiz.difficulty_lvl:
                self.lvl=b
                c=a+' '+b
                for k in quiz.quizfile:
                        if c in k:
                            fp=open(k)
                            self.score=0
                            r=fp.readlines()
                            print("\nName:- ",self.name)
                            print("Email:- ",self.email)
                            print(a,b)
                            self.q_num=0
                            self.q=[]
                            self.ans=[]
                            for l in range(0,len(r),6):
                                self.q_num+=1
                                q1=r[l].strip("\n")
                                self.q.append(q1)
                                print('\n',q1)
                                for x in range(1,5):
                                    m=r[l+x].strip("\n")
                                    print(x,"\t",m)
                                print("Score:- ",self.score)
                                ans=r[l+5].strip("\n")
                                self.ans.append(ans)
                                u_ans=input("Enter the correct option number: ")
                                if ans==u_ans:
                                    print("Your answer is correct")
                                    self.score+=1
                                else:
                                    print("Your answer is wrong")
                            fp.close()
                            self.display_report()
            else:
                print("Invalid input")
        else:
            print("Invalid input")
            
    def display_report(self):
        print('\n\n\nQUIZ REPORT')
        print("Name:- ",self.name)
        print("Email:- ",self.email)
        print("Topic:- ",self.topic)
        print("Level:- ",self.lvl)
        print("\n\n\nScore:- ",self.score)
        print("Total Marks:- ",self.q_num)
        print("Percentage:-",round((self.score/self.q_num)*100,2))
        print("\n\n\n")
        for i in range(len(self.q)):
            print(self.q[i])
            print("Ans:-",self.ans[i])
