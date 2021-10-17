'''file_to_save = os.path.join("Analysis", "election_analysis.txt")
outfile = open(file_to_save, "w")
outfile.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
outfile.close()'''

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Desktop", "Class_Folder", "Module_3", "Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Desktop", "Class_Folder", "Module_3", "Resources", "election_results.csv")

#print(os.getcwd())

# Open the election results and read the file.
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)

     # Read and print the header row.
     headers = next(file_reader)
     print(headers)