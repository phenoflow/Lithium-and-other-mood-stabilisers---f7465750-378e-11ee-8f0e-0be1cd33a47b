# Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, David While, Yvonne Awenat, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"52411020","system":"multilex"},{"code":"52412020","system":"multilex"},{"code":"54482020","system":"multilex"},{"code":"54483020","system":"multilex"},{"code":"55618020","system":"multilex"},{"code":"56310020","system":"multilex"},{"code":"56315020","system":"multilex"},{"code":"59989020","system":"multilex"},{"code":"59990020","system":"multilex"},{"code":"69070020","system":"multilex"},{"code":"69071020","system":"multilex"},{"code":"73096020","system":"multilex"},{"code":"78712020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('lithium-and-other-mood-stabilisers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lithium-and-other-mood-stabilisers-gastroresistant---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lithium-and-other-mood-stabilisers-gastroresistant---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lithium-and-other-mood-stabilisers-gastroresistant---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
