import PyPDF2, os, time
print("""
SH PDF Page Counter 1.0.1 
Identifies and count Pages in same directories
{ Shimul Hawladar }
""")

time.sleep(2)


def main():
    dir = os.listdir()
    fileWithPages = {}
    line = 0
    for x in dir:
        if ".pdf" in "." + x.split(".")[-1]:
            if line < len(x):
                line = len(x) + 10
            with open(x, 'rb') as pdf:
                numOfPage = PyPDF2.PdfReader(pdf)
                fileWithPages[x] = len(numOfPage.pages)
    print(f'{"=" * line}\n : Total Number of Pages : {sum(fileWithPages.values())}\n{"=" * line}\n')
    with open("result.txt", "w") as f:
        Header = f'{"=" * line}\n : Total Number of Pages : {sum(fileWithPages.values())}\n{"=" * line}\n'
        f.write(Header)
        for key,value in fileWithPages.items():
            f.writelines(f"{key} : {value} Page\n")


if __name__ == '__main__':
    main()
    print("Job completed successfully.\nPlease check { result.txt } file for separate report")
    time.sleep(5)


