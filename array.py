def main():
    score = [78, 85, 90, 66, 88]
    total_score = sum(score)
    average_score = total_score / len(score) 
    print("== main/master branch output ==")
    print(f"Score: {score}")
    print(f"Sum: {total_score}")
    print(f"Average: {average_score}")
if __name__ == "__main__":
    main()