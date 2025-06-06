"""
Copyright 2017 Ryan Wick (rrwick@gmail.com)
https://github.com/rrwick/Porechop

This module contains the class and sequences for known adapters used in Oxford Nanopore library
preparation kits.

This file is part of Porechop. Porechop is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. Porechop is distributed in
the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details. You should have received a copy of the GNU General Public License along with Porechop. If
not, see <http://www.gnu.org/licenses/>.
"""


class Adapter(object):

    def __init__(self, name, start_sequence=None, end_sequence=None, both_ends_sequence=None):
        self.name = name
        self.start_sequence = start_sequence if start_sequence else []
        self.end_sequence = end_sequence if end_sequence else []
        if both_ends_sequence:
            self.start_sequence = both_ends_sequence
            self.end_sequence = both_ends_sequence
        self.best_start_score, self.best_end_score = 0.0, 0.0

    def best_start_or_end_score(self):
        return max(self.best_start_score, self.best_end_score)

    def is_barcode(self):
        return self.name.startswith('Barcode ')

    def barcode_direction(self):
        if '_rev' in self.start_sequence[0]:
            return 'reverse'
        else:
            return 'forward'

    def get_barcode_name(self):
        """
        Gets the barcode name for the output files. We want a concise name, so it looks at all
        options and chooses the shortest.
        """
        possible_names = [self.name]
        if self.start_sequence:
            possible_names.append(self.start_sequence[0])
        if self.end_sequence:
            possible_names.append(self.end_sequence[0])
        barcode_name = sorted(possible_names, key=lambda x: len(x))[0]
        return barcode_name.replace(' ', '_')


# INSTRUCTIONS FOR ADDING CUSTOM ADAPTERS
# ---------------------------------------
# If you need Porechop to remove adapters that aren't included, you can add your own my modifying
# the ADAPTERS list below.
#
# Here is the format for a normal adapter:
#     Adapter('Adapter_set_name',
#             start_sequence=('Start_adapter_name', 'AAAACCCCGGGGTTTTAAAACCCCGGGGTTTT'),
#             end_sequence=('End_adapter_name', 'AACCGGTTAACCGGTTAACCGGTTAACCGGTT'))
#
# You can exclude start_sequence and end_sequence as appropriate.
#
# If you have custom Barcodes, make sure that the adapter set name starts with 'Barcode '. Also,
# remove the existing barcode sequences from this file to avoid conflicts:
#     Adapter('Barcode 1',
#             start_sequence=('Barcode_1_start', 'AAAAAAAACCCCCCCCGGGGGGGGTTTTTTTT'),
#             end_sequence=('Barcode_1_end', 'AAAAAAAACCCCCCCCGGGGGGGGTTTTTTTT')),
#     Adapter('Barcode 2',
#             start_sequence=('Barcode_2_start', 'TTTTTTTTGGGGGGGGCCCCCCCCAAAAAAAA'),
#             end_sequence=('Barcode_2_end', 'TTTTTTTTGGGGGGGGCCCCCCCCAAAAAAAA'))


