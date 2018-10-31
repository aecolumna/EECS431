def get_minimum_people(people_count, skills_count, skills_needed, skills_map):
    min_storage = [people_count]

    base_comparisons = 0
    least = people_count

    skills_set = set()
    people_set = set()

    condition_count = people_count

    for o in range(people_count):

        outer_count = 0
        skills_set.clear()
        people_set.clear()

        while (outer_count < people_count):

            # get base comparisons
            for i in range(o, outer_count + 1):

                for s in skills_map[i]:
                    skills_set.add(s)
                    people_set.add(i)
            #                print(skills_set)
            #                print(people_set)

            #            print("********************************")
            # compare base with the rest
            for j in range(outer_count + 1, people_count):
                #                print(skills_map[j])
                if (len(skills_set) == len(skills_set.union(skills_map[j]))):
                    if (len(people_set.union({j})) < least):
                        least = len(people_set.union({j}))

            outer_count += 1

    return least


def main():
    # main for hackerrank
    people_count, skills_count = map(int, input().split())

    skills_needed = [skill for skill in input().split()]

    skills_map = dict()

    for i in range(people_count):
        _ = input()
        skills_map[i] = {skill for skill in input().split()}

    # remove the useless people
    # skills_map_optimized = remove_useless_people(people_count, skills_map)

    print(get_minimum_people(people_count, skills_count, skills_needed, skills_map))
