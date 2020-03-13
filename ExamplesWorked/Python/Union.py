######## Union
num_english_subs = int(input())
english_sub_ids = set(map(int, input().split()))
num_french_subs = int(input())
french_sub_ids = set(map(int, input().split()))

all_subs = english_sub_ids.union(french_sub_ids)
print(len(all_subs))


######### Intersection
num_english_subs = int(input())
english_sub_ids = set(map(int, input().split()))
num_french_subs = int(input())
french_sub_ids = set(map(int, input().split()))

all_subs = english_sub_ids.intersection(french_sub_ids)
print(len(all_subs))

######### Difference
num_english_subs = int(input())
english_sub_ids = set(map(int, input().split()))
num_french_subs = int(input())
french_sub_ids = set(map(int, input().split()))

all_subs = english_sub_ids.difference(french_sub_ids)
print(len(all_subs))

########## Symmetric Difference

num_english_subs = int(input())
english_sub_ids = set(map(int, input().split()))
num_french_subs = int(input())
french_sub_ids = set(map(int, input().split()))

all_subs = english_sub_ids.symmetric_difference(french_sub_ids)
print(len(all_subs))