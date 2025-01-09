# Reads the FCC database files and puts them into a list of list for each file
from datetime import datetime as dt
from pathlib import Path

# Read input file
with open('inputs.txt', 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            start_date = line.strip()
        elif index == 1:
            end_date = line.strip()
            if end_date == "today":
                end_date = str(dt.today().date().strftime("%m/%d/%Y"))
                b = dt.strptime(end_date, '%m/%d/%Y')
            else:
                b = dt.strptime(end_date, '%m/%d/%Y')
        elif index == 2:
            zipcode_file_path = Path('zipcode_files/')
            zipcode_file = zipcode_file_path / line.strip()


# Used by the EN and HS reading loops to read the data in
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


# Progress bar to print to the command line
def progress_bar(progress, total):
    percent = (progress / float(total)) * 100
    bar = '#' * int(percent/2) + '-' * (50 - int(percent/2))
    print(f"\r|{bar}| {percent:.1f}%", end="\r")


# Read zip code file in as list
print('Reading: ' + str(zipcode_file))
zip_list = []
with open(zipcode_file, 'r') as file:
    for line in file:
        zip_list.append(line.strip())


# Column numbers that correspond to the data (information to help read code)
# EN
# 0 - EN, 1 - ID, 2 - blank, 3 - blank, 4 - Callsign, 5 - unknown, 6 - unknown, 7 - Full Name, 8 - First Name, 9 - MI, 10 - Last Name, 11 through 14 - blank,
# 15 - Address, 16 - City, 17 - State, 18 - Zip Code, 19 - PO Box Number, 20 - blank, 21 through 23 - unknown, 24 through 28 - blank

# HS
# 0 - HS, 1 - ID, 2 - blank, 3 - Callsign, 4 - Date, 5 - Type of Action Taken

# Read the EN.dat file into a list of lists
database_file_path = Path('database_files/')
EN_file_path = database_file_path / "EN.dat"
print()
print('Reading: ' + str(EN_file_path))
EN_list = []
with open(EN_file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        line_data_list = parse_file_line_data(current_line)
        if line_data_list[18] in zip_list and (len(line_data_list[4]) == 6): # The second criteria was added to only get first time licensees and not vanity
            EN_list.append(line_data_list)

print("Number of hams granted initial license in specified area: " + str(len(EN_list)))


# Read the HS.dat file into a list of lists
HS_file_path = database_file_path / "HS.dat"
print()
print('Reading: ' + str(HS_file_path))
HS_list = []
a = dt.strptime(start_date, '%m/%d/%Y')
i = 1
with open(HS_file_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        current_line = current_line + '|' # Needed to add make the parsing function work properly
        line_data_list = parse_file_line_data(current_line)
        i = i + 1
        current_date = dt.strptime(line_data_list[4], '%m/%d/%Y')
        if line_data_list[5] == 'SYSGRT' and (current_date >= a) and (current_date <= b) and (len(line_data_list[3]) == 6): # The second criteria was added to only get first time licensees and not vanity
            HS_list.append(line_data_list)

date_list_ham_num_str = "Number of hams granted initial license from " + start_date + " to " + end_date + ": " + str(len(HS_list))
print(date_list_ham_num_str)


print()
print('Compiling Final List of Hams')
final_list = []
EN_length = len(EN_list)
HS_length = len(HS_list)
if HS_length > EN_length:
    for prog, EN_people in enumerate(EN_list):
        progress_bar(prog + 1, len(EN_list))
        for HS_people in HS_list:
            if EN_people[1] in HS_people:
                final_list.append(HS_people)
                final_list.append(EN_people)
elif HS_length <= EN_length:
    for prog, HS_people in enumerate(HS_list):
        progress_bar(prog + 1, len(HS_list))
        for EN_people in EN_list:
            if HS_people[1] in EN_people:
                final_list.append(HS_people)
                final_list.append(EN_people)



final_list_len = str(int(len(final_list)/2))
print()
print()
print('Final List Length: ' + final_list_len)


outputs_file_path = Path('outputs/')
list_output_file = outputs_file_path / "results_list_output.txt"
print()
print('Writing list text to ' + str(list_output_file))
counter = 0
with open(list_output_file, 'w') as f:
    for line in final_list:
        counter = counter + 1
        f.write(f"{line}\n")
        if (counter % 2) == 0:
            f.write(f"\n")


address_output_file = outputs_file_path / "address_list_output.txt"
print()
print('Writing addresses to ' + str(address_output_file))
counter2 = 0
with open(address_output_file, 'w') as f:
    # Header
    num_of_results_str = "Number of Results from Query: " + final_list_len
    date_range_string = "From " + start_date + " to " + end_date
    f.write(f"Address List Output File\n")
    f.write(f"{date_range_string}\n")
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


address_csv_output_file = outputs_file_path / "address_list_output_csv.csv"
print()
print('Writing addresses to ' + str(address_csv_output_file))
counter3 = 0
with open(address_csv_output_file, 'w') as f:
    # Header
    f.write(f"Name,Callsign,Address,City,State,Zip\n")
    #Addresses
    for line in final_list:
        counter3 = counter3 + 1
        if (counter3 % 2) == 0:
            first = line[8]
            middle = line[9]
            last = line[10]
            callsign = line[4]
            if middle == '':
                full_name = first + ' ' + last
            else:
                full_name = first + ' ' + middle + '. ' + last
            address_line = line[15]
            PO_box_num = line[19]
            if address_line == '':
                address_line = 'PO Box #' + PO_box_num
            city = line[16]
            state = line[17]
            zip_code = line[18]
            f.write(f"{full_name},{callsign},{address_line},{city},{state},{zip_code}\n")


print()
print('Process Complete')
