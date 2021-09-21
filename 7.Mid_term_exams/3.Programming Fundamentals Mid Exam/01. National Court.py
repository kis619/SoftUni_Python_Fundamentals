em1 = int(input())
em2 = int(input())
em3 = int(input())

together = em1 + em2 + em3
ppl = int(input())

hours = 0
count = 0
while ppl > 0:

    ppl -= together
    hours += 1
    count += 1
    if not ppl <= 0 and count % 3 == 0:
        hours += 1
        count = 0

print(f"Time needed: {hours}h.")


# em1 = int(input())
# em2 = int(input())
# em3 = int(input())
#
# together = em1 + em2 + em3
# ppl = int(input())
#
# hours = 0
#
# while ppl > 0:
#     hours += 1
#     ppl -= together
#
#     if hours % 4 == 0:
#         hours += 1
# print(f"Time needed: {hours}h.")