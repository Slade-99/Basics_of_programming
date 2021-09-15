import random
name = input("Enter your name\n")
print(f"Hello, {name} . I am actually thinking of a number between 1 to 20 ")
num = random.randint(1,20)
def main():
    for i in range(1,6):
        guess = int(input("Can you try to guess the number?"))
        if guess>int(num):
            print("Your guess is too high.Try again")
        elif guess<int(num):
            print("Your guess is too low.Try again")
        elif guess==int(num):
            print(f"Great! you have guessed the number correctly in {i} tries")
            break
            
    if guess!=num:
        print(f"Sorry no more than 5 tries are allowed.\nThe correct answer was {num} ")

if __name__ == '__main__':
    main()



