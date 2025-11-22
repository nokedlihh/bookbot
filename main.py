import sys

def get_book_text(path):
    with open(path) as a:
        content= a.read()
    return content

from stats import count_words
from stats import count_char

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    alma=get_book_text(sys.argv[1])
    #print(alma) #kinyomja a teljes szoveget
    szavak_szama=count_words(alma)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {szavak_szama} total words")
    #betuk_szama=count_char(alma)
    print("--------- Character Count -------")
    for i in count_char(alma):
        char=i["char"]
        num=i["num"]
        print(f"{char}: {num}")
    #print(betuk_szama)
    print("============= END ===============")
main()