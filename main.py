# print("Hello World")
## hello this is a comment
# x = 5  # Final exam score
#
# print("Your Learning Path: \n\t - Python Basics \n\t - Data Engineering \n\t - AI")
#
# print("This value of x is", x)
#
# name = input("Enter your name:")
# print("Your name is", name)
# name = input("Enter your name: ")

# print("info@datawith" + name + ".com")
# print("support@datawith" + name + ".com")
# print("www.datawith" + name + ".com")

# age = int(input("What is your age "))
# ageInFive = str(age + 5)
# print("In five years you are going to be " + ageInFive + " years old")

# tempTrue = True
# tempFalse = False
#
# floatValue = 3.25
# intValue = 3
#
# print(floatValue + intValue)
#
# age = 20
# height = 1.75
# name = "Orgest"
# isStudent = True
# acceptedGenpact = None

# print(type(age))
# print(type(height))
# print(type(name))
# print(type(isStudent))
# print(type(acceptedGenpact))
# print(type(str(age)))

# print(len(name))
# print(len(str(age)))

# password = "1234123123"
#
# text = """
# Python is a pretty interesting language
# It is simple
# But powerful
# """
#
# if len(password) < 8:
#    print("Password too short")
# else:
#    print("Password long enough")
#
# print(text.count("i"))

# price = "123.4"
# phoneNumber = "+49 (176) 123-4567"
# isEuropian = True
#
# if isEuropian:
#    print(price.replace(".", ","))
# else:
#    print(price)
#
# print("PhoneNumber is " + phoneNumber)
# print(
#    "PhoneNumber trimmed is "
#    + phoneNumber.replace("-", "")
#    .replace("+", "")
#    .replace("(", "")
#    .replace(")", "")
#    .replace(" ", "")
# )
#

# tempStamp = "2026-09-20 14:30"
#
#
# def stampParser(stamp: str):
#    tempList = stamp.split(" ")
#    date = tempList[0]
#    time = tempList[1]
#    return f"The date is {date} while the time is {time}"
#
#
# def extractYear(stamp: str):
#    return stamp[0:4]
#
#
# print(stampParser(tempStamp))
# print(extractYear(tempStamp))
# print(tempStamp[-5:])  # This extracts the time given the format above
#
# phone1 = "+48-176-12345"
# phone2 = "48-456-7890"
#
#
# def trimPhone(phone: str):
#    return phone[phone.find("-") + 1 :]
#
#
# print(trimPhone(phone1))
# print(trimPhone(phone2))


# age = 20
# height = 1.75
# name = "Orgest"
# isStudent = True
# acceptedGenpact = None
#
#
# print(age)
# print(height)
# print(name)
# print(isStudent)
# print(acceptedGenpact)
#
# print(type(age))
# print(type(height))
# print(type(name))
# print(type(isStudent))
# print(type(acceptedGenpact))
#
#
# print(age.bit_length())
# print(len(str(height)))
# print(len(name))
# print(isStudent.bit_length())
# print(len(str(acceptedGenpact)))

# import random
#
# tempNr = random.random() * 100
# print(tempNr)
# print(int(tempNr))
# print(int(tempNr) % 2 == 0)
#
#

# tempNr = 5
# if tempNr % 2 == 0 and tempNr > 2:
#    print("Condition Fulfilled")
#
#


# def allowUser(isLoggedIn: bool, isGuest: bool, isBanned: bool):
#    return (isLoggedIn ^ isGuest) and (not isBanned)


# print(allowUser(False, True, False))
#
# x = [5]
# y = [5]
#
# print(x is y)
#
#

# user = {
#    "age": 20,
#    "name": "Orgest",
#    "password": "Orgestasdasdad",
#    "email": "Orgest@gmail.com",
#    "isAdmin": True,
#    "isModerator": False,
#    "isBanned": False,
# }
#
#
# def validate_user(user):
#    if user.get("isBanned"):
#        return False
#
#    name = user.get("name")
#    password = user.get("password")
#    email = user.get("email")
#    age = user.get("age")
#
#    if not isinstance(name, str):
#        return False
#
#    if not isinstance(password, str) or len(password) < 8 or " " in password:
#        return False
#
#    if not isinstance(email, str) or "@" not in email:
#        return False
#
#    if not isinstance(age, int) or age < 18:
#        return False
#
#    return True
#
#
# print(validate_user(user))
# print(bool(0))
#
#

