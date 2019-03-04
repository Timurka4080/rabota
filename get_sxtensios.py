import csv


set1 = {None}
with open('extensions.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        set1.add(row[0])

set2 = {str(i + 2000) for i in range(600)}
set_diff = set2 - set1
list_diff =  sorted(list(set_diff))

def compile_extension(number):
    '''
    Функция создает Список списков.
    Как аргумент ожидает Список внутренних номеров
    '''
    template = ('{num},,{num},default,0,,,{num},,,,,,,,'
        'default,{num},sip,SIP/{num},fixed,{num},{num},,'
        'dontcare,dontcare,dontcare,dontcare,disabled,'
        '10,disabled,enabled,{num},3,,,no,"device <{num}>",no,from-internal,'
        ',0.0.0.0/0.0.0.0,,rfc2833,no,no,dynamic,no,,,,'
        'no,172.16.0.0/22,5060,yes,60,no,5f2b7d0398fc70648484f82baba144ae,'
        'pai,accept,chan_sip,"udp,tcp,tls",yes,friend,'
        'inherit,,ENABLED,,,,,,,,,,,,,,,,,,yes,{num},Admin'
        ',,attach=no|saycid=no|envelope=no|delete=no,no,no,,,,1,,,')
    list_result = []
    for line in number:
        list_result.append(template.format(num = line))
    return list_result

summ_list = compile_extension(list_diff)


with open('/home/vagrant/tim/rabota/documents/result_extension.csv', 'w') as f:
    f.write(','.join(header)+'\n')
    for row in summ_list:
        f.write(row+'\n')