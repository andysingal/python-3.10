# def generate_dictionary(n):
#     my_dict = dict()
#     for num in range(1,n+1):
#         my_dict[num] = num*num
#     return my_dict
#
# print(generate_dictionary(5))


def multiply_values(p_dict):
          output = 1
          for key in p_dict:
             output = output * p_dict[key]
          return output

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
print(multiply_values(my_dict))