#
# email = "Password12"
#
#
# def emailValidator(email):
#    if email is None:
#        return False
#    if len(email) > 254:
#        return False
#    if email.count(".") == 0:
#        return False
#    if email.count("@") != 1:
#        return False
#    if not (email[0].isdigit() or email[0].isalpha()):
#        return False
#    if not (email[-1].isdigit() or email[-1].isalpha()):
#        return False
#    if not (email.endswith(".org") or email.endswith(".com") or email.endswith(".net")):
#        return False
#    return True
#
#
# password = "Password12"
#
#
# def passwordValidator(password):
#    if password is None:
#        return False
#    if len(password) < 8:
#        return False
#    if not any(c.isupper() for c in password):
#        return False
#    if not any(c.islower() for c in password):
#        return False
#    if password == email:
#        return False
#    return True
#
#
# print(passwordValidator(password))
# print(emailValidator(email))
#
#
#
#
#

# items = [1, 2, 3, 4]
# for i, value in enumerate(items):
#    items[i] *= 2
#
# print(items)
#
# tempString = "Python"
#
# scores = [80, 50, 60, 75]
# total = 0
#
# for i, score in enumerate(scores):
#    total += score
#    print("Final total:", total) if i == len(scores) - 1 else print(
#        "Current total:", total
#    )

# for i in range(1, 11):
#    print(f"7 x {i} = {7 * i}")
#
# for i in range(7):
#    print("*" * i)
#
# for i in range(11):
#    if i == 7:
#        break
#    print(i)
#    o
# weekend = ["Sat", "Sun"]
# days = ["Mon", "Tue", "Wed", "Sun", "Sat"]
# for day in days:
#    if day in weekend:
#        continue
#    print(f"Workday {day}")
# else:
#    print("The loop has ended")
#
# file_list = [
#    "report.csv",
#    "data.xlsx",
#    "summary.docx",
# ]
#
#
# def findDuplicate(file_list):
#    seen = set()
#    for file in file_list:
#        if file in seen:
#            return True
#        seen.add(file)
#    return False
#
#
# print(findDuplicate(file_list))
#
#
#
# temp = "Python"
# print(temp)
# print(list(temp))
# print("".join(list(temp)))
#

# temp_list = [
#    1,
#    0,
#    3,
#    1,
#    1,
#    11,
#    1,
# ]
# temp_list.append(4)
# temp_list.pop()
# temp_list.insert(10, 0)
#
# print(temp_list)
# print(len(temp_list))
# print(1 in (temp_list))
# print(temp_list.count(1))
# print(all(temp_list))
# print(max(temp_list))
# print(min(temp_list))
# print(sum(temp_list))
#
#
#
# matrix = [
#    [6, 2, 9],
#    [3, 5, 4],
#    [0, 7, 1],
# ]
#
#
# def sortMatrix(matrix: list[list[int]]):
#    flat = []
#
#    for row in matrix:
#        flat.extend(row)
#
#    flat.sort()
#    cols = len(matrix)
#
#    tempMatrix = []
#    for i in range(0, len(flat), cols):
#        chunk = flat[i : i + cols]
#        tempMatrix.append(chunk)
#    return tempMatrix
#
#
# matrix = sortMatrix(matrix)
# print(matrix)


# letters = ["a", "b", "c"]
# numbs = [1, 2, 3]
# newList = [letters, numbs]
# print(list(zip(numbs, letters)))
#
#
#
# nums = ["1", "2", "3", "4", "a"]
# it = iter(nums)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
#
#
#
# multiplyThree = lambda x: x * 3
# print(list(map(multiplyThree, nums)))
# print(list(filter(str.isalpha, nums)))
# price = [1, 2, 6, 7]
#
#
# priceModified = [x * 2 for x in price if x % 2 == 0]
#
# print(priceModified)
#
# tempSet = set()
# tempSet.add(10)
# print(tempSet)
# print(10 in tempSet)
# tempSet.remove(10)
# print(tempSet)
# print(10 in tempSet)
#
#
# tempDict = {"id": 1, "age": 20, "college": "UBT"}
# print(tempDict["id"])
# print(tempDict.get("id"))
#
# tempDict["name"] = "Orgest"
#
# print(tempDict)
# tempDict.pop("id", "Not Found")
# print(tempDict)
#

user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

tempUser = [value.upper() for key, value in user.items() if isinstance(value, str)]
print(tempUser)
