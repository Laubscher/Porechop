"""
Influenza A and B primers for PoreXop.
"""

from .adapters import (
    Adapter,
    make_full_native_barcode_adapter,
    make_old_full_rapid_barcode_adapter,
    make_new_full_rapid_barcode_adapter
)


ADAPTERS = [

    # Influenza A

    Adapter(
        'Influenza_A_Tuni-12',
        start_sequence=(
            'Tuni-12_start',
            'ACGCGTGATCAGCAAAAGCAGG'
        ),
        end_sequence=(
            'Tuni-12_end',
            'CCTGCTTTTGCTGATCACGCGT'
        )
    ),

    Adapter(
        'Influenza_A_Tuni-12.4',
        start_sequence=(
            'Tuni-12.4_start',
            'ACGCGTGATCAGCGAAAGCAGG'
        ),
        end_sequence=(
            'Tuni-12.4_end',
            'CCTGCTTTCGCTGATCACGCGT'
        )
    ),

    Adapter(
        'Influenza_A_Tuni-13',
        start_sequence=(
            'Tuni-13_start',
            'ACGCGTGATCAGTAGAAACAAGG'
        ),
        end_sequence=(
            'Tuni-13_end',
            'CCTTGTTTCTACTGATCACGCGT'
        )
    ),


    # Influenza B

    Adapter(
        'Influenza_B_PBs-UniF',
        start_sequence=(
            'B-PBs-UniF_start',
            'GGGGGGAGCAGAAGCGGAGC'
        ),
        end_sequence=(
            'B-PBs-UniF_end',
            'GCTCCGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_PBs-UniR',
        start_sequence=(
            'B-PBs-UniR_start',
            'CCGGGTTATTAGTAGAAACACGAGC'
        ),
        end_sequence=(
            'B-PBs-UniR_end',
            'GCTCGTGTTTCTACTAATAACCCGG'
        )
    ),

    Adapter(
        'Influenza_B_PA-UniF',
        start_sequence=(
            'B-PA-UniF_start',
            'GGGGGGAGCAGAAGCGGTGC'
        ),
        end_sequence=(
            'B-PA-UniF_end',
            'GCACCGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_PA-UniR',
        start_sequence=(
            'B-PA-UniR_start',
            'CCGGGTTATTAGTAGAAACACGTGC'
        ),
        end_sequence=(
            'B-PA-UniR_end',
            'GCACGTGTTTCTACTAATAACCCGG'
        )
    ),

    Adapter(
        'Influenza_B_HANA-UniF',
        start_sequence=(
            'B-HANA-UniF_start',
            'GGGGGGAGCAGAAGCAGAGC'
        ),
        end_sequence=(
            'B-HANA-UniF_end',
            'GCTCTGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_HANA-UniR',
        start_sequence=(
            'B-HANA-UniR_start',
            'CCGGGTTATTAGTAGTAACAAGAGC'
        ),
        end_sequence=(
            'B-HANA-UniR_end',
            'GCTCTTGTTACTACTAATAACCCGG'
        )
    ),

    Adapter(
        'Influenza_B_NP-UniF',
        start_sequence=(
            'B-NP-UniF_start',
            'GGGGGGAGCAGAAGCACAGC'
        ),
        end_sequence=(
            'B-NP-UniF_end',
            'GCTGTGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_NP-UniR',
        start_sequence=(
            'B-NP-UniR_start',
            'CCGGGTTATTAGTAGAAACAACAGC'
        ),
        end_sequence=(
            'B-NP-UniR_end',
            'GCTGTTGTTTCTACTAATAACCCGG'
        )
    ),

    Adapter(
        'Influenza_B_M-Uni3F',
        start_sequence=(
            'B-M-Uni3F_start',
            'GGGGGGAGCAGAAGCACGCACTT'
        ),
        end_sequence=(
            'B-M-Uni3F_end',
            'AAGTGCGTGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_Mg-Uni3F',
        start_sequence=(
            'B-Mg-Uni3F_start',
            'GGGGGGAGCAGAAGCAGGCACTT'
        ),
        end_sequence=(
            'B-Mg-Uni3F_end',
            'AAGTGCCTGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_M-Uni3R',
        start_sequence=(
            'B-M-Uni3R_start',
            'CCGGGTTATTAGTAGAAACAACGCACTT'
        ),
        end_sequence=(
            'B-M-Uni3R_end',
            'AAGTGCGTTGTTTCTACTAATAACCCGG'
        )
    ),

    Adapter(
        'Influenza_B_NS-Uni3F',
        start_sequence=(
            'B-NS-Uni3F_start',
            'GGGGGGAGCAGAAGCAGAGGATT'
        ),
        end_sequence=(
            'B-NS-Uni3F_end',
            'AATCCTCTGCTTCTGCTCCCCCC'
        )
    ),

    Adapter(
        'Influenza_B_NS-Uni3R',
        start_sequence=(
            'B-NS-Uni3R_start',
            'CCGGGTTATTAGTAGTAACAAGAGGATT'
        ),
        end_sequence=(
            'B-NS-Uni3R_end',
            'AATCCTCTTGTTACTACTAATAACCCGG'
        )
    )
]
