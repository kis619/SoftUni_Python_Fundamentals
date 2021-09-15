users_results = {}
languages = {}

user_input = input()
while not user_input == "exam finished":

    if "banned" in user_input:
        username, ban = user_input.split("-")
        del users_results[username]
        user_input = input()
        continue

    else:
        username, language, points = user_input.split("-")
        points = int(points)

        if language not in languages:
            languages[language] = 0
        languages[language] += 1

        if username not in users_results:
            users_results[username] = {language: points}
        else:
            if language in users_results[username]:
                if points > users_results[username][language]:
                    users_results[username][language] = points

            else:
                users_results[username][language] = points

        user_input = input()


users_results_upgraded = {}
for user, all_languages in users_results.items():
    for scores in all_languages.values():
        if user not in users_results_upgraded:
            users_results_upgraded[user] = scores
        else:
            if users_results_upgraded[user] < scores:
                users_results_upgraded[user] = scores


sorted_user_results = sorted(users_results_upgraded.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print("Results:")
for user, all_languages in sorted_user_results:
    print(f"{user} | {all_languages}")

languages_sorted = sorted(languages.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print("Submissions: ")
for user, all_languages in languages_sorted:
    print(f"{user} - {all_languages}")
