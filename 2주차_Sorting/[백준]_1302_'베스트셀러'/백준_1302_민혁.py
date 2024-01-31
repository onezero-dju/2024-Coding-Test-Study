# strip() 메서드는 책 제목의 공백을 제거하여 같은 제목임을 구분하기 위해 사용(도움)

from collections import Counter

def best_seller(books):
    counts = Counter(books)
    max_count = max(counts.values())
    # 가장 많이 팔린 책을 items()에 넣어 베스트셀러를 선정하기
    best_sellers = [book for book, count in counts.items() if count == max_count]
    return sorted(best_sellers)[0] # 가장 첫번째 정렬되어 있는 리스트를 반환하기

if __name__ == "__main__":
    N = int(input())
    # strip() 메서드 사용하여 공백 제거하기
    books = [input().strip() for _ in range(N)]
    print(best_seller(books))
