with open("st.txt", "w") as f:
    f.write("Cześć zapisano z Pythona.")

my_list = []

with open("st.txt", "r") as f:
    my_list.append(f.read())

with open("st.txt", "w") as f:
    my_text = ""
    for i in my_list:
        my_text = my_text + i + "\n"
    f.write(my_text + "Cześć zapisano z Pythona.")

with open("st.txt", "r") as f:
    print(f.read())
