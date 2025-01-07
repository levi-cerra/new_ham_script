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
	a. I have found that it takes about 3 minutes to run on my machine for a years worth of hams, 
	   but times may vary

5. Retrieve Outputs
	a. Go to "outputs\" folder and open address_list_output.txt to see the list of addresses
	b. results_list_output.txt has all the raw data from the database for all returned hams


Feel free to let me know if you run into any issues or if you need help running the code. I'd be happy to fix any
bugs or look into improvements you might need to make it work for your purposes.

