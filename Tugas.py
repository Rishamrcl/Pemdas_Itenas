import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)
print("DataFrame Awal:")
print(df)

df['Gaji karyawan setelah diberikan peningkatan 5%'] = df['Gaji'] * 1.05

print("\nDataFrame setelah diperbarui:")
print(df)

df['Gaji_Sebelumnya'] = df['Gaji karyawan setelah diberikan peningkatan 5%'] / 1.05
df['Peningkatan_Gaji'] = df['Gaji karyawan setelah diberikan peningkatan 5%'] - df['Gaji_Sebelumnya']

print("\nRingkasan perubahan:")
print(df[['Nama', 'Gaji_Sebelumnya', 'Gaji karyawan setelah diberikan peningkatan 5%', 'Peningkatan_Gaji']])

df['Gaji karyawan yang usianya di atas 30 tahun'] = df.apply(lambda row: row['Gaji karyawan setelah diberikan peningkatan 5%'] * 1.02 if row['Usia'] > 30 else row['Gaji karyawan setelah diberikan peningkatan 5%'], axis=1)
df['Peningkatan_Gaji_Akhir'] = df['Gaji karyawan yang usianya di atas 30 tahun'] - df['Gaji karyawan setelah diberikan peningkatan 5%']

print("\nGaji karyawan yang usianya di atas 30 tahun:")
print(df[['Nama', 'Usia', 'Gaji karyawan yang usianya di atas 30 tahun']])

print("\nRingkasan perubahan akhir:")
print(df[['Nama', 'Usia', 'Gaji karyawan yang usianya di atas 30 tahun', 'Peningkatan_Gaji_Akhir']])
