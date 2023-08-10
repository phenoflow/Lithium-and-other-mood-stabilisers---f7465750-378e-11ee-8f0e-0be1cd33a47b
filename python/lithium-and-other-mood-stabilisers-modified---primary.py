# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"4819020","system":"multilex"},{"code":"4823020","system":"multilex"},{"code":"59346020","system":"multilex"},{"code":"59347020","system":"multilex"},{"code":"61899020","system":"multilex"},{"code":"61900020","system":"multilex"},{"code":"62263020","system":"multilex"},{"code":"62264020","system":"multilex"},{"code":"72634020","system":"multilex"},{"code":"72635020","system":"multilex"},{"code":"74928020","system":"multilex"},{"code":"74929020","system":"multilex"},{"code":"74930020","system":"multilex"},{"code":"76250020","system":"multilex"},{"code":"76811020","system":"multilex"},{"code":"81319020","system":"multilex"},{"code":"93461020","system":"multilex"},{"code":"93463020","system":"multilex"},{"code":"95193020","system":"multilex"},{"code":"96128020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lithium-and-other-mood-stabilisers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lithium-and-other-mood-stabilisers-modified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lithium-and-other-mood-stabilisers-modified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lithium-and-other-mood-stabilisers-modified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
