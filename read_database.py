# Reads the FCC database files and puts them into a list of list for each file
from datetime import datetime as dt

# Inputs for the code
cutoff_date = '01/01/2024'
zipcode_file = 'allegheny_zips.txt'



def parse_file_line_data(current_line):
    line_data_list = []
    data = ''
    for current_char in current_line:
        if current_char == '|':
            if data != '':
                line_data_list.append(data)
                data = ''
        elif current_char != '|':
            data = data + current_char
    return line_data_list


# Read zip code file in as list
print('Reading zip list')
zip_list = []
with open(zipcode_file, 'r') as file:
    for line in file:
        zip_list.append(line.strip())

# Read the EN.dat file into a list of lists
print()
print('Reading EN.dat')
EN_list = []
file_path = 'EN.dat'
with open(file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        line_data_list = parse_file_line_data(current_line)
        #try:
        for i in line_data_list:
            if len(i) == 5 and i.isnumeric:
                if i in zip_list:
                    EN_list.append(line_data_list)


# Read the HS.dat file into a list of lists
print()
print('Reading HS.dat')
HS_list = []
file_path = 'HS.dat'
b = dt.strptime(cutoff_date, '%m/%d/%Y')
i = 1
with open(file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        current_line = current_line + '|' # Needed to add make the parsing function work properly
        #print(current_line)
        line_data_list = parse_file_line_data(current_line)
        i = i + 1
        try:
            a = dt.strptime(line_data_list[3], '%m/%d/%Y')
        except:
            print('HS.dat - No callsign on line: ' + str(i))
        try:
            if line_data_list[4] == 'SYSGRT' and a >= b:
                HS_list.append(line_data_list)
        except:
            print('HS.dat - No callsign on line: ' + str(i))

print()
print('Compiling Final List of Hams')
final_list = []
for HS_people in HS_list:
    for EN_people in EN_list:
        if HS_people[1] in EN_people:
            final_list.append(HS_people)
            final_list.append(EN_people)

print()
print('Final List Length: ' + str(len(final_list)))

print()
print('Writing text to output text file')
counter = 0
with open('output.txt', 'w') as f:
    for line in final_list:
        counter = counter + 1
        f.write(f"{line}\n")
        if (counter % 2) == 0:
            f.write(f"\n")

print()
print('Process Complete')
