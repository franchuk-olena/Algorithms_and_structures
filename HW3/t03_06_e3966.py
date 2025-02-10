def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    n = int(input().strip())
    collection = list(map(int, input().split()))
    m = int(input().strip())
    queries = list(map(int, input().split()))
    for k in queries:
        if binary_search(collection, k):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
