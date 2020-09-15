# Your code here
def finder(files, queries):
    cache = {}
    result = []
    for file in files:
        filepath = file.split('/')[-1]
        if filepath in cache.keys():
            cache[filepath].append(file)
        else:
            cache[filepath] = [file]
    for query in queries:
        if query in cache.keys():
            for path in cache[query]:
                result.append(path)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
