
    Phase I – Load Input Data
        Validate the data found in the Excel spreadsheets.

                       DONE BUT VERIFY i.    ~~Ensure~~ that all addresses listed in the Packages spreadsheet match EXACTLY with the addresses listed in the Distances spreadsheet.

                

                        DONE     i.     You can use Excel to do this automatically through the File->Save As options (and select CSV)

                        DONE     ii.     Open the .csv files and clean it up so it only has the data you need

                        DONE    For the packages.csv file, you need 40 rows (each with 8 fields / columns) of package data only.
                        DONE    For the distances.csv file, you need 27 rows (each with 27 fields / columns) of numeric distance values only.
                        DONE    The addresses that correlate to the distance file should be stored in a separate addresses.csv file that are listed in the same order as they appear in the distance Excel spreadsheet. Then you can correlate a specific package address to a specific distance table index by finding the address location within the address data.

                        DONE    iii.     Create a hash table from scratch with an insert() and lookup() function that is called out in the requirements.

                        DONE    Verify that the hash table insert() and lookup() function works properly using some test data.

                        DONE        iv.     Utilize the “csvreader” library that is built into python to extract the package data from the csv file from above.

                        DONE        Create a Package class that includes the 8 fields from the package csv file.
                        DONE        Read a row from the package csv file and create a Package object with it
                        DONE        Add the package object to the hash table using the insert() function.

                                v.     Utilize the “csvreader” library that is built into python to extract the distance data from the csv file from above.

                Create a 2D array (list of lists) that will store the distance information (OPTION 1.1)
                    Read a row from the distance csv file and insert it into the 2D array at the proper position.
                #OR Create Node objects with that are connected to other Node objects via edge weights. (OPTION 1.2)
                    Read a row from the distance csv file and populate the Node and edge weight information at the proper position.

                                                  vi.     Utilize the “csvreader” library that is built into python to extract the address data from the csv file from above.

                Utilize a list or dictionary to store the address information
                Create an address_lookup(string address) function that will translate the specific string address into a numeric value that can be returned.
                    NOTE: The address_lookup() function is only needed if you utilize the 2D array (from OPTION 1.1 above).