# Another way of accessing text files with a URL (Other way is better)
def count_word(url):
    from urllib import request
    from urllib.error import URLError

    try:
        with request.urlopen(url) as f:
            content = f.read()
    except URLError:
        return("The URL" + url + " does not exist")
    else:
        return len(content.split())

print(count_word("https://www.gutenberg.org/files/2000/2000-0.txt"))
print(count_word("https://there_is_no_file.txt"))

