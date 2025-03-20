# Canine EEG Helps Humans: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment

**📰 News:** Our paper has been accepted for publication in **National Science Review (IF = 16.3)**.

This repository contains the original Python code for our paper [**Canine EEG Helps Humans: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment**](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwaf086/8052010) (National Science Review, 2025).

## Overview
This work addresses the challenge of **cross-species (canine/human) and cross-modality (scalp/intracranial) EEG-based epileptic seizure detection**. Traditional models rely on within-species and within-modality data, limiting their generalizability. We introduce **ResizeNet+MSA**, a multi-space alignment framework that facilitates knowledge transfer across species and modalities, overcoming dataset heterogeneity and enhancing seizure detection performance.

This study represents a pioneering effort in **multi-species and multi-modality EEG integration**, offering a scalable solution to train large brain models with diverse EEG data.

---

## Challenges
Our study focuses on a scenario where **the target species has little or no labeled data**, leveraging auxiliary labeled data from another species or modality. The key challenges include:

- **Electrode configuration and signal heterogeneity**: Differences in electrode placements, sampling rates, and signal properties hinder direct transfer across species and modalities.
- **Distributional shifts**: EEG feature distributions vary significantly across species, datasets, and subjects, posing challenges for feature alignment.
- **Limited labeled data**: Scarcity of labeled seizure events in the target species constrains model training.

---

## Cross-Species Similarity
Despite biological differences, **EEG seizure patterns exhibit cross-species similarities** across multiple feature domains:

- **Temporal domain**: Both canine and human EEG signals show pronounced fluctuations during seizures.
- **Entropy domain**: The approximate entropy of intracranial EEG increases significantly during seizures for both species, highlighting potential transferability.
- **Spectral domain**: Power spectral density analysis reveals similar increases in seizure-related frequency components across species.

**Figure 1: Cross-species feature similarities in the temporal, spectral, and entropy domains.**  

<img width="416" alt="image" src="https://github.com/user-attachments/assets/f6fe4efe-9061-48e5-84aa-81ac874831f9" />

---

## Cross-Species Discrepancy
While similarities exist, **significant discrepancies** remain:

- **Input space differences**: Variations in electrode placement and device types introduce modality-specific biases.
  - Canine EEG data is acquired via **implanted intracranial electrodes**, whereas human scalp EEG is recorded **non-invasively**.
  - Even within the same modality, electrode configurations differ significantly (e.g., **16 intracranial electrodes for canines** vs. **6 for humans**).
- **Feature distribution gaps**: Distinct seizure characteristics across species lead to feature misalignment.

**Figure 2: Cross-species and cross-modality discrepancies in electrode placement and signal characteristics.**  

<img width="416" alt="image" src="https://github.com/user-attachments/assets/c06261a0-9ebb-426a-9e59-6c6136481002" />

---

## Proposed Framework
We introduce a **multi-space joint alignment mechanism** to facilitate epilepsy pattern transfer across species and modalities:

- **Input-space alignment (ResizeNet)**: Maps EEG signals from higher-dimensional sources to a lower-dimensional space for compatibility.
- **Feature-space alignment (MSA)**: Reduces distributional shifts between species and modalities.
- **Output-space alignment**: Ensures seizure classification consistency across different datasets.

**Figure 3: Overview of ResizeNet+MSA framework for cross-species EEG seizure detection.**  

<img width="416" alt="image" src="https://github.com/user-attachments/assets/bce199d7-3354-4a76-95cb-2f7dc171637b" />

---

## Key Results
We validate ResizeNet+MSA on four clinical EEG datasets (**Kaggle, Freiburg, CHSZ, NICU**), demonstrating significant improvements in cross-species seizure detection:

- **Limited labeled data scenario**: When the target domain has **<5% labeled data**, ResizeNet+MSA achieves an **AUC of 92.8%**, surpassing the within-species baseline by **18.7%**.
- **Unsupervised transfer scenario**: With **no labeled data in the target domain**, ResizeNet+MSA achieves **85.4% accuracy**, outperforming non-alignment methods by **17%**.
- **Feature preservation**: ResizeNet retains essential EEG signal characteristics.
- **Effective feature alignment**: Post-alignment, seizure-related features cluster more distinctly across species, improving classification robustness.

**Figure 4: EEG feature preservation after ResizeNet transformation.**  

<img width="416" alt="image" src="https://github.com/user-attachments/assets/ea3ad14c-c512-426c-a15b-8799675a93f9" />

**Figure 5: Improved feature alignment across species using ResizeNet+MSA.**  

<img width="416" alt="image" src="https://github.com/user-attachments/assets/e007d177-6326-43c0-9348-33c14a976829" />

---

## Citation
If you find this work useful, please consider citing our paper:

```bibtex
@article{wang2025canine,
  title={Canine EEG Helps Human: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment},
  author={Wang, Ziwei and Li, Siyang and Wu, Dongrui},
  journal={National Science Review},
  pages={nwaf086},
  year={2025},
  publisher={Oxford University Press},
}
```
---

## Contact
For any questions or collaborations, please feel free to reach out via **vivi@hust.edu.cn** or open an issue in this repository.
