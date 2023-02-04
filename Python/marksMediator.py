total=30
obtained=25

#Initializations
diff=total-obtained
temp=total
unanswered=0
mistake=0
for i in range(total+1,obtained,-1):
    temp-=1
    unanswered=total-temp
    if(temp==obtained):
        unanswered=temp
        break

print("Questions Unanswered =",unanswered)