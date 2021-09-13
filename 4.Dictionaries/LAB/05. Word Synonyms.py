number_of_pairs = int(input())

syn_dict = {}

for _ in range(number_of_pairs):
    word = input()
    synonym = input()
    if word not in syn_dict:
        syn_dict[word] = []
    syn_dict[word].append(synonym)

for each_word in syn_dict:
    print(f"{each_word} - {', '.join(syn_dict[each_word])}")

# for key, value in syn_dict.items():
#     print(f"{key} - {', '.join(value)}")
