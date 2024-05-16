from collections import deque

tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = [int(x) for x in input().split()]
arti_found = False
while tools and substances:

    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_substance * current_tool

    if result in challenges:
        challenges.remove(result)
        if not challenges:
            print('Harry found an ostracon, which is dated to the 6th century BCE.')
            arti_found = True
            break

    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)


if (not tools or not substances) and not arti_found:
    print('Harry is lost in the temple. Oblivion awaits him.')

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")
