class BarometerHeaders:
    def __init__(self, agency, region, typo, level, code_uic, station):
        # Add header index, they are different depending on the files
        self.dictionary_headers = {
            'Agence': agency,
            'Région (UG)': region,
            'Typologie de la gare': typo,
            'Niveau de service': level,
            'Code UIC': code_uic,
            'Gare': station
        }
