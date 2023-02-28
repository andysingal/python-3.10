programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    },
]

def add_new_user(p_user_name,p_favorite_language,p_experience):
    new_user = {}
    new_user["user_name"] = p_user_name
    new_user["favorite_language"] = p_favorite_language
    new_user["experience"] = p_experience
    programming_language.append(new_user)
    print(programming_language)

print(add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10))