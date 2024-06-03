def star_pattern(size):
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

def diamond_pattern(size):
    # Upper part of diamond
    for i in range(size):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))
    # Lower part of diamond
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + '*' * (2 * i + 1))

def square_pattern(size):
    for i in range(size):
        print('*' * size)

def checkerboard_pattern(size):
    for i in range(size):
        print(' '.join('*' if (i + j) % 2 == 0 else ' ' for j in range(size)))

def cross_pattern(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def main():
    print("Welcome to ArtBot!")
    while True:
        print("\nChoose an art pattern to generate:")
        print("1. Star Pattern")
        print("2. Diamond Pattern")
        print("3. Square Pattern")
        print("4. Checkerboard Pattern")
        print("5. Cross Pattern")
        print("6. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '6':
            print("Thank you for using ArtBot! Goodbye!")
            break
        
        size = int(input("Enter the size of the pattern (e.g., 5): "))
        
        if choice == '1':
            star_pattern(size)
        elif choice == '2':
            diamond_pattern(size)
        elif choice == '3':
            square_pattern(size)
        elif choice == '4':
            checkerboard_pattern(size)
        elif choice == '5':
            cross_pattern(size)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        # Welcome to ArtBot!

        # Choose an art pattern to generate:
        # 1. Star Pattern
        # 2. Diamond Pattern
        # 3. Square Pattern
        # 4. Checkerboard Pattern
        # 5. Cross Pattern
        # 6. Exit
        # Enter the number of your choice: 1
        # Enter the size of the pattern (e.g., 5): 5
        #     *
        # ***
        # *****
        # *******
        # *********

        # Choose an art pattern to generate:
        # 1. Star Pattern
        # 2. Diamond Pattern
        # 3. Square Pattern
        # 4. Checkerboard Pattern
        # 5. Cross Pattern
        # 6. Exit
        # Enter the number of your choice: 6
        # Thank you for using ArtBot! Goodbye!
