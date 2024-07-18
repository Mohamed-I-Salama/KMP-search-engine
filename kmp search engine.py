import time

def KMPSearch(pat, txt):
   
    M, N = len(pat), len(txt)
    lps = [0] * M

    i, length = 1, 0
    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    i, j = 0, 0
    occurrences = []
    while i < N:
        if pat[j] == txt[i]:
            i, j = i + 1, j + 1
            if j == M:
                occurrences.append(i - j)
                j = lps[j - 1]
        else:
            if j:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

def search_engine(filename, search_term):
    
    results = {}
    try:
        with open(filename, "r") as file:
            for doc_id, document in enumerate(file):
                occurrences = KMPSearch(search_term, document.strip())
                if occurrences:
                    results[doc_id] = occurrences
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None  

    return results

if __name__ == "__main__":
    filename = "kmpppp.txt" 
    search_term = input("What would you like to search for? ")

    start_time = time.time()
    results = search_engine(filename, search_term)

    if results:  
        for doc_id, occurrences in results.items():
            print(f"Pattern recognized in line {doc_id + 1} at positions: {occurrences}")
    else:
        if results is not None:
            print("Pattern not found in the file.")

    end_time = time.time()
    print(f"Search completed in {end_time - start_time:.6f} seconds")

