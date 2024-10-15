# 06. Take a list of names.
names=["Gaurav","Kunal","Ankit","Rahul"]

#create a dictionary where key is name and value is favourite language of that person.
user_favourite_language={}
#iterate over the names and ask the user to input their favourite language.
for name in names:
    value=input(f"enter the favourite language of {name}: ")
    user_favourite_language[name]=value
print(user_favourite_language)
