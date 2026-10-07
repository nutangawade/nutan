string=input("Enter your String")
print("\n----String operation Menu---")
print("1.Find the frequency of a character")
print("2.Replace a character by another character ")
print("3.Remove the first occurence of a character")
print("4.Remove all occurences of a string")
print("5.Exit")

while True:
          choice=int(input("\nEnter Your choice(1-5):"))

          if choice==1:
                   
               ch=input("Enter character to find frequency :")
               freq=string.count(ch)
               print(f"The Frequency of'{ch}'in'{string}'is:{freq}")
          
          elif choice==2:
                   
               old=input("Enter character to be replace :")
               new=input("Enter the new character:")
               new_string=string.replace(old,new)
               print("Updated string:",new_string)

          elif choice==3:
               
               ch=input("Enter the character to remove (first occurrence):")
               pos=string.find(ch)
               
               if pos!=-1:
                   
                    string=string[:pos]+string[pos+1:]
                    print("Updated String:",string)
                   
               else:
                    print("Character not found in string.")
                       
          elif choice==4:
                       
               ch=input("Enter the characters to remove (all occurrences):")
               string=string.replace(ch," ")
               print("Updated string:",string)
                              
          elif choice==5:
                        
               print("Exiting program.Goodbye!")
               break
                    
          else:
               print("Invalid choice! Please enter number between 1 to 5.")
