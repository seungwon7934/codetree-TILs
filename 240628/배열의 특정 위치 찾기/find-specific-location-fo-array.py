arr = list(map(int, input().split()))

even_arr = arr[1::2]
three_mul_arr = arr[2::3]

print(f"{sum(even_arr)} {sum(three_mul_arr) / len(three_mul_arr):.1f}")