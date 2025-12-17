def process_file(filepath):
    my_file = open(filepath, 'r', encoding="utf-8")
    print(my_file)
    for line in my_file:
        print(line, end="")
    my_file.close()

# process_file("p04_simple_generator.py")


def process_file(filepath):
    try:
        with open(filepath, 'r', encoding="utf-8") as my_file:
            for line in my_file:
                print(line, end="")
        # konec -> zde je již soubor automaticky uzavřen
    except Exception as e:
        print(f"ERROR: {e}")


process_file("p04_simple_generator.py")
print("="*80)
process_file("p02_prime_iterator.py")

print("="*80)

try:
    with open("p02_prime_iterator.py", 'r', encoding="utf-8") as f:
        my_file = f.read()  # celý obsah souboru je v paměti (neefektivní)
        print(my_file)
except Exception as e:
    print(e)

print("="*80)

try:
    with open("p02_prime_iterator.py", 'r', encoding="utf-8") as f:
        lines = f.readlines()  # celý obsah souboru je v paměti jako seznam řádků (neefektivní)
        for line in lines:
            print(line, end="")
except Exception as e:
    print(e)

print("="*80)

def filter_keyword_from_file(filepath, keyword):
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            for line in f:
                cleaned_line = line.strip()

                if keyword in cleaned_line:
                    yield cleaned_line

    except Exception as e:
        print(f"ERROR: {e}")


f_name = "p02_prime_iterator.py"
for function in filter_keyword_from_file(f_name, "def"):
    print(f"[FUNCTION]: {function}")


print("\nEND")