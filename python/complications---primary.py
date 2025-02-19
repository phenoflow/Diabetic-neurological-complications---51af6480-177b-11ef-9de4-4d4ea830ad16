# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"17247.0","system":"readv2"},{"code":"45467.0","system":"readv2"},{"code":"49146.0","system":"readv2"},{"code":"109197.0","system":"readv2"},{"code":"40962.0","system":"readv2"},{"code":"67853.0","system":"readv2"},{"code":"47409.0","system":"readv2"},{"code":"72320.0","system":"readv2"},{"code":"18230.0","system":"readv2"},{"code":"95351.0","system":"readv2"},{"code":"109865.0","system":"readv2"},{"code":"50813.0","system":"readv2"},{"code":"34268.0","system":"readv2"},{"code":"62674.0","system":"readv2"},{"code":"66965.0","system":"readv2"},{"code":"35385.0","system":"readv2"},{"code":"54008.0","system":"readv2"},{"code":"99231.0","system":"readv2"},{"code":"39809.0","system":"readv2"},{"code":"59903.0","system":"readv2"},{"code":"101735.0","system":"readv2"},{"code":"46301.0","system":"readv2"},{"code":"45919.0","system":"readv2"},{"code":"39317.0","system":"readv2"},{"code":"24694.0","system":"readv2"},{"code":"18425.0","system":"readv2"},{"code":"37315.0","system":"readv2"},{"code":"61829.0","system":"readv2"},{"code":"35785.0","system":"readv2"},{"code":"2340.0","system":"readv2"},{"code":"17067.0","system":"readv2"},{"code":"7795.0","system":"readv2"},{"code":"5002.0","system":"readv2"},{"code":"48078.0","system":"readv2"},{"code":"50527.0","system":"readv2"},{"code":"101311.0","system":"readv2"},{"code":"68105.0","system":"readv2"},{"code":"42831.0","system":"readv2"},{"code":"47816.0","system":"readv2"},{"code":"16491.0","system":"readv2"},{"code":"67905.0","system":"readv2"},{"code":"55842.0","system":"readv2"},{"code":"61523.0","system":"readv2"},{"code":"16230.0","system":"readv2"},{"code":"2342.0","system":"readv2"},{"code":"44033.0","system":"readv2"},{"code":"60208.0","system":"readv2"},{"code":"22573.0","system":"readv2"},{"code":"52283.0","system":"readv2"},{"code":"91943.0","system":"readv2"},{"code":"98616.0","system":"readv2"},{"code":"41716.0","system":"readv2"},{"code":"31790.0","system":"readv2"},{"code":"24571.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetic-neurological-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["complications---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["complications---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["complications---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
