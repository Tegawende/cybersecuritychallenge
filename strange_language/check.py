data = "36 53 68 56 3a 38 6d 74 29 35 39 51 57 2b 35 47 40 46 5d 75 31 2f 28 47 43 3c 26 38 23 42 48 3d 54 69 30 31 47 4d 4c 44 47 3d 2b 6e 5a 44 29 3f 45 54 44 2e 3e 53 40 37 6e 3f 61 2a 37 37 44 4a 58 37 72 72 6c 56 44 66 2f 48 33 3c 2c 34 69 58 30 6a 37 25 24 32 65 48 30 25 3d 5f 27 4b 64 46 3e 47 67 41 45 2b 5f 67 46 47 3b 6a 5c 53 3d 2a 38 64 45 45 2c 66 41 52 41 34 26 6e 2d 42 33 26 74 2d 3a 32 3c 5a 64 31 33 52 34 65 46 3e 48 75 53 39 35 64 3a 22 42 6c 51 55 53 3d 23 57 5a 45 3d 40 59 5f 5e 41 6a 4b 46 33 37 6f 44 72 55 3b 44 69 2d 34 33 44 2b 55 2e 37 58 41 2d 47 39 4d 54 3e 27 43 4a 4a 74 54 33 2d 53 32 2e 45 47 4a 60 75 33 46 62 42 56 45 60 5a 61 69 36 5b 21 36 57 46 5c 35 25 72 42 4a 60 3d 49 33 48 30 2a 71 42 69 5d 22 3c 43 4d 2e 45 3d 47 74 4b 71 4b 47 40 6a 2d 39 47 5b 6a 51 65 42 4e 36 72 6f 45 41 44 68 75 37 73 5b 69 74 36 3d 46 62 55 41 37 67 21 42 46 59 59 63"

tab = []
for couple in data.split(" "):
    x = int(couple[0])
    # y = int(couple) % 10
    tab.append(x)

print(max(tab))