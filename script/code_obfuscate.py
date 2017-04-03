import os
import re


# @param scripts Array[String] Array of contents of javascripts inside a single webpage
# @return Array[String]  Array of obfuscated javascript codes

def code_obfuscate(scripts):
    retArray = []
    for s in scripts:
        #TODO apply code obfuscate
        obfuscate_result = s
        # obfuscate_result = "aaa"
        retArray.append(obfuscate_result);
    return retArray

if __name__ == '__main__':
    pattern = re.compile(r'<\s*script[^>]*>(.*?)<\s*/\s*script\s*>', re.M | re.S)
    pattern2 = re.compile(r'<\s*script[^>]*>.*?<\s*/\s*script\s*>', re.M | re.S)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    renamed_malware_base = os.path.join(script_dir, '../data/js-malicious-dataset-renamed')
    output_dir_base = os.path.join(script_dir, '../data/obfuscated-output')
    if not os.path.exists(output_dir_base):
        os.mkdir(output_dir_base)

    dir_list = os.listdir(renamed_malware_base)
    for dir_base in dir_list:
        full_dir_base = os.path.join(renamed_malware_base, dir_base)
        full_output_dir_base = os.path.join(output_dir_base, dir_base)
        if not os.path.exists(full_output_dir_base):
            os.mkdir(full_output_dir_base)

        for root, dirs, files in os.walk(full_dir_base):
            for f in files:
                file_full_path = os.path.join(root, f)
                output_file_full_path = os.path.join(full_output_dir_base, f)

                with open(file_full_path) as input_file:
                    content = input_file.read()
                match_results = re.findall(pattern, content)
                match_results_full = re.findall(pattern2, content)

                obfuscate_results = code_obfuscate(match_results)
                obfuscated_content = content

                for i in range(len(match_results)):
                    f = match_results_full[i]
                    if len(match_results[i]) != 0:
                        obf_f = f.replace(match_results[i], obfuscate_results[i])
                        obfuscated_content = obfuscated_content.replace(f, obf_f)

                with open(output_file_full_path, 'w') as output_file:
                    output_file.write(obfuscated_content)
