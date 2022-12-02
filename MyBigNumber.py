def MyBigNumber(stn1 : str ,stn2 : str) : 
    len1 = len(stn1)
    len2= len(stn2)
    
    #visualize phep tinh
    maxLen= max(len1,len2)
    print("Ta có thể hình dung phép tính như sau : ")
    visual="""
            %s
        +
            %s
           ----
        =  ?
            """%("0"*(maxLen-len1)+stn1,"0"*(maxLen-len2)+stn2)
    print(visual)
    
    Check = False
    result = ""
    
    # giải 
    print("Bài làm :\n")
    for i in range(maxLen): 
        print("Bước %d: "%(i+1))
        
        int1=0 if len1 - i-1 <0 else int(stn1[len1 - i-1])
        int2=0 if len2 - i-1 <0 else int(stn2[len2 - i-1])
        temp = int1 + int2 if Check == False else int1 + int2 + 1

        if Check:
            if temp >=10:
                print("Lấy %d cộng với %d được %d. Cộng tiếp với nhớ 1 được %d.Lưu %d vào kết quả và nhớ 1."%(int1,int2,temp-1,temp,temp%10))  
            else:
                print("Lấy %d cộng với %d được %d. Cộng tiếp với nhớ 1 được %d"%(int1,int2,temp-1,temp))  
        else : 
            if temp >=10:
                print("Lấy %d cộng với %d được %d.Lưu %d vào kết quả và nhớ 1."%(int1,int2,temp,temp%10))  
            else:
                print("Lấy %d cộng với %d được %d.Lưu %d vào kết quả."%(int1,int2,temp,temp))  
                
        Check = True if temp >=10 else False 
        result =str(temp) + result if Check and i == maxLen -1 else str(temp%10) + result    

        
    print("Kết quả của phép tính là : %s\n\n"%result)
    return int(result)
        

# print(MyBigNumber("117","26"),117+26)
# print(MyBigNumber("1171","226"),1171+226)
# print(MyBigNumber("11721","226"),11721+226)
# print(MyBigNumber("117","2626277"),117+2626277)
# print(MyBigNumber("1171","227776"),1171+227776)
#print(MyBigNumber("999999","2269898"),999999+2269898,sep="\n")
#print(MyBigNumber("0","0"),0+0,sep="\n")
#   999999
#  2269898
#print(MyBigNumber("999999999","99999999",),999999999+99999999,sep="\n")
# print(MyBigNumber("99999999","999999999"),99999999+999999999,sep="\n")
# print(MyBigNumber("99999999","1999999999"),99999999+1999999999,sep="\n")
# print(MyBigNumber("0","1999999999"),0+1999999999,sep="\n")