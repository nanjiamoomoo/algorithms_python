def decoder(path) -> str:
    dictionary = {}
    f = open(path)
    while f:
        line = f.readline()
        if line == "":
            break
        l = line.split()
        dictionary.update({int(l[0]): l[1]})
    f.close()
    index = 1
    step = 1
    res = []
    while index < len(dictionary) + 1:
        res.append(dictionary[index])
        step += 1
        index += step

    return ' '.join(res)

if __name__=="__main__":
    path = r"D:\GitHubRepo\algorithms_python\algorithms_python\File Handling\coding_qual_input.txt"    
    s = decoder(path)
    print(s)

   



    