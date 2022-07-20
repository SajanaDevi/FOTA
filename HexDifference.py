f1 = open("1.hex", "r")
f2 = open("2.hex", "r")
memory_address = hex(0x08100000)  # bank2 address
i = 0
j = 0
k = 0
get_address = 0
no_of_bytes = 0
# l1 = []
# l2 = []
f1_list = list(f1)
f2_list = list(f2)
line_number = 0
key = 0
new_key = 0

for line1, line2 in zip(f1_list, f2_list):
    l1 = []
    l2 = []
    count = 0
    l3 = []

    if line1 == line2:
        pass

    else:
        for j in range(1, len(line1), 2):
            l1.append(line1[j: j + 2])
            l2.append(line2[j: j + 2])
            if line1[j:j + 2] != line2[j:j + 2]:
                no_of_bytes = count + 1

                count += 1

    with open('sajana.txt', 'a') as output:
        output.writelines("%s\n" % l1)
    with open('deviwrite.txt', 'a') as abd:
        abd.writelines("%s\n" % l2)

    for k in range(len(l1)):
        if l1[k] != l2[k]:
            index = str(k)
            print("printing index")
            print(index)
            #b = (int(memory_address, 16) + int(index, 16))
            #print("hellohello")
            integer = int(index)
            int_index = integer-4
            print(f" integer index is {int_index} ")
            hex_index=hex(int_index)
            print(f"hex index is {hex_index}")
            # hexb=hex(b)
            #print(f"hexb is {hexb}")
            address = l1[1:3]
            # print(address)
            line_address = "".join(l2[1:3])
            print(f"line address is {line_address}")
            int_line = int(line_address, 16)
            hex_address = hex(int_line)
            print(f" he address is {hex_address}")
            print(f"int line address is {int_line}")
            end = int_index+int_line
            print(f"ANSWER {end}")
            hex_end= hex(end)
            print(f"hex rhi is {hex_end}")

            data = (l2[k])
            adding = hex_end
            print(adding)

            print(f"hex data is{data}")
            new_data = int(data, 16)
            #print(f"Data in int is {new_data}")
            print()
            key = key + new_data
            #print(key)
            new_key =hex(key)
            #print(f"Checksum is {new_key}")
            with open("result30000.txt", "a+") as f:
                f.write( "\n"+ str(adding)+("&")+str(data))


with open("re.txt", "a+") as f:
    f.write("\n" + str(new_key))


f1.close()
f2.close()