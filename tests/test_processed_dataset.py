"""Validaciones de estructura del CSV procesado, sin bibliotecas adicionales a pandas."""
from pathlib import Path
import unittest
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "processed" / "dengue_distrito_semanal.csv"
COLUMNS = {
    "ubigeo", "ano", "semana", "casos_semanales", "casos_graves",
    "casos_con_alarma", "casos_femeninos", "proporcion_graves",
    "proporcion_alarma", "departamento", "provincia", "distrito",
}


@unittest.skipUnless(CSV.exists(), "CSV procesado no disponible localmente; ejecutar notebook 02")
class TestProcessedDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(CSV, dtype={"ubigeo": "string"})

    def test_columns(self):
        self.assertTrue(COLUMNS.issubset(self.df.columns))

    def test_temporal_keys_unique(self):
        self.assertFalse(self.df.duplicated(["ubigeo", "ano", "semana"]).any())

    def test_geographic_fields_complete(self):
        self.assertFalse(self.df[["ubigeo", "departamento", "provincia", "distrito"]].isna().any().any())

    def test_valid_counts_and_proportions(self):
        d = self.df
        self.assertTrue(d["casos_semanales"].gt(0).all())
        self.assertTrue(d["semana"].between(1, 53).all())
        for field in ["casos_graves", "casos_con_alarma", "casos_femeninos"]:
            self.assertTrue(d[field].between(0, d["casos_semanales"]).all())
        for field in ["proporcion_graves", "proporcion_alarma"]:
            self.assertTrue(d[field].between(0, 1).all())


if __name__ == "__main__":
    unittest.main()
