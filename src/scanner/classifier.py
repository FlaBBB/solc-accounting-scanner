"""Pengklasifikasi untuk kandidat temuan yang ambigu.

Dipakai **hanya** untuk kandidat yang tidak dapat diputuskan secara struktural
oleh mesin aturan. Algoritma dibatasi pada SVM, Random Forest, dan Logistic
Regression karena jumlah data terbatas (1.021 judul temuan) dan model klasik
lebih mudah diinterpretasikan.

Pemilihan model akhir dilakukan berdasarkan kinerja pada data uji, dengan
pembagian 80:20 berlapis menurut sub-kelas dan dilakukan pada tingkat
repositori untuk mencegah kebocoran data.

Status: kerangka. Implementasi menyusul pada tahap 3.6 naskah.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal

ModelName = Literal["svm", "random_forest", "logreg"]

DEFAULT_PARAMS: dict[str, dict[str, Any]] = {
    "svm": {"kernel": "rbf", "C": 1.0, "class_weight": "balanced"},
    "random_forest": {"n_estimators": 300, "class_weight": "balanced", "random_state": 42},
    "logreg": {"max_iter": 2000, "class_weight": "balanced"},
}


@dataclass
class TrainedModel:
    """Pembungkus model terlatih beserta metadata."""

    name: ModelName
    model: Any
    feature_names: tuple[str, ...]
    classes: tuple[str, ...]

    def predict_proba(self, X: list[list[float]]) -> list[float]:
        """Probabilitas kelas positif untuk tiap baris fitur."""
        raise NotImplementedError("implementasi menyusul pada tahap pengklasifikasi")


def train(
    X: list[list[float]],
    y: list[str],
    *,
    name: ModelName = "random_forest",
    feature_names: tuple[str, ...] = (),
) -> TrainedModel:
    """Latih model pada matriks fitur dan label."""
    raise NotImplementedError("implementasi menyusul pada tahap pengklasifikasi")


def evaluate(y_true: list[str], y_pred: list[str]) -> dict[str, float]:
    """Hitung presisi, recall, dan F1."""
    raise NotImplementedError("implementasi menyusul pada tahap pengklasifikasi")


__all__ = ["DEFAULT_PARAMS", "ModelName", "TrainedModel", "evaluate", "train"]
