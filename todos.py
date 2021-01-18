todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

index = 0 # Begin with index 0
while index < len(todos):
    todo = todos[index]
    print("%d: %s" % (index + 1, todo))
    index += 1