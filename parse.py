from yacc import parser

def main():
    with open("input.txt", "r") as file:
        for line in file:
            if line.strip():
                parser.parse(line)

if __name__ == "__main__":
    main()
