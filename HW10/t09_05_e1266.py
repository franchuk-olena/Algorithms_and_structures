def find_max_(tape_length, CD_list, CD_count, CD_index, current_tape):
    best_found = current_tape
    for i in range(CD_index, CD_count):
        new_tape = current_tape + CD_list[i]
        if new_tape <= tape_length:
            result = find_max_(tape_length, CD_list, CD_count, i + 1, new_tape)
            if result == tape_length:
                return result
            if result > best_found:
                best_found = result

    return best_found

def find_max(tape_length, CD_list, CD_count):
    best_found = find_max_(tape_length, CD_list, CD_count, 0, 0)
    print(f"sum:{best_found}")


def main():
    while True:
        try:
            buffer = input()
            tokens = buffer.split()
            N = int(tokens[0])
            s = int(tokens[1])
            arr = list(map(int, tokens[2:]))
            find_max(N, arr, s)

        except EOFError:
            break


if __name__ == "__main__":
    main()
