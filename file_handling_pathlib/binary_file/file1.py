# with open('binary_file','bw') as b_file:
#     for i in range(21):
#         b_file.write(bytes([i]))
import shelve
dict_key = input("Enter a key: ")
with shelve.open('shelve_file') as sh_file:
    sh_file['miller'] = ' a person who owns or works in a corn mill'
    sh_file['programmer'] = 'a person who writes compyter programs'
    sh_file['app'] = 'an application, especially as downloaded by a user to a mobile device'
    if dict_key in sh_file:
        print(sh_file[dict_key])
    else:
        print("The key does not exist")

    # print(sh_file.get('software','I love you'))
    # for word, definition in sh_file.items():
    #     print(f"{word}: {definition}")
# sh_file = shelve.open('shelve_file')
# for key in sh_file:
#     print(key, sh_file[key])
# sh_file.close()