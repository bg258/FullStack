def main():
    import sys 
    input = sys.stdin.read

    # Read input 
    data = input().splitlines()

    # First lines is the number of estimates (not needed directly)
    n = int(data[0])

    # Remaining lines are the estimates
    estimates = data[1:]

    # Compute and output the number of digits for each estimate
    for estimate in estimates:
        print(len(estimate))

if __name__ == "__main__":
    main()


"""
3
0
10
100
"""