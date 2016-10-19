majors = [ ]

    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors)

    count = 0
    for major in majors:
        if major == current_major:
            count += 1
        else:
            print(current_major, count)
            current_major == major
            count = 1

value = 1.0
while iterations > 0:
    value = 0.5 * (value + number / value)
    iterations -= 1
return value