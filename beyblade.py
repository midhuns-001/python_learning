''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def read_input():
    tc = int(input())
    num_of_members = int(input())

    g_rev_members = input().split(' ')
    g_rev_members = list(filter(None, g_rev_members))
    g_rev_members = list(map(int, g_rev_members))

    opp_members = input().split(' ')
    opp_members = list(filter(None, opp_members))
    opp_members = list(map(int, opp_members))
    if num_of_members != len(g_rev_members):
        sys.exit(-1)
    if num_of_members != len(opp_members):
            sys.exit(-1)
    return tc, num_of_members, g_rev_members, opp_members

def find_max_fights(num_of_members, g_rev_members, opp_members):

    g_rev_members.sort()
    opp_members.sort()
    max_fights_won = 0
    #print(g_rev_members)
    #print(opp_members)
    temp_o_members = opp_members
    for i in reversed(range(len(g_rev_members))):
        for j in reversed(range(len(temp_o_members))):
           if g_rev_members[i] > temp_o_members[j]:
                #print(g_rev_members[i])
                #print(temp_o_members[j])
                max_fights_won = max_fights_won+1
                temp_o_members.pop(j)
                break

    print(max_fights_won)
    return max_fights_won


def main():
    tc, num_of_members, g_rev_members, opp_members = read_input()
    find_max_fights(num_of_members, g_rev_members, opp_members)


main()

