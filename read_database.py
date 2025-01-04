# Reads the FCC database files and puts them into a list of list for each file
from datetime import datetime as dt

# Read input file
with open('inputs.txt', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            cutoff_date = line.strip()
        elif index == 1:
            zipcode_file = 'zipcode_files\\' + line.strip()


def parse_file_line_data(current_line):
    line_data_list = []
    data = ''
    for current_char in current_line:
        if current_char == '|':
            line_data_list.append(data)
            data = ''
        elif current_char != '|':
            data = data + current_char
    return line_data_list


# Read zip code file in as list
print('Reading: ' + zipcode_file)
zip_list = []
with open(zipcode_file, 'r') as file:
    for line in file:
        zip_list.append(line.strip())

# Read the EN.dat file into a list of lists
file_path = 'database_files\EN.dat'
print()
print('Reading: ' + file_path)
EN_list = []
with open(file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        line_data_list = parse_file_line_data(current_line)
        if line_data_list[18] in zip_list:
            EN_list.append(line_data_list)


# Read the HS.dat file into a list of lists
file_path = 'database_files\HS.dat'
print()
print('Reading: ' + file_path)
HS_list = []
b = dt.strptime(cutoff_date, '%m/%d/%Y')
i = 1
with open(file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        current_line = current_line + '|' # Needed to add make the parsing function work properly
        #print(current_line)
        line_data_list = parse_file_line_data(current_line)
        i = i + 1
        a = dt.strptime(line_data_list[4], '%m/%d/%Y')
        if line_data_list[5] == 'SYSGRT' and a >= b:
            HS_list.append(line_data_list)

print()
print('Compiling Final List of Hams')
final_list = []
for HS_people in HS_list:
    for EN_people in EN_list:
        if HS_people[1] in EN_people:
            final_list.append(HS_people)
            final_list.append(EN_people)


final_list_len = str(len(final_list))
print()
print('Final List Length: ' + final_list_len)


list_output_file = 'outputs\\results_list_output.txt'
print()
print('Writing list text to ' + list_output_file)
counter = 0
with open(list_output_file, 'w') as f:
    for line in final_list:
        counter = counter + 1
        f.write(f"{line}\n")
        if (counter % 2) == 0:
            f.write(f"\n")


address_output_file = 'outputs\\address_list_output.txt'
print()
print('Writing addresses to ' + address_output_file)
counter2 = 0
with open(address_output_file, 'w') as f:
    # Header
    num_of_results_str = "Number of Results from Query: " + final_list_len
    f.write(f"Address List Output File\n")
    f.write(f"{num_of_results_str}\n")
    f.write(f"-----------------------------------\n")
    f.write(f"\n")
    #Addresses
    for line in final_list:
        counter2 = counter2 + 1
        if (counter2 % 2) == 0:
            first = line[8]
            middle = line[9]
            last = line[10]
            callsign = line[4]
            if middle == '':
                full_name = first + ' ' + last + ' (' + callsign + ')'
            else:
                full_name = first + ' ' + middle + '. ' + last + ' (' + callsign + ')'
            address_line = line[15]
            PO_box_num = line[19]
            if address_line == '':
                address_line = 'PO Box #' + PO_box_num
            city = line[16]
            state = line[17]
            zip_code = line[18]
            csz = city + ', ' + state + ' ' + zip_code
            f.write(f"{full_name}\n")
            f.write(f"{address_line}\n")
            f.write(f"{csz}\n")
            f.write(f"\n")

print()
print('Process Complete')
