#program to find whether a given post is talking about "Gaurav" or not

post="Today, I met Gaurav at the coffee shop. We discussed some interesting tech topics, and he shared insights about his latest project."

if post.__contains__("Gaurav"):
    print("yes this post is talking about Gaurav")
else:print("no, this post is not talking about Gaurav")