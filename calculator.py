with open("step_2.txt", "r") as f:
    end_result = 0
    for cnt, line in enumerate(f):
        input_arr = line.split()
        if (input_arr[1] == '+'):
            result = int(input_arr[2]) + int(input_arr[3])
            end_result += result
        elif (input_arr[1] == '-'):
            result = int(input_arr[2]) - int(input_arr[3])
            end_result += result
        elif (input_arr[1] == 'x'):
            result = int(input_arr[2]) * int(input_arr[3])
            end_result += result
        elif (input_arr[1] == '/'):
            result = int(input_arr[2]) / int(input_arr[3])
        elif (input_arr[1] == '^'):
            result = pow(int(input_arr[2]), int(input_arr[3]))
            end_result += result
        elif (input_arr[1] == '%'):
            result = int(input_arr[2]) % int(input_arr[3])
            end_result += result

print("Step2 result ", end_result) # 756216.3057730488

f2 = open("step_3.txt", "r")
lines = f2.read().splitlines()
idx = 0
visited = []
while True:
    print(idx)
    if idx > len(lines):
        break
    line = lines[idx]
    if line in visited:
        break
    visited.append(line)
    input_arr = line.split()
    if (input_arr[1] != "calc"):
        idx = int(input_arr[1]) - 1
        continue
    if (input_arr[2] == '+'):
        result = int(int(input_arr[3]) + int(input_arr[4]))
        idx = int(result) - 1
    elif (input_arr[2] == '-'):
        result = int(int(input_arr[3]) - int(input_arr[4]))
        idx = int(result) - 1
    elif (input_arr[2] == 'x'):
        result = int(int(input_arr[3]) * int(input_arr[4]))
        idx = int(result) - 1
    elif (input_arr[2] == '/'):
        result = int(int(input_arr[3]) / int(input_arr[4]))
        idx = int(result) - 1
    elif (input_arr[2] == '%'):
        result = int(int(input_arr[3]) % int(input_arr[4]))
        idx = int(result) - 1
    elif (input_arr[2] == '^'):
        result = pow(int(input_arr[2]), int(input_arr[3]))
        idx = int(result) - 1
print("Step3 IDX: ", idx, " Value ", lines[idx])