import h5py
import pandas as pd

# HDF5文件路径
hdf5_file_path = 'your_hdf5_file.h5'  # 替换为你的HDF5文件路径

# Excel文件路径
excel_file_path = 'output_data.xlsx'  # 替换为你希望保存的Excel文件路径

# 打开HDF5文件
with h5py.File(hdf5_file_path, 'r') as hdf5_file:
    # 创建一个Excel writer对象
    writer = pd.ExcelWriter(excel_file_path, engine='openpyxl')

    # 遍历HDF5文件中的所有键
    for key in hdf5_file.keys():
        # 读取数据
        data = hdf5_file[key][:]

        # 将数据转换为DataFrame
        df = pd.DataFrame(data)

        # 将DataFrame保存到Excel文件中，每个键对应一个工作表
        df.to_excel(writer, sheet_name=key, index=False)

    # 保存Excel文件
    writer.save()

print(f'All keys from HDF5 file have been saved to {excel_file_path}')
