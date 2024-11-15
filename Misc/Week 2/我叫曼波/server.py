import random
import base64

flag = "0xGame{OH_yEah_Wow_Duang_HajiMi_u_MADE_it!_and_MaY_5e_Y0u_hAv4_HeArD_7he_ST0ry_0f_Gu_Gao_MaN_B0}"

def real_real_real_random():
    random_num = random.randint(1,1000)
    return str(random_num)

def RC4(plain,K):
    S = [0] * 256
    T = [0] * 256
    for i in range(0,256): 
        S[i] = i
        T[i] = K[i % len(K)]

    j = 0
    for i in range(0,256): 
        j = (j + S[i] + ord(T[i])) % 256
        S[i], S[j] = S[j], S[i]

    i = 0
    j = 0
    
    cipher = []
    for s in plain:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        k = S[t]
        cipher.append(chr(ord(s) ^ k))

    return (base64.b64encode("".join(cipher).encode())).decode()

def base3(s):
    base3_s = ""
    for i in s:
        dec_value = ord(i)
        base3_c = ""
        while dec_value > 0:
            base3_c += str(dec_value % 3)
            dec_value = dec_value // 3
        base3_c = base3_c[::-1].rjust(5,"0")
        base3_s += base3_c
    return (base3_s)

def manbo_encode(base3_s):
    manbo_dict = {"0":"曼波","1":"哦耶","2":"哇嗷"}
    manbo_text = ""
    for i in base3_s:
        manbo_text += manbo_dict[i]
    return manbo_text

def encode(i):
    flag_part = flag[i:i+1]
    a = real_real_real_random()
    b = RC4(flag_part,a)
    c = base3(b)
    d = manbo_encode(c)
    return a,d

def welcome():
	print("Welcome to 0xGame2024!")
	print("Here is a flag which is prepared by MANBO.Oh YEAH!!!WoW!!!")
	print("But it seems to be encoded.")
	print("Dear hajimi,can you use your wisdom to decode it?")
	print("MANBO hopes you have read the encode.py before starting the challenge")

def cho():
    c = ""
    print("Please input your choice and MANBO will make a series of corresponding behavioral responses.")
    print("1.generate the next part of flag")
    print("2.show current key")
    print("3.show current ciphertext")
    c = input("> ")
    return c

    
welcome()
flag_part_index = 0


while (1):
    choice = cho()
    if choice == "1":
        if flag_part_index >= 96:
            print("You've reached the end of flag.Good Luck!----MANBO\n\n\n")
            exit(0)
        else:
            key,ciphertext = encode(flag_part_index)
            flag_part_index += 1
            print("Part of the flag have been generated.\n\n\n")
    elif choice == "2":
        if flag_part_index == 0:
            print("Please generate the first part of flag,otherwise MANBO cannot offer you the key.OvO")
            exit(1)
        print(key)
        print("\n\n")
    elif choice == "3":
        if flag_part_index == 0:
            print("Please generate the first part of flag,otherwise MANBO cannot offer you the ciphertext.OvO")
            exit(1)
        print(ciphertext)
        print("\n\n")
    else:
        print("Duang!!!MANBO only recognizes number 1,2,3.Please re-enter!\n\n\n")
