num = int(input())
bookList = dict()

for i in range(num):
    book = input()
    if book in bookList:
        bookList[book] += 1
    else:
        bookList[book] = 1

maxBooks = sorted([key for key, value in bookList.items() if value == max(bookList.values())])

maxBook = maxBooks[0]
print(maxBooks[0])



