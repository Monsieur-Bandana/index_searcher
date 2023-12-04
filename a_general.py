from csv import writer


def name_creator(link, filetype, prfx=""):
    original_string = link
    characters_to_remove = [':', '/', '.']

    # Using a loop to remove characters
    resulting_string = ''.join(
        char for char in original_string if char not in characters_to_remove)
    resulting_string = resulting_string.replace("http", "")
    resulting_string = resulting_string.replace("www", "")

    filename = prfx + resulting_string + "." + filetype
    return filename


def progress_definer(i, listi):
    print("step no " + str(i) + ", of " +
          str(len(listi)) + " total steps completed")
    i = i+1
    return i


def createCsvFile(filename, res):
    filename = filename + '.csv'
    with open(filename, 'a', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(res)
        f_object.close()
