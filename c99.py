import re
import requests
import sys

output_set = set()  # Set to store unique lines

for line in sys.stdin:
    domain = line.strip()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'CSRF1026678917967820': 'subnet_ip106570706',
        'CSRF1096441495957721': 'addict110345100',
        'CSRF1007702562023574': 'cyberspace109555800',
        'CSRF1004003527439518': 'cyberspace100736110',
        'CSRF1023393969392558': 'car101143291',
        'CSRF1089386269258747': 'phisher103950502',
        'CSRF1059102427277992': 'computer104570500',
        'CSRF1071953466400943': 'intrusion109372456',
        'CSRF1028671235593408': 'counterfeiter103011803',
        'CSRF1017598117367098': 'spammer102830158',
        'CSRF1009903479562331': 'cyberspace101005200',
        'CSRF1043301363915168': 'network107234901',
        'CSRF1099529846092900': 'attacker104138624',
        'CSRF1006055432474521': 'firewall106316591',
        'CSRF1060852624268506': 'bot106926350',
        'CSRF1076408186085144': 'programmer108568747',
        'CSRF1072599247638037': 'infiltrator103138560',
        'CSRF1035817379234376': 'tenant101186226',
        'CSRF1074413032688342': 'prankster111001579',
        'CSRF1079649616617652': 'mask109658509',
        'CSRF1031964369854863': 'malware104296137',
        'CSRF1065145753781646': 'car101625796',
        'CSRF1068238697989899': 'hacking102707372',
        'CSRF1047013877733523': 'identitytheft105620795',
        'CSRF1010697487062123': 'cracker105337057',
        'CSRF1079483293129902': 'spy108836917',
        'CSRF1057273728798018': 'CSRF106708249',
        'CSRF1055466776362599': 'cyber100138636',
        'CSRF1047963330595649': 'car101453593',
        'CSRF1089846443658998': 'car105125547',
        'CSRF1069652405586429': 'hack101565042',
        'CSRF1108511320531573': 'Trojan108332645',
        'CSRF1053394228234221': 'network109534222',
        'CSRF1092479797143862': 'infiltrator107426288',
        'CSRF1051278072652514': 'TrojanHorse107578232',
        'CSRF1094592276075469': 'attacker107879343',
        'CSRF9843438138797932': 'phishing100365371',
        'jn': 'JS aan, T aangeroepen, CSRF aangepast',
        'domain': domain,
        'lol-stop-reverse-engineering-my-source-and-buy-an-api-key': '7e1408afd06beca934ee57afcc3e15a48f551f65',
        'scan_subdomains': ''
    }

    response = requests.post('https://subdomainfinder.c99.nl/', headers=headers, data=data)

    line = next(line for line in response.text.splitlines() if "value='https://subdomainfinder.c99.nl/scans/" in line)

    pattern = r"(?<=value=')[^']*"
    match = re.search(pattern, line)
    if match:
        value = match.group(0)
        response2 = requests.get(f'{value}', headers=headers, data=data)
        subdomain_lines = re.findall(r'<a href="//subdomainfinder.c99.nl/scans/([^"]*)"', response2.text)
        for subdomain_line in subdomain_lines:
            c_url = f'https://subdomainfinder.c99.nl/scans/{subdomain_line}'
            if re.search(f"{domain}", c_url):
                output_set.add(c_url)  # Add unique lines to the set

# Print unique lines
for line in output_set:
    response3 = requests.get(f'{line}')
    outputs = re.findall(fr"//[^']*{domain}", response3.text)
    for output in outputs:
        result = output.split("/")[2]
        if f"{domain}" in result:
            print(result)