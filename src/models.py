def users(username, email, password, role="user"):
    return {
        "username":username,
        "email":email,
        "password":password,
        "role":role
    }

def blogs(title, desc, image):
    return {
        "title":title,
        "desc":desc,
        "image":image
    }