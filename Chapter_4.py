#how many books are in the Harry Potter Series

num_correct = 0
total_q = 0
book_ans = int(input("How many books are there in the Harry Potter series? "))
if book_ans == 7:
    print("Correct!")
    num_correct += 1
    total_q += 1
else:
    print("Incorrect!")
    total_q += 1
    

#Math problem

math_ans = int(input("What is 3*(2-1)? "))
if math_ans == 3:
    print("Correct!")
    num_correct +=1
    total_q += 1
else:
    print("Incorrect!")
    total_q += 1
    
singer_ans = int(input("""Who sings Black Horse and the Cheery Tree?
1.Kelly Clarkson
2.K.T. tunstall
3.Hillary Duff
4.Bon Jovi
? """ ))

if singer_ans ==2:
    print("Correct!")
    num_correct +=1
    total_q += 1
else:
    print("Incorrect!")
    total_q += 1
    

dollar_answer = int(input("""Who is on the front of a one dollar bill?
1.George Washington
2.Abraham Lincoln
3.John Adams
4.Thomas Jefferson
? """ ))

if dollar_answer == 1:
    print("Yes")
    num_correct +=1
    total_q += 1
else:
    print("No")
    total_q += 1
    
print("Congradulations, you got %d answers right.\n That is a score of %0.1f percent." % (num_correct ,(num_correct/total_q)*100))


