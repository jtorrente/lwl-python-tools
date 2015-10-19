import os

__author__ = 'jtorrente'

def generate_class():
    savedpath = os.getcwd()
    os.chdir(r"D:\Dropbox\UCL\LISTEN WITH LEMUR\Sounds\ListenAppZip")
    voice_file_prefix = ["childs", "fem01", "fem02", "male01"]
    type_file_prefix = ["name", "ono"]

    field_file_prefix = ["CHILD", "FEMALE01", "FEMALE02", "MALE"]
    field_file_prefix2 = ["NAME", "ONOMATOPOEIA"]

    constants = []

    for vfp in voice_file_prefix:
        for tfp in type_file_prefix:
            with open(vfp+"_"+tfp+".txt", 'rb') as f:
                ffp = field_file_prefix[voice_file_prefix.index(vfp)]
                ffp2 = field_file_prefix2[type_file_prefix.index(tfp)]
                for line in f.readlines():
                    constants.append("\tpublic static final String "+ffp+"_"+ffp2+"_ = \""+line.replace(".wav", ".wav\";"))

    with open('Sounds.java', 'wb') as output_f:
        output_f.write("public class Sounds {\n")
        output_f.writelines(constants)
        output_f.write("}")

generate_class()