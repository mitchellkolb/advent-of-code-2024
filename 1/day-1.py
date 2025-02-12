
from collections import Counter

def parse_input(file_path):
    left_list = []
    right_list = []
    with open(file_path, "r") as file:
        for line in file:
            left, right = map(int, line.split())  # Convert to integers
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    return total_distance

def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    similarity_score = sum(l * right_count[l] for l in left_list)
    return similarity_score

# Read input from file
file_path = "input.txt"  
left_list, right_list = parse_input(file_path)

total_distance = calculate_total_distance(left_list, right_list)
similarity_score = calculate_similarity_score(left_list, right_list)

print(f"Total Distance: {total_distance}")
print(f"Similarity Score: {similarity_score}")
