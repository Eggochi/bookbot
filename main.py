def wordcount(book):
    words=book.split()
    return len(words)

def sortdict(dict):
    # Transforms a dictionary into a list of dictionaries and sorts it by value of entry
    def sort_on(d):
        return d["num"]
    
    items=[]
    for x in dict:
        items.append({"letter": x , "num": dict[x]})
    items.sort(reverse=True, key=sort_on)
    return items

def lettercount(book):
    #gets the number of letters and sorts them from most to least
    letters={}
    for letter in book.lower():
        if letter.isalpha():
            letters[letter]=letters.get(letter,0)+1
    return sortdict(letters)

def main():
    book="books/frankestein.txt"
    with open("books/frankestein.txt") as f:
        file_contents= f.read()

    letters=lettercount(file_contents)
    print(f"Report for {book}")
    print(f"Word count {wordcount(file_contents)} \n")
    print("Letter count (from most to least used)")
    for x in letters:
        print(f"The '{x["letter"]}' character was found {x["num"]} times")


main()