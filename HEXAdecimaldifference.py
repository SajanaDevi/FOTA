f1 = open("TST9.hex", "r")
f2 = open("TSTA.hex", "r")
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
new_key=0

for line1, line2 in zip(f1_list, f2_list):
    l1 = []
    l2 = []
    count = 0
    l3 = []

    if line1 == line2:
        pass

    else:
        # line_number += 1
        # print(line_number)
        for j in range(1, len(line1), 2):
            l1.append(line1[j: j + 2])
            l2.append(line2[j: j + 2])
            if line1[j:j + 2] != line2[j:j + 2]:
                no_of_bytes = count + 1
                # temp=str(j) + str(",") + str(j+1)
                # l3.append(j)

                # break
                count += 1

                ###print(f"\n The no.of bytes to be written is {no_of_bytes}")
                if count > 2:
                    print(f"lin1 is{line1}")
                    line1 = line2
                    #print(line1)

                else:

                    ###print(line1)
                    get_address = line1[3:7]

                    bank_address = hex(int(get_address, 16) + int(memory_address, 16))
                    # print(f"get is {bank_address}")
                    s = int(bank_address, 16) + count

    # print(l1)
    with open('sajana.txt', 'a') as output:
        output.writelines("%s\n" % l1)
    with open('deviwrite.txt', 'a') as abd:
        abd.writelines("%s\n" % l2)

    for k in range(len(l1)):
        if l1[k] != l2[k]:
            index = str(k)
            b = (int(memory_address, 16) + int(index, 16))
            address = l1[1:3]
            line_address = "".join(l1[1:3])
            # print(line_address)
            int_line = int(line_address, 16)
            # print(int_line)
            bank = hex(int_line + b)
            #print(bank)
            data = (l2[k])
            print(f"hex data is{data}")
            new_data = int(data, 16)
            print(f"Data in int is {new_data}")


            key = key + new_data
            print(key)
            new_key =hex(key)
            print(f"Checksum is {new_key}")

            with open("result0001.txt", "a+") as f:
                f.write( "\n"+ str(bank)+("&")+str(data))


with open("result0001.txt", "a+") as f:
    f.write("\n" + str(new_key))

f1.close()
f2.close()