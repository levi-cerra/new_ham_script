Title: New Ham Radio Licensee Address Lister

Creator: Levi Cerra (KC3ZSY)

Description: This is a python script with accompanying input and output text files that can be used to find
local hams that recieved their licenses after a chosen date. Anyone can feel free to take the code and change
it for their specific needs. There is a lot more data conainted here than just the addresses that the current
implementation returns.

Reason for project: This code was created to find recent ham radio licensees in a given area. It returns the 
addresses of the hams so that you could reach out to them via mail and invite them to join your ham radio 
club or welcome them into the hobby. A club could find all the surrounding zip codes in their area and then
mail an invitation to all new hams in their area that this program would output.


Software needed:
Python
No external packages required, only uses the datetime and pathlib libraries
Should be able to run on Windows, Mac, and Linux, but let me know if you run into any issues (Developed in windows)



Running Instructions:

1. Get updated data from the FCC 
	a. Go to https://www.fcc.gov/uls/transactions/daily-weekly
	b. Scroll down to Weekly Databases -> Amateur Radio Service
	c. Click Licenses and a new zip file will be downloaded from FCC website
	d. Take the HS.dat and EN.dat files from the zip file and place them in a folder called "database_files\"
		- I could not create an empty folder on github and the files are too big to upload
		- This folder should be located in the same directory you are running the python file from

2. Get list of zip codes within radius of desired location
	a. There are multiple ways of doing this, but below is the one I've found and use
	b. Go to https://www.unitedstateszipcodes.org/zip-code-radius-map.php
	c. Input the city and radius you desire
	d. Copy and paste the returned list into a text file in the "zipcode_files\" folder
	e. Change the third line of inputs.txt to the name of the zipcode list file
		- The code will only read one zipcode list file at a time, you can keep multiple in that folder though

3. Change the input dates to set the range that the code will use to return all ham licenses in that time frame
	a. Go to the inputs.txt file and change the first line to the desired start date
	b. Change the second line to the desired end date
		- You can also write "today" in this line and it will automatically use today's date
	c. Dates must be in format MM/DD/YYYY

4. Run the python script
	a. I have found that it takes about 3 minutes when searching for a years worth of hams, but times may 
	   vary depending on your machine

5. Retrieve Outputs
	a. Go to "outputs\" folder and open address_list_output.txt to see the list of addresses (easily readable)
	b. The address_list_output_csv.csv files is the same information as the address_list_output.txt but
	   can be fed read by a spreadsheet for easier use
		- I have created a google apps script that automatically populates a post card template with the
		  address information. If you are interested in that, I could publish it as well. There are also
		  other options and tools available (some cost money) that would work for automating that process
		  as well.
	c. results_list_output.txt has all the raw data from the database for all returned hams
		- Less useful, was more needed when writing the code



File Descriptions:
outputs/address_list_output.txt
  - plain text files of the output
	- lists date range and number of hams found in addition to the address list

outputs/address_list_output_csv.csv
  - outputs in csv format, can be opened in excel or google sheets to automate postcard making

outputs/results_list.txt
  - Used during development

database_files/
  - must be made locally and populated with the EN.dat and HS.dat files
	- files were too big to be uploaded, but they're not too unwieldy on a personal computer

zipcode_files/
  - example zip code list files used during testing located here
	- put your desired zip code list file in here and make sure to write the name in the input file

inputs.txt
  - input file
	- line 1: start date of query (currently 01/01/2024)
	- line 2: end start date of query in same format (or put "today" and it will automaticlly use today's date)
	- line 3: name of zip code list file you made (currently zips_carnegie_25_miles.txt)

read_database.py
  - Main script python script

README.txt




I hope this program can be used by those who need it. Hopefully it can help bring more people to your ham radio club!


Feel free to let me know if you run into any issues or if you need help running the code. I'd be happy to fix any
bugs or look into improvements you might need to make it work for your purposes.

