data = input()
data_args = data.split('\\')
file, extension = data_args[-1].split('.')

print(f'File name: {file}')
print(f'File extension: {extension}')