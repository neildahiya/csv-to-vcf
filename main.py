import csv

def csv_to_vcf(csv_file, vcf_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        
        with open(vcf_file, mode='w') as vcf:
            for row in reader:
                vcf.write("BEGIN:VCARD\n")
                vcf.write("VERSION:3.0\n")
                vcf.write(f"N:{row['LAST NAME']};{row['FIRST NAME']};;;\n")
                vcf.write(f"FN:{row['FIRST NAME']} {row['LAST NAME']}\n")
                
                if row['MOBILE NUMBER']:
                    vcf.write(f"TEL;TYPE=CELL:{row['MOBILE NUMBER']}\n")
                
                if row['EMAIL']:
                    vcf.write(f"EMAIL:{row['EMAIL']}\n")
                
                vcf.write("END:VCARD\n")

# Replace 'cte2024.csv' with your actual file name if it's different
csv_file = 'cte2024.csv'
vcf_file = 'contacts.vcf'
csv_to_vcf(csv_file, vcf_file)

print(f"VCF file '{vcf_file}' created successfully.")
