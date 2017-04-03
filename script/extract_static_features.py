import os
import re


# @param scripts Array[String] Array of contents of javascripts inside a single webpage
# @return Array[Number]  Array of feature values in a single webpage. The features value of more than one
#                          javascripts inside a single webpage should be merged together in to one array
#                          Please record the meaning of every features in https://docs.google.com/spreadsheets/d/1OQ3ae6dfGrREFBgLj0iQDvi_VuwRELjKBtx5G_qsNOs/edit?usp=sharing

def extract_features(scripts):
    #TODO: return features array from static analysis
    return [1, 1, 1]
    pass

if __name__ == '__main__':
    pattern = re.compile(r'<\s*script[^>]*>(.*?)<\s*/\s*script\s*>', re.M | re.S)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    renamed_malware_base = os.path.join(script_dir, '../data/js-malicious-dataset-renamed')

    dir_list = os.listdir(renamed_malware_base)
    for dir_base in dir_list:
        full_dir_base = os.path.join(renamed_malware_base, dir_base)

        for root, dirs, files in os.walk(full_dir_base):
            for f in files:
                file_full_path = os.path.join(root, f)

                with open(file_full_path) as input_file:
                    content = input_file.read()
                match_results = re.findall(pattern, content)
                extract_features(match_results)

