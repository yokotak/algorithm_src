# #%%
# def prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2, n):

#         if n % i == 0:
#             return False
        
#     return True
        
# if __name__=="__main__":
#     for i in range (0, 200, 10):
#         judge = "|"
#         for j in range(1,11):
#             value = i + j
#             if prime(value) == True:
#                 judge += "   P |"
#             else:
#                 judge += f'{value:>4} |' #
#         print(judge)

# #%%
# def is_prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2, n):

#         if n % i == 0:
#             return False
        
#     return True

# def is_judge(n):
#     judged = []
#     for i in range(1, n+1):
#         if is_prime(i) == False:
#             judged += [i]
#         else:
#             judged += ["P"]
#     return judged
#     # print(judged)

# def print_10_row(list):
#     count = 0
#     for i in list:
#         count += 1
#         print("|", end="")
#         if count % 10 == 0:
#             print (f'{i:>4} |')
#         else:
#             print (f'{i:>4} ', end="")

# if __name__=="__main__":
#     print(print_10_row(is_judge(205)))
# # %%
# print(is_judge(200))

#%%
def prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):

        if n % i == 0:
            return False
        
    return True
        
def view(n):
    for i in range (0, n, 10):
        judge = ""
        if n-i > 10:
            for j in range(1,10):
                value = i + j
                if prime(value) == True:
                    judge += "   P,"
                else:
                    judge += f'{value:>4},' #
            judge += f'{i+10:>4}'
            print(judge)
        else:
            for j in range(1, n-i):
                value = i + j
                if prime(value) == True:
                    judge += "   P,"
                else:
                    judge += f'{value:>4},' #
            judge += f'{n:>4}'
            print(judge)
            
if __name__=="__main__":
    view(1000)

# %%
