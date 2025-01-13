'''fahrenheit to kelvin'''

print('===Fahrenheit Ke Kelvin ===\n\n')

fahren = float(input('Masukkan suhu dalam Fahrenheit: '))
print('Suhu dalam Fahrenheit adalah:', fahren, '°F\n\n')

kelvin = (fahren - 32) * 5/9 + 273.15
print('Suhu dalam Kelvin adalah:', kelvin, 'Kelvin')


'''kelvin to fahrenheit'''

print('===Kelvin Ke Fahrenheit ===\n\n')

kelvin_f = float(input('Masukkan suhu dalam Kelvin: '))
print('Suhu dalam Kelvin adalah:', kelvin_f, 'Kelvin\n\n')

fahren_k = (kelvin_f - 273.15) * 9/5 + 32
print('Suhu dalam Fahrenheit adalah:', fahren_k, '°F')

