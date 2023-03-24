import json
import os
import pandas as pd

tar_dir = r'E:\Parser_Test'

def json_to_csv(data):

    data['contacts'] = json.dumps(data['contacts'],indent=4,ensure_ascii=False)
    data['currentLocation'] = json.dumps(data['currentLocation'],indent=4,ensure_ascii=False)
    data['preferredLocations'] = json.dumps(data['preferredLocations'],indent=4,ensure_ascii=False)
    data['languages'] = json.dumps(data['languages'],indent=4,ensure_ascii=False)
    data['educations'] = json.dumps(data['educations'],indent=4,ensure_ascii=False)
    data['experiences'] = json.dumps(data['experiences'],indent=4,ensure_ascii=False)


    table = pd.DataFrame(data, index=[0])

    table.to_csv(os.path.join(tar_dir,'parser_Result.csv'), index= False, mode= 'a',header=False, encoding= 'utf_8_sig',
                 columns= ['fileName','fileType','size','page','start_time','last_update_time','parser_cost_time','firstName','lastName','contacts',
                                            'currentLocation','preferredLocations','languages','skills','educations','experiences'])
    print('------------------------------------')

if __name__ == '__main__':
    data = {
        'c' : '3st column',
        'b' : 'secend column',
        'a' : 'first column'
    }

    json_to_csv(data)