try:
    size=int(input("Enter the size:"))
    user_list=[]
    for i in range(size):
        val=int(input(f"Enter element{i+1}::"))
        user_list.append(val)
    index=int(input("Enter index to access element:"))
    print("Element index at",index,"is:-----",user_list[index])
except ValueError:
    print("Error:please enter only integers")
except IndexError:
    print("Error:  index--out--of--range")