a = int(input('First input: '))

# w = x = y = z = 0

if a == 0:
    w = x = y = z = "GREEN"
    pattern = "🟢 🟢 🟢 🟢"
elif a in [1, 3]:
    w = y = "GREEN"
    x = z = "RED"
    pattern = "🟢 🔴 🟢 🔴"
elif a in [2, 4]:
    w = y = "RED"
    x = z = "GREEN"
    pattern = "🔴 🟢 🔴 🟢"
else:
    print('❌ Error: Input must be 0-4')
    exit()

print(f"Output: w={w}, x={x}, y={y}, z={z}")
print(f"Visual: {pattern}")

