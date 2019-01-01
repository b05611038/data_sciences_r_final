import gzip
#--------------------------------------------------------------------------------
#the class and function are the basic function for data processing and analysis
#--------------------------------------------------------------------------------
def read_gz(file_path):
    with gzip.open(file_path, 'rb') as f:
        file_content = f.read()

    f.close()
    file_content = file_content.decode('utf-8')
    return file_content


