def copy_alternate_lines(file1,file2):
    f1=open(file1,"r")
    f2=open(file2,"w")


    line_number=1
    for line in f1:
        if line_number %2!=0:
            f2.write(line)
        line_number+=1

        
    f1.close()
    f2.close()
    print("Odd-numbered lines have been copid successfully.")
copy_alternate_lines('file1.txt','file2.txt')
