def main(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a+b
        print(a)
	print("I'm best!")


if __name__ == "__main__":
    main(10)