ADAPTERS = [Adapter('Adapter_set_monkeypox-2500_2_LEFT', start_sequence=('monkeypox-2500_2_LEFT_start', 'TGTTCTACACCCTGATGCTCCT'), end_sequence=('monkeypox-2500_2_LEFT_end', 'AGGAGCATCAGGGTGTAGAACA')),
Adapter('Adapter_set_monkeypox-2500_2_RIGHT', start_sequence=('monkeypox-2500_2_RIGHT_start', 'TCCACCCACCTTTCTTGAAATGA'), end_sequence=('monkeypox-2500_2_RIGHT_end', 'TCATTTCAAGAAAGGTGGGTGGA')),
Adapter('Adapter_set_monkeypox-2500_4_LEFT', start_sequence=('monkeypox-2500_4_LEFT_start', 'GTAGCAGTAGTTGGTGCATGGT'), end_sequence=('monkeypox-2500_4_LEFT_end', 'ACCATGCACCAACTACTGCTAC')),
Adapter('Adapter_set_monkeypox-2500_4_RIGHT', start_sequence=('monkeypox-2500_4_RIGHT_start', 'TGTGTCCTCTCCTCTTATAACATCG'), end_sequence=('monkeypox-2500_4_RIGHT_end', 'CGATGTTATAAGAGGAGAGGACACA')),
Adapter('Adapter_set_monkeypox-2500_6_LEFT', start_sequence=('monkeypox-2500_6_LEFT_start', 'AGCGTTGACTTATGGACTCTGG'), end_sequence=('monkeypox-2500_6_LEFT_end', 'CCAGAGTCCATAAGTCAACGCT')),
Adapter('Adapter_set_monkeypox-2500_6_RIGHT', start_sequence=('monkeypox-2500_6_RIGHT_start', 'TACCTATCCAACGACAGGCACT'), end_sequence=('monkeypox-2500_6_RIGHT_end', 'AGTGCCTGTCGTTGGATAGGTA')),
Adapter('Adapter_set_monkeypox-2500_8_LEFT', start_sequence=('monkeypox-2500_8_LEFT_start', 'TTGCGGACATGTTACACTCCTT'), end_sequence=('monkeypox-2500_8_LEFT_end', 'AAGGAGTGTAACATGTCCGCAA')),
Adapter('Adapter_set_monkeypox-2500_8_RIGHT', start_sequence=('monkeypox-2500_8_RIGHT_start', 'ACTATGGATCCCCACCACTTGA'), end_sequence=('monkeypox-2500_8_RIGHT_end', 'TCAAGTGGTGGGGATCCATAGT')),
Adapter('Adapter_set_monkeypox-2500_10_LEFT', start_sequence=('monkeypox-2500_10_LEFT_start', 'TCGCCGTCATTTCTCCAAAGAA'), end_sequence=('monkeypox-2500_10_LEFT_end', 'TTCTTTGGAGAAATGACGGCGA')),
Adapter('Adapter_set_monkeypox-2500_10_RIGHT', start_sequence=('monkeypox-2500_10_RIGHT_start', 'TCTGTTGTTTACCACTCAGCGG'), end_sequence=('monkeypox-2500_10_RIGHT_end', 'CCGCTGAGTGGTAAACAACAGA')),
Adapter('Adapter_set_monkeypox-2500_12_LEFT', start_sequence=('monkeypox-2500_12_LEFT_start', 'GGAACCGTTTTCGTACCGTACT'), end_sequence=('monkeypox-2500_12_LEFT_end', 'AGTACGGTACGAAAACGGTTCC')),
Adapter('Adapter_set_monkeypox-2500_12_RIGHT', start_sequence=('monkeypox-2500_12_RIGHT_start', 'AGTCAGGTCTTGAAGGCTACCA'), end_sequence=('monkeypox-2500_12_RIGHT_end', 'TGGTAGCCTTCAAGACCTGACT')),
Adapter('Adapter_set_monkeypox-2500_14_LEFT', start_sequence=('monkeypox-2500_14_LEFT_start', 'TGATCCAAACCCTTGATCTCCTC'), end_sequence=('monkeypox-2500_14_LEFT_end', 'GAGGAGATCAAGGGTTTGGATCA')),
Adapter('Adapter_set_monkeypox-2500_14_RIGHT', start_sequence=('monkeypox-2500_14_RIGHT_start', 'ACGGATTTCAGATGGCCATTGA'), end_sequence=('monkeypox-2500_14_RIGHT_end', 'TCAATGGCCATCTGAAATCCGT')),
Adapter('Adapter_set_monkeypox-2500_16_LEFT', start_sequence=('monkeypox-2500_16_LEFT_start', 'GGCTGCTCCTGTTCTTGTAGTC'), end_sequence=('monkeypox-2500_16_LEFT_end', 'GACTACAAGAACAGGAGCAGCC')),
Adapter('Adapter_set_monkeypox-2500_16_RIGHT', start_sequence=('monkeypox-2500_16_RIGHT_start', 'GATAACGCCAAAATCGCTGCTC'), end_sequence=('monkeypox-2500_16_RIGHT_end', 'GAGCAGCGATTTTGGCGTTATC')),
Adapter('Adapter_set_monkeypox-2500_18_LEFT', start_sequence=('monkeypox-2500_18_LEFT_start', 'AAATTCGCGCCCACAATTCATC'), end_sequence=('monkeypox-2500_18_LEFT_end', 'GATGAATTGTGGGCGCGAATTT')),
Adapter('Adapter_set_monkeypox-2500_18_RIGHT', start_sequence=('monkeypox-2500_18_RIGHT_start', 'TCGCCGTTTCATTTTCAACAGC'), end_sequence=('monkeypox-2500_18_RIGHT_end', 'GCTGTTGAAAATGAAACGGCGA')),
Adapter('Adapter_set_monkeypox-2500_20_LEFT', start_sequence=('monkeypox-2500_20_LEFT_start', 'AGAAATGCCAAATCTATAAGAAAAGTCCT'), end_sequence=('monkeypox-2500_20_LEFT_end', 'AGGACTTTTCTTATAGATTTGGCATTTCT')),
Adapter('Adapter_set_monkeypox-2500_20_RIGHT', start_sequence=('monkeypox-2500_20_RIGHT_start', 'CCTTTATCAACAAGGAAAGCGTGT'), end_sequence=('monkeypox-2500_20_RIGHT_end', 'ACACGCTTTCCTTGTTGATAAAGG')),
Adapter('Adapter_set_monkeypox-2500_22_LEFT', start_sequence=('monkeypox-2500_22_LEFT_start', 'TCGTATTGTGGTTATATGGCTACAATT'), end_sequence=('monkeypox-2500_22_LEFT_end', 'AATTGTAGCCATATAACCACAATACGA')),
Adapter('Adapter_set_monkeypox-2500_22_RIGHT', start_sequence=('monkeypox-2500_22_RIGHT_start', 'TGAATTGTTGCAACGGTTTCCA'), end_sequence=('monkeypox-2500_22_RIGHT_end', 'TGGAAACCGTTGCAACAATTCA')),
Adapter('Adapter_set_monkeypox-2500_24_LEFT', start_sequence=('monkeypox-2500_24_LEFT_start', 'TCAGTCGTTCTAACTCCTTTGCT'), end_sequence=('monkeypox-2500_24_LEFT_end', 'AGCAAAGGAGTTAGAACGACTGA')),
Adapter('Adapter_set_monkeypox-2500_24_RIGHT', start_sequence=('monkeypox-2500_24_RIGHT_start', 'CACGCTTCTATGTTGCCGTCTA'), end_sequence=('monkeypox-2500_24_RIGHT_end', 'TAGACGGCAACATAGAAGCGTG')),
Adapter('Adapter_set_monkeypox-2500_26_LEFT', start_sequence=('monkeypox-2500_26_LEFT_start', 'AGACAGAATATCGTGAACAGGTGG'), end_sequence=('monkeypox-2500_26_LEFT_end', 'CCACCTGTTCACGATATTCTGTCT')),
Adapter('Adapter_set_monkeypox-2500_26_RIGHT', start_sequence=('monkeypox-2500_26_RIGHT_start', 'TGTTTCGACTGGAGAATCATCCA'), end_sequence=('monkeypox-2500_26_RIGHT_end', 'TGGATGATTCTCCAGTCGAAACA')),
Adapter('Adapter_set_monkeypox-2500_28_LEFT', start_sequence=('monkeypox-2500_28_LEFT_start', 'TAACTCCAGGCCGTTTGTTTCC'), end_sequence=('monkeypox-2500_28_LEFT_end', 'GGAAACAAACGGCCTGGAGTTA')),
Adapter('Adapter_set_monkeypox-2500_28_RIGHT', start_sequence=('monkeypox-2500_28_RIGHT_start', 'TTGTGTACCAGAACTCCACCTAAA'), end_sequence=('monkeypox-2500_28_RIGHT_end', 'TTTAGGTGGAGTTCTGGTACACAA')),
Adapter('Adapter_set_monkeypox-2500_30_LEFT', start_sequence=('monkeypox-2500_30_LEFT_start', 'CTGCCACGTTAGAGGATGACAG'), end_sequence=('monkeypox-2500_30_LEFT_end', 'CTGTCATCCTCTAACGTGGCAG')),
Adapter('Adapter_set_monkeypox-2500_30_RIGHT', start_sequence=('monkeypox-2500_30_RIGHT_start', 'ACTAACGTTTCTTAGCGGAGGC'), end_sequence=('monkeypox-2500_30_RIGHT_end', 'GCCTCCGCTAAGAAACGTTAGT')),
Adapter('Adapter_set_monkeypox-2500_32_LEFT', start_sequence=('monkeypox-2500_32_LEFT_start', 'CAAGACGTTAGAGACAAGAGACGT'), end_sequence=('monkeypox-2500_32_LEFT_end', 'ACGTCTCTTGTCTCTAACGTCTTG')),
Adapter('Adapter_set_monkeypox-2500_32_RIGHT', start_sequence=('monkeypox-2500_32_RIGHT_start', 'CAACGCCACAGATTTCTGGAGA'), end_sequence=('monkeypox-2500_32_RIGHT_end', 'TCTCCAGAAATCTGTGGCGTTG')),
Adapter('Adapter_set_monkeypox-2500_34_LEFT', start_sequence=('monkeypox-2500_34_LEFT_start', 'GCTATTTAAATGGGTGCCGCAG'), end_sequence=('monkeypox-2500_34_LEFT_end', 'CTGCGGCACCCATTTAAATAGC')),
Adapter('Adapter_set_monkeypox-2500_34_RIGHT', start_sequence=('monkeypox-2500_34_RIGHT_start', 'GGTGATGATCCTTGACGGAAGA'), end_sequence=('monkeypox-2500_34_RIGHT_end', 'TCTTCCGTCAAGGATCATCACC')),
Adapter('Adapter_set_monkeypox-2500_36_LEFT', start_sequence=('monkeypox-2500_36_LEFT_start', 'GGCCGCCATCATGATCCTATTC'), end_sequence=('monkeypox-2500_36_LEFT_end', 'GAATAGGATCATGATGGCGGCC')),
Adapter('Adapter_set_monkeypox-2500_36_RIGHT', start_sequence=('monkeypox-2500_36_RIGHT_start', 'TTACCGCCTTCTGGATAACCTG'), end_sequence=('monkeypox-2500_36_RIGHT_end', 'CAGGTTATCCAGAAGGCGGTAA')),
Adapter('Adapter_set_monkeypox-2500_38_LEFT', start_sequence=('monkeypox-2500_38_LEFT_start', 'AGGTGGTGGAACTCCTATTGGA'), end_sequence=('monkeypox-2500_38_LEFT_end', 'TCCAATAGGAGTTCCACCACCT')),
Adapter('Adapter_set_monkeypox-2500_38_RIGHT', start_sequence=('monkeypox-2500_38_RIGHT_start', 'CACCGCTTCGAAACCATGAAAC'), end_sequence=('monkeypox-2500_38_RIGHT_end', 'GTTTCATGGTTTCGAAGCGGTG')),
Adapter('Adapter_set_monkeypox-2500_40_LEFT', start_sequence=('monkeypox-2500_40_LEFT_start', 'TCACGTCAGCGGCATCTAAATT'), end_sequence=('monkeypox-2500_40_LEFT_end', 'AATTTAGATGCCGCTGACGTGA')),
Adapter('Adapter_set_monkeypox-2500_40_RIGHT', start_sequence=('monkeypox-2500_40_RIGHT_start', 'TTCATGTGAAACTTTGTCCTTTCCT'), end_sequence=('monkeypox-2500_40_RIGHT_end', 'AGGAAAGGACAAAGTTTCACATGAA')),
Adapter('Adapter_set_monkeypox-2500_42_LEFT', start_sequence=('monkeypox-2500_42_LEFT_start', 'AGCCCGTAAATGCAATCAGTGA'), end_sequence=('monkeypox-2500_42_LEFT_end', 'TCACTGATTGCATTTACGGGCT')),
Adapter('Adapter_set_monkeypox-2500_42_RIGHT', start_sequence=('monkeypox-2500_42_RIGHT_start', 'GCCGTTAAACCAAGCGAATACA'), end_sequence=('monkeypox-2500_42_RIGHT_end', 'TGTATTCGCTTGGTTTAACGGC')),
Adapter('Adapter_set_monkeypox-2500_44_LEFT', start_sequence=('monkeypox-2500_44_LEFT_start', 'ACGTGTACTGTATCGACCGGAT'), end_sequence=('monkeypox-2500_44_LEFT_end', 'ATCCGGTCGATACAGTACACGT')),
Adapter('Adapter_set_monkeypox-2500_44_RIGHT', start_sequence=('monkeypox-2500_44_RIGHT_start', 'ACGGGTTCAGAAATATCGACGT'), end_sequence=('monkeypox-2500_44_RIGHT_end', 'ACGTCGATATTTCTGAACCCGT')),
Adapter('Adapter_set_monkeypox-2500_46_LEFT', start_sequence=('monkeypox-2500_46_LEFT_start', 'CCAAGATCAAAAGACACGCACG'), end_sequence=('monkeypox-2500_46_LEFT_end', 'CGTGCGTGTCTTTTGATCTTGG')),
Adapter('Adapter_set_monkeypox-2500_46_RIGHT', start_sequence=('monkeypox-2500_46_RIGHT_start', 'TTGATGATGTGGAAGGGTCTGC'), end_sequence=('monkeypox-2500_46_RIGHT_end', 'GCAGACCCTTCCACATCATCAA')),
Adapter('Adapter_set_monkeypox-2500_48_LEFT', start_sequence=('monkeypox-2500_48_LEFT_start', 'AGATGGGCCCGTTCTCTGAATA'), end_sequence=('monkeypox-2500_48_LEFT_end', 'TATTCAGAGAACGGGCCCATCT')),
Adapter('Adapter_set_monkeypox-2500_48_RIGHT', start_sequence=('monkeypox-2500_48_RIGHT_start', 'TGTAGCTGTTGTAGACATAACGGTA'), end_sequence=('monkeypox-2500_48_RIGHT_end', 'TACCGTTATGTCTACAACAGCTACA')),
Adapter('Adapter_set_monkeypox-2500_50_LEFT', start_sequence=('monkeypox-2500_50_LEFT_start', 'GCTACTTCGTCGATGGAAACCA'), end_sequence=('monkeypox-2500_50_LEFT_end', 'TGGTTTCCATCGACGAAGTAGC')),
Adapter('Adapter_set_monkeypox-2500_50_RIGHT', start_sequence=('monkeypox-2500_50_RIGHT_start', 'TCCTTAAATCTGGTGCCGTTGT'), end_sequence=('monkeypox-2500_50_RIGHT_end', 'ACAACGGCACCAGATTTAAGGA')),
Adapter('Adapter_set_monkeypox-2500_52_LEFT', start_sequence=('monkeypox-2500_52_LEFT_start', 'AACCAAAAAGTCACACGCTCCA'), end_sequence=('monkeypox-2500_52_LEFT_end', 'TGGAGCGTGTGACTTTTTGGTT')),
Adapter('Adapter_set_monkeypox-2500_52_RIGHT', start_sequence=('monkeypox-2500_52_RIGHT_start', 'TTCTATGCAGGATCTCCCGAAG'), end_sequence=('monkeypox-2500_52_RIGHT_end', 'CTTCGGGAGATCCTGCATAGAA')),
Adapter('Adapter_set_monkeypox-2500_54_LEFT', start_sequence=('monkeypox-2500_54_LEFT_start', 'GAGAACATAATGCCGCCGTAGT'), end_sequence=('monkeypox-2500_54_LEFT_end', 'ACTACGGCGGCATTATGTTCTC')),
Adapter('Adapter_set_monkeypox-2500_54_RIGHT', start_sequence=('monkeypox-2500_54_RIGHT_start', 'TGACGTACATCCAGGAGAACCT'), end_sequence=('monkeypox-2500_54_RIGHT_end', 'AGGTTCTCCTGGATGTACGTCA')),
Adapter('Adapter_set_monkeypox-2500_56_LEFT', start_sequence=('monkeypox-2500_56_LEFT_start', 'CACACACGGCAGAAAAACCATC'), end_sequence=('monkeypox-2500_56_LEFT_end', 'GATGGTTTTTCTGCCGTGTGTG')),
Adapter('Adapter_set_monkeypox-2500_56_RIGHT', start_sequence=('monkeypox-2500_56_RIGHT_start', 'GTTCCGTTCCCATCATAGTCGT'), end_sequence=('monkeypox-2500_56_RIGHT_end', 'ACGACTATGATGGGAACGGAAC')),
Adapter('Adapter_set_monkeypox-2500_58_LEFT', start_sequence=('monkeypox-2500_58_LEFT_start', 'GAAACGGAATCGGTAGATCGTCT'), end_sequence=('monkeypox-2500_58_LEFT_end', 'AGACGATCTACCGATTCCGTTTC')),
Adapter('Adapter_set_monkeypox-2500_58_RIGHT', start_sequence=('monkeypox-2500_58_RIGHT_start', 'CATAGCGTCTCCGGATTCCAAG'), end_sequence=('monkeypox-2500_58_RIGHT_end', 'CTTGGAATCCGGAGACGCTATG')),
Adapter('Adapter_set_monkeypox-2500_60_LEFT', start_sequence=('monkeypox-2500_60_LEFT_start', 'ACTCGACGAGCTCACGTTTAAG'), end_sequence=('monkeypox-2500_60_LEFT_end', 'CTTAAACGTGAGCTCGTCGAGT')),
Adapter('Adapter_set_monkeypox-2500_60_RIGHT', start_sequence=('monkeypox-2500_60_RIGHT_start', 'GTTCGACGATTAACGGAGAGCA'), end_sequence=('monkeypox-2500_60_RIGHT_end', 'TGCTCTCCGTTAATCGTCGAAC')),
Adapter('Adapter_set_monkeypox-2500_62_LEFT', start_sequence=('monkeypox-2500_62_LEFT_start', 'GCTTCGCGTTTAGTCTCTGGAT'), end_sequence=('monkeypox-2500_62_LEFT_end', 'ATCCAGAGACTAAACGCGAAGC')),
Adapter('Adapter_set_monkeypox-2500_62_RIGHT', start_sequence=('monkeypox-2500_62_RIGHT_start', 'TCGATGCCTGTAAAGGGGAAAC'), end_sequence=('monkeypox-2500_62_RIGHT_end', 'GTTTCCCCTTTACAGGCATCGA')),
Adapter('Adapter_set_monkeypox-2500_64_LEFT', start_sequence=('monkeypox-2500_64_LEFT_start', 'ACCATCATCATAGCATGCGACT'), end_sequence=('monkeypox-2500_64_LEFT_end', 'AGTCGCATGCTATGATGATGGT')),
Adapter('Adapter_set_monkeypox-2500_64_RIGHT', start_sequence=('monkeypox-2500_64_RIGHT_start', 'GTGTTTGGTTGCGTTATTGCCA'), end_sequence=('monkeypox-2500_64_RIGHT_end', 'TGGCAATAACGCAACCAAACAC')),
Adapter('Adapter_set_monkeypox-2500_66_LEFT', start_sequence=('monkeypox-2500_66_LEFT_start', 'TAATAAGTTCGAGGATGCCGCC'), end_sequence=('monkeypox-2500_66_LEFT_end', 'GGCGGCATCCTCGAACTTATTA')),
Adapter('Adapter_set_monkeypox-2500_66_RIGHT', start_sequence=('monkeypox-2500_66_RIGHT_start', 'TTTTCCATGGACTTGTTCAACGT'), end_sequence=('monkeypox-2500_66_RIGHT_end', 'ACGTTGAACAAGTCCATGGAAAA')),
Adapter('Adapter_set_monkeypox-2500_68_LEFT', start_sequence=('monkeypox-2500_68_LEFT_start', 'ATGTCTCGTGGGGCATTAATCG'), end_sequence=('monkeypox-2500_68_LEFT_end', 'CGATTAATGCCCCACGAGACAT')),
Adapter('Adapter_set_monkeypox-2500_68_RIGHT', start_sequence=('monkeypox-2500_68_RIGHT_start', 'ACCGGATTCATCGTCGTAACAA'), end_sequence=('monkeypox-2500_68_RIGHT_end', 'TTGTTACGACGATGAATCCGGT')),
Adapter('Adapter_set_monkeypox-2500_70_LEFT', start_sequence=('monkeypox-2500_70_LEFT_start', 'AGACTAGTGTATGTGGAAATGTCATAGA'), end_sequence=('monkeypox-2500_70_LEFT_end', 'TCTATGACATTTCCACATACACTAGTCT')),
Adapter('Adapter_set_monkeypox-2500_70_RIGHT', start_sequence=('monkeypox-2500_70_RIGHT_start', 'TCGGATTATAGCTAAGGACTAGATTCG'), end_sequence=('monkeypox-2500_70_RIGHT_end', 'CGAATCTAGTCCTTAGCTATAATCCGA')),
Adapter('Adapter_set_monkeypox-2500_72_LEFT', start_sequence=('monkeypox-2500_72_LEFT_start', 'GCAAAAATCAATGGGTCGTTGGAC'), end_sequence=('monkeypox-2500_72_LEFT_end', 'GTCCAACGACCCATTGATTTTTGC')),
Adapter('Adapter_set_monkeypox-2500_72_RIGHT', start_sequence=('monkeypox-2500_72_RIGHT_start', 'GTGACACCCATTCATCTGGAGA'), end_sequence=('monkeypox-2500_72_RIGHT_end', 'TCTCCAGATGAATGGGTGTCAC')),
Adapter('Adapter_set_monkeypox-2500_74_LEFT', start_sequence=('monkeypox-2500_74_LEFT_start', 'TCCTTTTAGTGCTCGACAGTGT'), end_sequence=('monkeypox-2500_74_LEFT_end', 'ACACTGTCGAGCACTAAAAGGA')),
Adapter('Adapter_set_monkeypox-2500_74_RIGHT', start_sequence=('monkeypox-2500_74_RIGHT_start', 'ACATTGTTTGCCACGTCTTGAT'), end_sequence=('monkeypox-2500_74_RIGHT_end', 'ATCAAGACGTGGCAAACAATGT')),
Adapter('Adapter_set_monkeypox-2500_76_LEFT', start_sequence=('monkeypox-2500_76_LEFT_start', 'TCTTCCGATATCTACAAGGATATTCCA'), end_sequence=('monkeypox-2500_76_LEFT_end', 'TGGAATATCCTTGTAGATATCGGAAGA')),
Adapter('Adapter_set_monkeypox-2500_76_RIGHT', start_sequence=('monkeypox-2500_76_RIGHT_start', 'ACGGATGATCTGCACAGAACTC'), end_sequence=('monkeypox-2500_76_RIGHT_end', 'GAGTTCTGTGCAGATCATCCGT')),
Adapter('Adapter_set_monkeypox-2500_78_LEFT', start_sequence=('monkeypox-2500_78_LEFT_start', 'CTCATGTTCTTGTGTAATCGCAGT'), end_sequence=('monkeypox-2500_78_LEFT_end', 'ACTGCGATTACACAAGAACATGAG')),
Adapter('Adapter_set_monkeypox-2500_78_RIGHT', start_sequence=('monkeypox-2500_78_RIGHT_start', 'TGTTCTGCGTCATCTACATCTGA'), end_sequence=('monkeypox-2500_78_RIGHT_end', 'TCAGATGTAGATGACGCAGAACA')),
Adapter('Adapter_set_monkeypox-2500_80_LEFT', start_sequence=('monkeypox-2500_80_LEFT_start', 'AGCGAGAGATCTAGCAACTAGAGT'), end_sequence=('monkeypox-2500_80_LEFT_end', 'ACTCTAGTTGCTAGATCTCTCGCT')),
Adapter('Adapter_set_monkeypox-2500_80_RIGHT', start_sequence=('monkeypox-2500_80_RIGHT_start', 'TCGAGTCATTTTACGCACGGTT'), end_sequence=('monkeypox-2500_80_RIGHT_end', 'AACCGTGCGTAAAATGACTCGA')),
Adapter('Adapter_set_monkeypox-2500_82_LEFT', start_sequence=('monkeypox-2500_82_LEFT_start', 'GCTCAATCTGCCAGGATCAAGT'), end_sequence=('monkeypox-2500_82_LEFT_end', 'ACTTGATCCTGGCAGATTGAGC')),
Adapter('Adapter_set_monkeypox-2500_82_RIGHT', start_sequence=('monkeypox-2500_82_RIGHT_start', 'TCAATGGAGCAGGAAAATGGGT'), end_sequence=('monkeypox-2500_82_RIGHT_end', 'ACCCATTTTCCTGCTCCATTGA')),
Adapter('Adapter_set_monkeypox-2500_84_LEFT', start_sequence=('monkeypox-2500_84_LEFT_start', 'GACCTCACAACACAGTGCAAGA'), end_sequence=('monkeypox-2500_84_LEFT_end', 'TCTTGCACTGTGTTGTGAGGTC')),
Adapter('Adapter_set_monkeypox-2500_84_RIGHT', start_sequence=('monkeypox-2500_84_RIGHT_start', 'CCAGCTAACATAAGAGCCAATCTCA'), end_sequence=('monkeypox-2500_84_RIGHT_end', 'TGAGATTGGCTCTTATGTTAGCTGG')),
Adapter('Adapter_set_monkeypox-2500_86_LEFT', start_sequence=('monkeypox-2500_86_LEFT_start', 'AAAACCATGATGTGATAAAGCTCTGT'), end_sequence=('monkeypox-2500_86_LEFT_end', 'ACAGAGCTTTATCACATCATGGTTTT')),
Adapter('Adapter_set_monkeypox-2500_86_RIGHT', start_sequence=('monkeypox-2500_86_RIGHT_start', 'CCATTGGATGGTGCATGTGGT'), end_sequence=('monkeypox-2500_86_RIGHT_end', 'ACCACATGCACCATCCAATGG')),
Adapter('Adapter_set_monkeypox-2500_88_LEFT', start_sequence=('monkeypox-2500_88_LEFT_start', 'CCGGGAACTTACGCTTTCAGAT'), end_sequence=('monkeypox-2500_88_LEFT_end', 'ATCTGAAAGCGTAAGTTCCCGG')),
Adapter('Adapter_set_monkeypox-2500_88_RIGHT', start_sequence=('monkeypox-2500_88_RIGHT_start', 'AAAAATGTGTGACCCACGACCG'), end_sequence=('monkeypox-2500_88_RIGHT_end', 'CGGTCGTGGGTCACACATTTTT')),
Adapter('Adapter_set_monkeypox-2500_1_LEFT', start_sequence=('monkeypox-2500_1_LEFT_start', 'AAAAATGTGTGACCCACGACCG'), end_sequence=('monkeypox-2500_1_LEFT_end', 'CGGTCGTGGGTCACACATTTTT')),
Adapter('Adapter_set_monkeypox-2500_1_RIGHT', start_sequence=('monkeypox-2500_1_RIGHT_start', 'CCGGGAACTTACGCTTTCAGAT'), end_sequence=('monkeypox-2500_1_RIGHT_end', 'ATCTGAAAGCGTAAGTTCCCGG')),
Adapter('Adapter_set_monkeypox-2500_3_LEFT', start_sequence=('monkeypox-2500_3_LEFT_start', 'GTTAACGATGCGCACAATCTCG'), end_sequence=('monkeypox-2500_3_LEFT_end', 'CGAGATTGTGCGCATCGTTAAC')),
Adapter('Adapter_set_monkeypox-2500_3_RIGHT', start_sequence=('monkeypox-2500_3_RIGHT_start', 'TAGTGAGAGCGAGAGTGACAGT'), end_sequence=('monkeypox-2500_3_RIGHT_end', 'ACTGTCACTCTCGCTCTCACTA')),
Adapter('Adapter_set_monkeypox-2500_5_LEFT', start_sequence=('monkeypox-2500_5_LEFT_start', 'AATAGTCTGTAGACCTTTATCGTCGT'), end_sequence=('monkeypox-2500_5_LEFT_end', 'ACGACGATAAAGGTCTACAGACTATT')),
Adapter('Adapter_set_monkeypox-2500_5_RIGHT', start_sequence=('monkeypox-2500_5_RIGHT_start', 'ACTGCTAGAATCCGGTTCAGATG'), end_sequence=('monkeypox-2500_5_RIGHT_end', 'CATCTGAACCGGATTCTAGCAGT')),
Adapter('Adapter_set_monkeypox-2500_7_LEFT', start_sequence=('monkeypox-2500_7_LEFT_start', 'CACTGTAAGCATGTCCGTACCA'), end_sequence=('monkeypox-2500_7_LEFT_end', 'TGGTACGGACATGCTTACAGTG')),
Adapter('Adapter_set_monkeypox-2500_7_RIGHT', start_sequence=('monkeypox-2500_7_RIGHT_start', 'TGAGAACGAGCTCTTCAAACACT'), end_sequence=('monkeypox-2500_7_RIGHT_end', 'AGTGTTTGAAGAGCTCGTTCTCA')),
Adapter('Adapter_set_monkeypox-2500_9_LEFT', start_sequence=('monkeypox-2500_9_LEFT_start', 'AGGCTATGTTTCGCCCATCATC'), end_sequence=('monkeypox-2500_9_LEFT_end', 'GATGATGGGCGAAACATAGCCT')),
Adapter('Adapter_set_monkeypox-2500_9_RIGHT', start_sequence=('monkeypox-2500_9_RIGHT_start', 'GTCCTTTACGATGAGCTCAAATGT'), end_sequence=('monkeypox-2500_9_RIGHT_end', 'ACATTTGAGCTCATCGTAAAGGAC')),
Adapter('Adapter_set_monkeypox-2500_11_LEFT', start_sequence=('monkeypox-2500_11_LEFT_start', 'TGTCACTCCATAACTACCACGC'), end_sequence=('monkeypox-2500_11_LEFT_end', 'GCGTGGTAGTTATGGAGTGACA')),
Adapter('Adapter_set_monkeypox-2500_11_RIGHT', start_sequence=('monkeypox-2500_11_RIGHT_start', 'AGTTTCGTCGATAGTACTGTGTGT'), end_sequence=('monkeypox-2500_11_RIGHT_end', 'ACACACAGTACTATCGACGAAACT')),
Adapter('Adapter_set_monkeypox-2500_13_LEFT', start_sequence=('monkeypox-2500_13_LEFT_start', 'TCCTTATGAAGATGATGTTTGGCG'), end_sequence=('monkeypox-2500_13_LEFT_end', 'CGCCAAACATCATCTTCATAAGGA')),
Adapter('Adapter_set_monkeypox-2500_13_RIGHT', start_sequence=('monkeypox-2500_13_RIGHT_start', 'CCCTCCTGGAGAACGACAGTTA'), end_sequence=('monkeypox-2500_13_RIGHT_end', 'TAACTGTCGTTCTCCAGGAGGG')),
Adapter('Adapter_set_monkeypox-2500_15_LEFT', start_sequence=('monkeypox-2500_15_LEFT_start', 'TGGAAGCGAATGATCCGGAAAA'), end_sequence=('monkeypox-2500_15_LEFT_end', 'TTTTCCGGATCATTCGCTTCCA')),
Adapter('Adapter_set_monkeypox-2500_15_RIGHT', start_sequence=('monkeypox-2500_15_RIGHT_start', 'TCCGTGGTTTCTAGTGGGTGTA'), end_sequence=('monkeypox-2500_15_RIGHT_end', 'TACACCCACTAGAAACCACGGA')),
Adapter('Adapter_set_monkeypox-2500_17_LEFT', start_sequence=('monkeypox-2500_17_LEFT_start', 'ACCTTGGCTGTCTCATTCAATAGG'), end_sequence=('monkeypox-2500_17_LEFT_end', 'CCTATTGAATGAGACAGCCAAGGT')),
Adapter('Adapter_set_monkeypox-2500_17_RIGHT', start_sequence=('monkeypox-2500_17_RIGHT_start', 'TGAATGGCTGTCGTCAAAAGGT'), end_sequence=('monkeypox-2500_17_RIGHT_end', 'ACCTTTTGACGACAGCCATTCA')),
Adapter('Adapter_set_monkeypox-2500_19_LEFT', start_sequence=('monkeypox-2500_19_LEFT_start', 'AGGCTTCCAAAAATTTTTCATCCGT'), end_sequence=('monkeypox-2500_19_LEFT_end', 'ACGGATGAAAAATTTTTGGAAGCCT')),
Adapter('Adapter_set_monkeypox-2500_19_RIGHT', start_sequence=('monkeypox-2500_19_RIGHT_start', 'ACGTCGCTGTAATAGACAAGGC'), end_sequence=('monkeypox-2500_19_RIGHT_end', 'GCCTTGTCTATTACAGCGACGT')),
Adapter('Adapter_set_monkeypox-2500_21_LEFT', start_sequence=('monkeypox-2500_21_LEFT_start', 'CCCTAGGACGAACTACTGCCAT'), end_sequence=('monkeypox-2500_21_LEFT_end', 'ATGGCAGTAGTTCGTCCTAGGG')),
Adapter('Adapter_set_monkeypox-2500_21_RIGHT', start_sequence=('monkeypox-2500_21_RIGHT_start', 'TTGTGCTGCTCTTATCGTCTGA'), end_sequence=('monkeypox-2500_21_RIGHT_end', 'TCAGACGATAAGAGCAGCACAA')),
Adapter('Adapter_set_monkeypox-2500_23_LEFT', start_sequence=('monkeypox-2500_23_LEFT_start', 'AAAAACCCTAGTATTCTTCCATCGC'), end_sequence=('monkeypox-2500_23_LEFT_end', 'GCGATGGAAGAATACTAGGGTTTTT')),
Adapter('Adapter_set_monkeypox-2500_23_RIGHT', start_sequence=('monkeypox-2500_23_RIGHT_start', 'AACGGTATGTTACGGTTTGCCA'), end_sequence=('monkeypox-2500_23_RIGHT_end', 'TGGCAAACCGTAACATACCGTT')),
Adapter('Adapter_set_monkeypox-2500_25_LEFT', start_sequence=('monkeypox-2500_25_LEFT_start', 'CTCGCCATTTCGACATCTGGAT'), end_sequence=('monkeypox-2500_25_LEFT_end', 'ATCCAGATGTCGAAATGGCGAG')),
Adapter('Adapter_set_monkeypox-2500_25_RIGHT', start_sequence=('monkeypox-2500_25_RIGHT_start', 'CGGGACCAAATGTAGTCAAGCT'), end_sequence=('monkeypox-2500_25_RIGHT_end', 'AGCTTGACTACATTTGGTCCCG')),
Adapter('Adapter_set_monkeypox-2500_27_LEFT', start_sequence=('monkeypox-2500_27_LEFT_start', 'ACGCGTTCACTATCTCCAGAGA'), end_sequence=('monkeypox-2500_27_LEFT_end', 'TCTCTGGAGATAGTGAACGCGT')),
Adapter('Adapter_set_monkeypox-2500_27_RIGHT', start_sequence=('monkeypox-2500_27_RIGHT_start', 'TACGCACGCTTCTCCTACCTTA'), end_sequence=('monkeypox-2500_27_RIGHT_end', 'TAAGGTAGGAGAAGCGTGCGTA')),
Adapter('Adapter_set_monkeypox-2500_29_LEFT', start_sequence=('monkeypox-2500_29_LEFT_start', 'TTGACTTTTTGGTCCACTTTTCCA'), end_sequence=('monkeypox-2500_29_LEFT_end', 'TGGAAAAGTGGACCAAAAAGTCAA')),
Adapter('Adapter_set_monkeypox-2500_29_RIGHT', start_sequence=('monkeypox-2500_29_RIGHT_start', 'ATATTCGTGACACTGTGCAACG'), end_sequence=('monkeypox-2500_29_RIGHT_end', 'CGTTGCACAGTGTCACGAATAT')),
Adapter('Adapter_set_monkeypox-2500_31_LEFT', start_sequence=('monkeypox-2500_31_LEFT_start', 'TCCGGACATGATGGTAAAGACC'), end_sequence=('monkeypox-2500_31_LEFT_end', 'GGTCTTTACCATCATGTCCGGA')),
Adapter('Adapter_set_monkeypox-2500_31_RIGHT', start_sequence=('monkeypox-2500_31_RIGHT_start', 'AACGAATTCTGCGTCTCGTTCA'), end_sequence=('monkeypox-2500_31_RIGHT_end', 'TGAACGAGACGCAGAATTCGTT')),
Adapter('Adapter_set_monkeypox-2500_33_LEFT', start_sequence=('monkeypox-2500_33_LEFT_start', 'TAGGCTCACCGATGATCATTGG'), end_sequence=('monkeypox-2500_33_LEFT_end', 'CCAATGATCATCGGTGAGCCTA')),
Adapter('Adapter_set_monkeypox-2500_33_RIGHT', start_sequence=('monkeypox-2500_33_RIGHT_start', 'AACACAGCATCCAACTGAGCAT'), end_sequence=('monkeypox-2500_33_RIGHT_end', 'ATGCTCAGTTGGATGCTGTGTT')),
Adapter('Adapter_set_monkeypox-2500_35_LEFT', start_sequence=('monkeypox-2500_35_LEFT_start', 'ACAGGGGCAATGTTTACCACAA'), end_sequence=('monkeypox-2500_35_LEFT_end', 'TTGTGGTAAACATTGCCCCTGT')),
Adapter('Adapter_set_monkeypox-2500_35_RIGHT', start_sequence=('monkeypox-2500_35_RIGHT_start', 'CTAGACGCCACGGGGTTTAAAA'), end_sequence=('monkeypox-2500_35_RIGHT_end', 'TTTTAAACCCCGTGGCGTCTAG')),
Adapter('Adapter_set_monkeypox-2500_37_LEFT', start_sequence=('monkeypox-2500_37_LEFT_start', 'TTGTTTCGTCAACAAGTTGGATGA'), end_sequence=('monkeypox-2500_37_LEFT_end', 'TCATCCAACTTGTTGACGAAACAA')),
Adapter('Adapter_set_monkeypox-2500_37_RIGHT', start_sequence=('monkeypox-2500_37_RIGHT_start', 'CGGATACCAGAGTGATAATTTCGGT'), end_sequence=('monkeypox-2500_37_RIGHT_end', 'ACCGAAATTATCACTCTGGTATCCG')),
Adapter('Adapter_set_monkeypox-2500_39_LEFT', start_sequence=('monkeypox-2500_39_LEFT_start', 'CCGCATTGGTGTTCCGATCTTA'), end_sequence=('monkeypox-2500_39_LEFT_end', 'TAAGATCGGAACACCAATGCGG')),
Adapter('Adapter_set_monkeypox-2500_39_RIGHT', start_sequence=('monkeypox-2500_39_RIGHT_start', 'TGAACCTGAGGCATGGAAAAGG'), end_sequence=('monkeypox-2500_39_RIGHT_end', 'CCTTTTCCATGCCTCAGGTTCA')),
Adapter('Adapter_set_monkeypox-2500_41_LEFT', start_sequence=('monkeypox-2500_41_LEFT_start', 'CCACAGATTCCAATTATCAGTTGGC'), end_sequence=('monkeypox-2500_41_LEFT_end', 'GCCAACTGATAATTGGAATCTGTGG')),
Adapter('Adapter_set_monkeypox-2500_41_RIGHT', start_sequence=('monkeypox-2500_41_RIGHT_start', 'AGACGACTCTCCAAAGATAATTGGT'), end_sequence=('monkeypox-2500_41_RIGHT_end', 'ACCAATTATCTTTGGAGAGTCGTCT')),
Adapter('Adapter_set_monkeypox-2500_43_LEFT', start_sequence=('monkeypox-2500_43_LEFT_start', 'TGTACAGGTACCTCCATCATTAGGA'), end_sequence=('monkeypox-2500_43_LEFT_end', 'TCCTAATGATGGAGGTACCTGTACA')),
Adapter('Adapter_set_monkeypox-2500_43_RIGHT', start_sequence=('monkeypox-2500_43_RIGHT_start', 'TTGGTTGTCGACTTCCCAGTTG'), end_sequence=('monkeypox-2500_43_RIGHT_end', 'CAACTGGGAAGTCGACAACCAA')),
Adapter('Adapter_set_monkeypox-2500_45_LEFT', start_sequence=('monkeypox-2500_45_LEFT_start', 'TCCTGAAAACGATGATGGCAATC'), end_sequence=('monkeypox-2500_45_LEFT_end', 'GATTGCCATCATCGTTTTCAGGA')),
Adapter('Adapter_set_monkeypox-2500_45_RIGHT', start_sequence=('monkeypox-2500_45_RIGHT_start', 'AACTCTTCGAAGTGAGGATCGAT'), end_sequence=('monkeypox-2500_45_RIGHT_end', 'ATCGATCCTCACTTCGAAGAGTT')),
Adapter('Adapter_set_monkeypox-2500_47_LEFT', start_sequence=('monkeypox-2500_47_LEFT_start', 'CTCCCGGATCACGATTTTGTCT'), end_sequence=('monkeypox-2500_47_LEFT_end', 'AGACAAAATCGTGATCCGGGAG')),
Adapter('Adapter_set_monkeypox-2500_47_RIGHT', start_sequence=('monkeypox-2500_47_RIGHT_start', 'GAACATATAGCGACGCCACCAA'), end_sequence=('monkeypox-2500_47_RIGHT_end', 'TTGGTGGCGTCGCTATATGTTC')),
Adapter('Adapter_set_monkeypox-2500_49_LEFT', start_sequence=('monkeypox-2500_49_LEFT_start', 'TTGCATCTACATCATCCGTGGA'), end_sequence=('monkeypox-2500_49_LEFT_end', 'TCCACGGATGATGTAGATGCAA')),
Adapter('Adapter_set_monkeypox-2500_49_RIGHT', start_sequence=('monkeypox-2500_49_RIGHT_start', 'AATGGAAGCCGTGGTCAATAGC'), end_sequence=('monkeypox-2500_49_RIGHT_end', 'GCTATTGACCACGGCTTCCATT')),
Adapter('Adapter_set_monkeypox-2500_51_LEFT', start_sequence=('monkeypox-2500_51_LEFT_start', 'TCTCTGTAGTCGACGCTCTCAA'), end_sequence=('monkeypox-2500_51_LEFT_end', 'TTGAGAGCGTCGACTACAGAGA')),
Adapter('Adapter_set_monkeypox-2500_51_RIGHT', start_sequence=('monkeypox-2500_51_RIGHT_start', 'ACGGCCGGAAATAGTTAAGAGAC'), end_sequence=('monkeypox-2500_51_RIGHT_end', 'GTCTCTTAACTATTTCCGGCCGT')),
Adapter('Adapter_set_monkeypox-2500_53_LEFT', start_sequence=('monkeypox-2500_53_LEFT_start', 'GTTGTATGGCATTGCGCAGAAA'), end_sequence=('monkeypox-2500_53_LEFT_end', 'TTTCTGCGCAATGCCATACAAC')),
Adapter('Adapter_set_monkeypox-2500_53_RIGHT', start_sequence=('monkeypox-2500_53_RIGHT_start', 'CAAGGATGGTGTTTGTGTTGGC'), end_sequence=('monkeypox-2500_53_RIGHT_end', 'GCCAACACAAACACCATCCTTG')),
Adapter('Adapter_set_monkeypox-2500_55_LEFT', start_sequence=('monkeypox-2500_55_LEFT_start', 'CTGACAATGTACTGGGCCATGT'), end_sequence=('monkeypox-2500_55_LEFT_end', 'ACATGGCCCAGTACATTGTCAG')),
Adapter('Adapter_set_monkeypox-2500_55_RIGHT', start_sequence=('monkeypox-2500_55_RIGHT_start', 'ACATCATCGGAGGATAATACGCTAA'), end_sequence=('monkeypox-2500_55_RIGHT_end', 'TTAGCGTATTATCCTCCGATGATGT')),
Adapter('Adapter_set_monkeypox-2500_57_LEFT', start_sequence=('monkeypox-2500_57_LEFT_start', 'TTGGGAGAACTTAAGCGGCAAG'), end_sequence=('monkeypox-2500_57_LEFT_end', 'CTTGCCGCTTAAGTTCTCCCAA')),
Adapter('Adapter_set_monkeypox-2500_57_RIGHT', start_sequence=('monkeypox-2500_57_RIGHT_start', 'AAACGATAAGAGTGGCCGCTTG'), end_sequence=('monkeypox-2500_57_RIGHT_end', 'CAAGCGGCCACTCTTATCGTTT')),
Adapter('Adapter_set_monkeypox-2500_59_LEFT', start_sequence=('monkeypox-2500_59_LEFT_start', 'AAGATTGCGGCTAATTGCTTCG'), end_sequence=('monkeypox-2500_59_LEFT_end', 'CGAAGCAATTAGCCGCAATCTT')),
Adapter('Adapter_set_monkeypox-2500_59_RIGHT', start_sequence=('monkeypox-2500_59_RIGHT_start', 'GAGGGAATTGACTCGCGAAAGA'), end_sequence=('monkeypox-2500_59_RIGHT_end', 'TCTTTCGCGAGTCAATTCCCTC')),
Adapter('Adapter_set_monkeypox-2500_61_LEFT', start_sequence=('monkeypox-2500_61_LEFT_start', 'ACAGAACAATTAGAGCGGCAGG'), end_sequence=('monkeypox-2500_61_LEFT_end', 'CCTGCCGCTCTAATTGTTCTGT')),
Adapter('Adapter_set_monkeypox-2500_61_RIGHT', start_sequence=('monkeypox-2500_61_RIGHT_start', 'ACACGATGCGACAATGTATAGACT'), end_sequence=('monkeypox-2500_61_RIGHT_end', 'AGTCTATACATTGTCGCATCGTGT')),
Adapter('Adapter_set_monkeypox-2500_63_LEFT', start_sequence=('monkeypox-2500_63_LEFT_start', 'GACGATGATGATTGATCACTATTACACA'), end_sequence=('monkeypox-2500_63_LEFT_end', 'TGTGTAATAGTGATCAATCATCATCGTC')),
Adapter('Adapter_set_monkeypox-2500_63_RIGHT', start_sequence=('monkeypox-2500_63_RIGHT_start', 'AATCCATCCATTGCCGTCTGAT'), end_sequence=('monkeypox-2500_63_RIGHT_end', 'ATCAGACGGCAATGGATGGATT')),
Adapter('Adapter_set_monkeypox-2500_65_LEFT', start_sequence=('monkeypox-2500_65_LEFT_start', 'TCAATCCCAAACCCAAAACCGT'), end_sequence=('monkeypox-2500_65_LEFT_end', 'ACGGTTTTGGGTTTGGGATTGA')),
Adapter('Adapter_set_monkeypox-2500_65_RIGHT', start_sequence=('monkeypox-2500_65_RIGHT_start', 'CCCAGTAAGCAACTCCATAGCA'), end_sequence=('monkeypox-2500_65_RIGHT_end', 'TGCTATGGAGTTGCTTACTGGG')),
Adapter('Adapter_set_monkeypox-2500_67_LEFT', start_sequence=('monkeypox-2500_67_LEFT_start', 'ACTTTCGAGGTTATTGGTTGTGGA'), end_sequence=('monkeypox-2500_67_LEFT_end', 'TCCACAACCAATAACCTCGAAAGT')),
Adapter('Adapter_set_monkeypox-2500_67_RIGHT', start_sequence=('monkeypox-2500_67_RIGHT_start', 'GCATACGCTACTCCAGAGAACG'), end_sequence=('monkeypox-2500_67_RIGHT_end', 'CGTTCTCTGGAGTAGCGTATGC')),
Adapter('Adapter_set_monkeypox-2500_69_LEFT', start_sequence=('monkeypox-2500_69_LEFT_start', 'TGATGCACTAACGAGAAAATTAGAAGG'), end_sequence=('monkeypox-2500_69_LEFT_end', 'CCTTCTAATTTTCTCGTTAGTGCATCA')),
Adapter('Adapter_set_monkeypox-2500_69_RIGHT', start_sequence=('monkeypox-2500_69_RIGHT_start', 'ACTTAAACCACCATCAAAAATCCATGT'), end_sequence=('monkeypox-2500_69_RIGHT_end', 'ACATGGATTTTTGATGGTGGTTTAAGT')),
Adapter('Adapter_set_monkeypox-2500_71_LEFT', start_sequence=('monkeypox-2500_71_LEFT_start', 'GGTGGAGTCGTTAAAGGTGACA'), end_sequence=('monkeypox-2500_71_LEFT_end', 'TGTCACCTTTAACGACTCCACC')),
Adapter('Adapter_set_monkeypox-2500_71_RIGHT', start_sequence=('monkeypox-2500_71_RIGHT_start', 'TGCCTTGCATGTGATAAGACCT'), end_sequence=('monkeypox-2500_71_RIGHT_end', 'AGGTCTTATCACATGCAAGGCA')),
Adapter('Adapter_set_monkeypox-2500_73_LEFT', start_sequence=('monkeypox-2500_73_LEFT_start', 'ATTGGATTCACGGTGGGTCATG'), end_sequence=('monkeypox-2500_73_LEFT_end', 'CATGACCCACCGTGAATCCAAT')),
Adapter('Adapter_set_monkeypox-2500_73_RIGHT', start_sequence=('monkeypox-2500_73_RIGHT_start', 'TCACAGACAGCATTTGGATCCA'), end_sequence=('monkeypox-2500_73_RIGHT_end', 'TGGATCCAAATGCTGTCTGTGA')),
Adapter('Adapter_set_monkeypox-2500_75_LEFT', start_sequence=('monkeypox-2500_75_LEFT_start', 'ATTCGATCGTCATGGGCATAGT'), end_sequence=('monkeypox-2500_75_LEFT_end', 'ACTATGCCCATGACGATCGAAT')),
Adapter('Adapter_set_monkeypox-2500_75_RIGHT', start_sequence=('monkeypox-2500_75_RIGHT_start', 'TGTATCTGAATCCATGTTAGTAGTAAGCA'), end_sequence=('monkeypox-2500_75_RIGHT_end', 'TGCTTACTACTAACATGGATTCAGATACA')),
Adapter('Adapter_set_monkeypox-2500_77_LEFT', start_sequence=('monkeypox-2500_77_LEFT_start', 'GTTGGGACTGACAGATGTGTTCT'), end_sequence=('monkeypox-2500_77_LEFT_end', 'AGAACACATCTGTCAGTCCCAAC')),
Adapter('Adapter_set_monkeypox-2500_77_RIGHT', start_sequence=('monkeypox-2500_77_RIGHT_start', 'TGTATCGCATTCCACCCTTTCC'), end_sequence=('monkeypox-2500_77_RIGHT_end', 'GGAAAGGGTGGAATGCGATACA')),
Adapter('Adapter_set_monkeypox-2500_79_LEFT', start_sequence=('monkeypox-2500_79_LEFT_start', 'GATAGATCAGTGGGTGTCCATGAT'), end_sequence=('monkeypox-2500_79_LEFT_end', 'ATCATGGACACCCACTGATCTATC')),
Adapter('Adapter_set_monkeypox-2500_79_RIGHT', start_sequence=('monkeypox-2500_79_RIGHT_start', 'GTGTTGGGTACGACCGCTTATA'), end_sequence=('monkeypox-2500_79_RIGHT_end', 'TATAAGCGGTCGTACCCAACAC')),
Adapter('Adapter_set_monkeypox-2500_81_LEFT', start_sequence=('monkeypox-2500_81_LEFT_start', 'CACCTGATGGTCTGGACATACC'), end_sequence=('monkeypox-2500_81_LEFT_end', 'GGTATGTCCAGACCATCAGGTG')),
Adapter('Adapter_set_monkeypox-2500_81_RIGHT', start_sequence=('monkeypox-2500_81_RIGHT_start', 'ACTACGTCCTTTTGCCATTGCA'), end_sequence=('monkeypox-2500_81_RIGHT_end', 'TGCAATGGCAAAAGGACGTAGT')),
Adapter('Adapter_set_monkeypox-2500_83_LEFT', start_sequence=('monkeypox-2500_83_LEFT_start', 'CCACATTGGCTAGAGGAATGCC'), end_sequence=('monkeypox-2500_83_LEFT_end', 'GGCATTCCTCTAGCCAATGTGG')),
Adapter('Adapter_set_monkeypox-2500_83_RIGHT', start_sequence=('monkeypox-2500_83_RIGHT_start', 'TGATAAGCGACGCCATTCATGT'), end_sequence=('monkeypox-2500_83_RIGHT_end', 'ACATGAATGGCGTCGCTTATCA')),
Adapter('Adapter_set_monkeypox-2500_85_LEFT', start_sequence=('monkeypox-2500_85_LEFT_start', 'ACTAAATCTCCTTCATGCTCTCTCAC'), end_sequence=('monkeypox-2500_85_LEFT_end', 'GTGAGAGAGCATGAAGGAGATTTAGT')),
Adapter('Adapter_set_monkeypox-2500_85_RIGHT', start_sequence=('monkeypox-2500_85_RIGHT_start', 'ACCTGCTCGGTTACTTCTGTGT'), end_sequence=('monkeypox-2500_85_RIGHT_end', 'ACACAGAAGTAACCGAGCAGGT')),
Adapter('Adapter_set_monkeypox-2500_87_LEFT', start_sequence=('monkeypox-2500_87_LEFT_start', 'CCAAGCTAAGCGACTACCATCT'), end_sequence=('monkeypox-2500_87_LEFT_end', 'AGATGGTAGTCGCTTAGCTTGG')),
Adapter('Adapter_set_monkeypox-2500_87_RIGHT', start_sequence=('monkeypox-2500_87_RIGHT_start', 'TGATGCAATTGTCTGACAACCTAGA'), end_sequence=('monkeypox-2500_87_RIGHT_end', 'TCTAGGTTGTCAGACAATTGCATCA')),]


