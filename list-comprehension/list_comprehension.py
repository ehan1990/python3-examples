

def main():
    versions = ["1.0.0", "1.0.1", "1.0.2"]

    # append 'v' in front of versions
    versions = [f"v{x}" for x in versions]

    print(versions)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # only include even nums
    even_nums = [num for num in nums if num % 2 == 0]
    print(even_nums)


if __name__ == "__main__":
    main()
