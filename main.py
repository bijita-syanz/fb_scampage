import json 
import os 


file_path = "data.json"


def banner() :
    print("""
.------..------..------..------..------..------..------..------..------..------..------.
|F.--. ||B.--. ||_.--. ||S.--. ||C.--. ||A.--. ||M.--. ||P.--. ||A.--. ||G.--. ||E.--. |
| :(): || :(): || :/\: || :/\: || :/\: || (\/) || (\/) || :/\: || (\/) || :/\: || (\/) |
| ()() || ()() || :\/: || :\/: || :\/: || :\/: || :\/: || (__) || :\/: || :\/: || :\/: |
| '--'F|| '--'B|| '--'_|| '--'S|| '--'C|| '--'A|| '--'M|| '--'P|| '--'A|| '--'G|| '--'E|
`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'
""")
    print()
def main( ):
    while True :
        choise = input(">> ")
        if choise == "show" :
            read(file_path)
        elif choise == "rm":
            delet(file_path)
        elif choise == "":
            pass
        else :
            print("invalid command !")

def read(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            rownumber = 0
            for entry in data:
                rownumber +=1
                print(f"\nRow  {rownumber}:")
                for key, value in entry.items():
                    print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please check the file format.")

def delet(file_path):
    r = input("do you want to delete the json file (y/n) : ")
    if r == "y" :
        with open(file_path , "w") as file :
            file.write(" ")

if __name__ == "__main__" :
    banner()
    main()