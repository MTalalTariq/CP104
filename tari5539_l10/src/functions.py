"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Muhammad Talal Tariq
ID:      169035539
Email:   tari5539@mylaurier.ca
__updated__ = "2022-11-16"
-------------------------------------------------------
"""
#task1 (not required)


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    data = fh.readline()
    result = []
    dataline = []
    i = 0
    while data != "":
        data = data.strip()

        dataline = data.split(",")  # turning string into list
        if i == n:
            result = dataline
        data = fh.readline()
        i += 1
    return result
# task2


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    # processes first line, then the rest
    # each iteration of the loop sees one line from the file
    data = fh.readline()
    result = []
    dataline = []
    while data != "":
        data = data.strip()

        dataline = data.split(",")  # turning string into list

        if dataline[0] == id_number:  # find the id
            result = dataline
            break
        # process line
        data = fh.readline()
    """ Wrong code
    i = 0
    while i < datlen:
        data[i] = data[i].split(",")
        i += 1
    j = 0
    while j < datlen:
        minidata = data[j]

        if minidata[0] == id_number:
            result = minidata

        j += 1
    """
    return result
# task7


def append_max_num(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of fh. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    fh.seek(0)  # 'a+' starts reading at end of file
    data = fh.readline()
    tempnum = 0
    num = 0
    while data != "":
        data = data.strip()
        tempnum = int(data)
        # print(data)
        if tempnum >= num:
            num = tempnum
        data = fh.readline()
    num = str(num)  # converted to str for appending to file
    fh.write(num)
    num = int(num)  # converting back to int for output
    return num
# task9


def count_frequency_value(fh, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fh.
    Use: count = count_frequency_value(fh, value)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fh (int)
    ------------------------------------------------------
    """
    data = fh.readline()  # process first line, then the rest in a loop
    count = 0
    while data != "":
        data = data.strip()
        data = int(data)
        if data == value:
            count += 1

        data = fh.readline()
    return count
# task12


def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    data = fh.readline()  # process first line, then the rest in a loop
    word = ""
    smollen = 10000  # the smallest word length so far
    while data != "":
        data = data.strip()
        wordlen = len(data)  # current word length
        if wordlen < smollen:
            smollen = wordlen
            word = data
        data = fh.readline()
    return word
# task14


def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    datalist = []  # list of text lines to be copied
    # reading fh_1
    data = fh_1.readline()
    i = 1
    while i <= n and data != "":
        # data = data.strip() stripping removed "/n", that was my error
        datalist.append(data)
        i += 1
        data = fh_1.readline()
    # appending fh_2
    # fh_2.writelines(datalist)

    for j in datalist:
        fh_2.write(j)
        # fh_2.write('/n')

    return
