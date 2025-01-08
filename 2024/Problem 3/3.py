result = 0
enabled = True

def find_next_mul(line, position):
    start_pos = position
    while True:
        mul_pos = line.find("mul(", start_pos)
        close_pos = line.find(")", mul_pos)
        if mul_pos == -1 or close_pos == -1:
            return -1, 0
        inside = line[mul_pos + 4:close_pos]
        parts = inside.split(",")
        if len(parts) == 2:
            first, second = parts
            first = first.strip()
            second = second.strip()
            if first.isdigit() and second.isdigit() and 1 <= len(first) <= 3 and 1 <= len(second) <= 3:
                return close_pos, (first, second)
        start_pos = mul_pos + 4


with open("input.txt") as file:
    pos = 0
    for line in file:
        while True:
            pos_do = line.find("do()", pos)
            pos_dont = line.find("don't()", pos)
            pos_mul = line.find("mul(", pos)

            candidates = []

            if pos_do != -1: candidates.append((pos_do, 'do'))
            if pos_dont != -1: candidates.append((pos_dont, 'dont'))
            if pos_mul != -1: candidates.append((pos_mul, 'mul'))

            if not candidates:
                break

            candidates.sort(key=lambda x: x[0])
            next_index, instruction = candidates[0]

            if instruction == 'do':
                enabled = True
                pos = next_index + len('do()')

            elif instruction == 'dont':
                enabled = False
                pos = next_index + len("don't()")

            else:
                if enabled:
                    close_pos = line.find(")", next_index)
                    if close_pos != -1:
                        inside = line[pos_mul + 4:close_pos]
                        parts = inside.split(",")
                        if len(parts) == 2:
                            first = parts[0].strip()
                            second = parts[1].strip()
                            if first.isdigit() and second.isdigit() and 1 <= len(first) <= 3 and 1 <= len(second) <= 3:
                                result += int(first)*int(second)
                pos = next_index + len("mul(")

        pos = 0

print(result)


