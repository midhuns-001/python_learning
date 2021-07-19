''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
'''
    Method to read the input from STDIN
    Format the qty values in a list and convert the
    list elements into integers
'''
def read_user_input():
    no_of_ingred = int(input())

    qty_of_each_ingred = input().split(' ')
    qty_of_each_ingred = list(filter(None, qty_of_each_ingred))
    qty_of_each_ingred = list(map(int, qty_of_each_ingred)) 

    qty_of_lab_ingred = input().split(' ')
    qty_of_lab_ingred = list(filter(None, qty_of_lab_ingred))
    qty_of_lab_ingred = list(map(int, qty_of_lab_ingred)) 
 
    return no_of_ingred, qty_of_each_ingred, qty_of_lab_ingred

'''
    Method to find the max no.of Powerpuffs that
    can be created out of given ingredients
'''
def find_max_number(no_of_ingred, qty_of_each_ingred, qty_of_lab_ingred):
    num = []
    for i in range(no_of_ingred):
        num.append(int(qty_of_lab_ingred[i]/qty_of_each_ingred[i]))
    print(min(num))
    return(min(num))
        

def main():

    num, qty, lab_qty = read_user_input()
    find_max_number(num,qty,lab_qty)
main()


