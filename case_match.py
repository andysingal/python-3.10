todos = []
while True:
  user_input = input("Type add or show or exit: ")
  user_input = user_input.strip()
  match user_input:
      case "add":
         todo = input('Enter to do: ')
         todos.append(todo)
      case "show"|"display":
          for item in todos:
            item = item.title()
            print(item)
      case "exit":
          break 
      case _:
         print("Hey, you entered an unknown command")
print("Bye")  
