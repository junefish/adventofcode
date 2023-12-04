with open("adventofcode2020\day5\day5input.txt", "r") as input:
    seats = [line.rstrip() for line in input]

rows = []
cols = []
seat_ids = []
char_to_replace = {"F": "0", "B": "1", "L": "0", "R": "1"}
for seat in seats:
    row = slice(7)
    rows.append(seat[row].translate(str.maketrans(char_to_replace)))

    col = seat[-3:]
    cols.append(col.translate(str.maketrans(char_to_replace)))

for i in range(len(seats)):
    seat_ids.append(int(rows[i], 2) * 8 + int(cols[i], 2))

seat_ids.sort()

for i in range(len(seat_ids)):
    if seat_ids[i + 1] != seat_ids[i] + 1:
        print(seat_ids[i] + 1)
        break
