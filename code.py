from tabulate import tabulate
import mysql.connector as a
con = a.connect(host = 'localhost', user = 'root', password = 'mysql', database = 'library')

def addbook():
    bcode = int(input("Enter book code: "))
    bname = input("Enter book name: ")
    aname = input("Enter author name: ")
    btotal = int(input("Enter total number of books: "))
    my = con.cursor()
    sql = 'insert into books values(%s, %s, %s, %s)'
    data = (bcode, bname, aname, btotal)
    my.execute(sql, data)
    c = con.commit()
    print("Book added successfully!")
    print('\n')
    
def issuebook():
    name = input("Enter the name: ")
    regno = int(input("Enter registration number: "))
    bcode = int(input("Enter book code: "))
    issue_date = int(input("Enter the issue date without any space, slash, hyphen(yyyymmdd): "))
    my = con.cursor()
    data = (name, regno, bcode, issue_date)
    sql = 'insert into issue values(%s, %s, %s, %s)'
    my.execute(sql, data)
    my = con.commit()
    print("Book issued successfully to {}!".format(name))
    print('\n')
    
def returnbook():
    name = input("Enter the name: ")
    regno = int(input("Enter registration number: "))
    bcode = int(input("Enter book code: "))
    return_date = int(input("Enter the return date without any space, slash, hyphen(yyyymmdd): "))
    my = con.cursor()
    data = (name, regno, bcode, return_date)
    sql = 'insert into return_book values(%s, %s, %s, %s)'
    my.execute(sql, data)
    my = con.commit()
    print("Book returned successfully by {}!".format(name))
    print('\n')
    
def deletebook():
    bcode = int(input("enter book code to delete: "))
    my = con.cursor()
    data = (bcode,)
    sql = 'delete from books where Book_code = %s'
    my.execute(sql, data)
    my = con.commit()
    print("Book deleted successfully!")
    print('\n')

def deleteissuedbook():
    rgno = int(input("enter registration number to delete: "))
    my = con.cursor()
    data = (rgno,)
    sql = 'delete from issue where RegNo = %s'
    my.execute(sql, data)
    my = con.commit()
    print("Issued Book deleted successfully!")
    print('\n')

def deletereturnedbook():
    rgno = int(input("enter registration number to delete: "))
    my = con.cursor()
    data = (rgno,)
    sql = 'delete from return_book where RegNo = %s'
    my.execute(sql, data)
    my = con.commit()
    print("Returned Book deleted successfully!")
    print('\n')
    
def displaybook():
    my = con.cursor()
    sql = 'select * from books;'
    my.execute(sql)
    m = my.fetchall()
    headers = ['Book Code', 'Book name', 'Author name', 'Total books']
    tablefmt = "double_outline"
    print(tabulate(m, headers, tablefmt))
    my = con.commit()
    print('\n')
    
def displayissuedbooks():
    my = con.cursor()
    sql = 'select * from issue'
    my.execute(sql)
    m = my.fetchall()
    headers = ['Name', 'Registration number', 'Book code', 'Issued date']
    tablefmt = "double_outline"
    print(tabulate(m, headers, tablefmt))
    my = con.commit()
    print('\n')

def displayreturnedbooks():
    my = con.cursor()
    sql = 'select * from return_book'
    my.execute(sql)
    m = my.fetchall()
    headers = ['Name', 'Registration number', 'Book code', 'Returned date']
    tablefmt = "double_outline"
    print(tabulate(m, headers, tablefmt))
    my = con.commit()
    print('\n')
    
def maincode():
    header = ["LIBRARY MANGEMENT APPLICATION"]
    footer = [['1.ADD BOOK'], ['2.ISSUE BOOK'], ['3.RETURN BOOK'], ['4.DELETE BOOK'],['5.DELETE ISSUED BOOK'], ['6.DELETE RETURNED BOOK'], ['7.VIEW MENU'], ['8.EXIT PROGRAM']]
    tablefmt = "simple"
    print(tabulate(footer, header, tablefmt))
    
maincode()

while True:
    print('\n')
    choice = int(input("Enter task number(1-8): "))
    print('\n')
    if choice == 1:
        addbook()
        maincode()

    elif choice == 2:
        issuebook()
        maincode()

    elif choice == 3:
        returnbook()
        maincode()

    elif choice == 4:
        deletebook()
        maincode()

    elif choice == 5:
        deleteissuedbook()
        maincode()

    elif choice == 6:
        deletereturnedbook()
        maincode()

    elif choice == 7:
            
        def viewmenu():
            
            header = ["VIEW MENU"]
            footer = [['1. DISPLAY BOOKS'], ['2. DISPLAY ISSUED BOOKS'], ['3. DISPLAY RETURNED BOOKS'], ['4. GO BACK TO MAIN MENU']]
            tablefmt = "simple"
            print(tabulate(footer, header, tablefmt))
            print('\n')

            choice1 = int(input("Enter task number(1-4): "))
            print('\n')
            
            if choice1 == 1:
                displaybook()
                print('\n')
                viewmenu()

            elif choice1 == 2:
                displayissuedbooks()
                print('\n')
                viewmenu()

            elif choice1 == 3:
                displayreturnedbooks()
                print('\n')
                viewmenu()

            elif choice1 == 4:
                print('\n')
                maincode()
                print('\n')

            else:
                print("Invalid choice. Please try again")
                print('\n')
                viewmenu()
                print('\n')

        viewmenu()

    elif choice == 8:
        print("Thank you for using library management application. Have a great day ahead!")
        break

    else:
        print("Invalid choice. Please try again")
        print('\n')
        maincode()
        print('\n')