def make_full_native_barcode_adapter(barcode_num):
    barcode = [x for x in ADAPTERS if x.name == 'Barcode ' + str(barcode_num) + ' (reverse)'][0]
    start_barcode_seq = barcode.start_sequence[1]
    end_barcode_seq = barcode.end_sequence[1]

    start_full_seq = 'AATGTACTTCGTTCAGTTACGTATTGCTAAGGTTAA' + start_barcode_seq + 'CAGCACCT'
    end_full_seq = 'AGGTGCTG' + end_barcode_seq + 'TTAACCTTAGCAATACGTAACTGAACGAAGT'

    return Adapter('Native barcoding ' + str(barcode_num) + ' (full sequence)',
                   start_sequence=('NB' + '%02d' % barcode_num + '_start', start_full_seq),
                   end_sequence=('NB' + '%02d' % barcode_num + '_end', end_full_seq))


def make_old_full_rapid_barcode_adapter(barcode_num):  # applies to SQK-RBK001
    barcode = [x for x in ADAPTERS if x.name == 'Barcode ' + str(barcode_num) + ' (forward)'][0]
    start_barcode_seq = barcode.start_sequence[1]

    start_full_seq = 'AATGTACTTCGTTCAGTTACG' + 'TATTGCT' + start_barcode_seq + \
                     'GTTTTCGCATTTATCGTGAAACGCTTTCGCGTTTTTCGTGCGCCGCTTCA'

    return Adapter('Rapid barcoding ' + str(barcode_num) + ' (full sequence, old)',
                   start_sequence=('RB' + '%02d' % barcode_num + '_full', start_full_seq))


def make_new_full_rapid_barcode_adapter(barcode_num):  # applies to SQK-RBK004
    barcode = [x for x in ADAPTERS if x.name == 'Barcode ' + str(barcode_num) + ' (forward)'][0]
    start_barcode_seq = barcode.start_sequence[1]

    start_full_seq = 'AATGTACTTCGTTCAGTTACG' + 'GCTTGGGTGTTTAACC' + start_barcode_seq + \
                     'GTTTTCGCATTTATCGTGAAACGCTTTCGCGTTTTTCGTGCGCCGCTTCA'

    return Adapter('Rapid barcoding ' + str(barcode_num) + ' (full sequence, new)',
                   start_sequence=('RB' + '%02d' % barcode_num + '_full', start_full_seq))