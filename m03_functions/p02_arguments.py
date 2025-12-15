def print_full_name(name: str, surname: str, **kwargs) -> None:
    print(name, surname, **kwargs)


print_full_name("Adam", "Bernau")
print_full_name(name="Bedřich", surname="Smetana")
print_full_name("Cyril", surname="Svoboda")
#print_full_name(name="Dušan", "Čermák")  # SyntaxError: positional argument follows keyword argument
print_full_name(surname="Bodocká", name="Eva")  # Eva Bodocká
print_full_name("Filip", "Novák", sep="_", end="=\n")
