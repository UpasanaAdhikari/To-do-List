from Funtion import addlist,mark_as_completed,delete_list,viewlist
def main():
    try: 
        while True:

            print('-'* 50)  
            print("Welcome to do list")
            print('-'* 50)  
            print("Choose options below : ")
            print("1> View List \n2> Delete List \n3> Add List \n4>Mark as Completed \n5>Exit")
            choice = int(input("Enter Choice "))
            if choice  == 1:
                viewlist()
            elif choice  ==2:
                delete_list()
            elif choice  ==3:
                addlist()
            elif choice  == 4:
                mark_as_completed()
            elif choice == 5:
                break
            else:
                print("Choose valid value")
    except:
        print("exception error")       
if __name__ == "__main__":
    main()

