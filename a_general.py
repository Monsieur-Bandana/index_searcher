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
