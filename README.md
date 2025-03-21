# Canine EEG Helps Human: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment

**📰 News:** Our paper has been accepted for publication in **National Science Review (IF=16.3)**.

This repository contains the original Python code for our paper [**Canine EEG Helps Human: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment**](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwaf086/8052010) (National Science Review, 2025).

## Overview
This work addresses the challenge of **cross-species (canine/human) and cross-modality (scalp/intracranial) EEG-based epileptic seizure detection**. Traditional models rely on within-species and within-modality data, limiting their generalizability. We introduce **ResizeNet+Multi-Space Alignment (MSA)**, a multi-space alignment framework that facilitates knowledge transfer across species and modalities, overcoming dataset heterogeneity and enhancing seizure detection performance.

This study represents a pioneering effort in multi-species and multi-modality EEG integration, offering a scalable solution to train large brain models with diverse EEG data.

---

## Challenges
Our study focuses on a scenario where the target species has little or no labeled data, leveraging auxiliary labeled data from another species or modality. The key challenges include:

- Electrode configuration and signal heterogeneity: Differences in electrode placements, sampling rates, and signal properties hinder direct transfer across species and modalities.
- Distributional shifts: EEG feature distributions vary significantly across species, datasets, and subjects, posing challenges for feature alignment.
- Limited labeled data: Scarcity of labeled seizure events in the target species constrains model training.

## Cross-Species Similarity
Despite biological differences, EEG seizure patterns exhibit cross-species similarities across multiple feature domains:

- Temporal domain: Both canine and human EEG signals show pronounced fluctuations during seizures.
- Entropy domain: The approximate entropy of intracranial EEG increases significantly during seizures for both species, highlighting potential transferability.
- Spectral domain: Power spectral density analysis reveals similar increases in seizure-related frequency components across species.

<img width="1188" alt="image" src="https://github.com/user-attachments/assets/73a4f9e5-5178-4942-a76b-dd8c34b35b73" />
<p align="center"><font color="gray">Figure 1: Evidence for cross-species and cross-modality feature transferability.


## Cross-Species Discrepancy
While similarities exist, significant discrepancies remain:

- Input space differences: Variations in electrode placement and device types introduce modality-specific biases.
  - Canine EEG data is acquired via implanted intracranial electrodes, whereas human scalp EEG is recorded non-invasively.
  - Even within the same modality, electrode configurations differ significantly (e.g., 16 intracranial electrodes for canines vs. 6 for humans).
- Feature distribution gaps: Distinct seizure characteristics across species lead to feature misalignment.

<img width="1211" alt="image" src="https://github.com/user-attachments/assets/1b75f4d8-c435-4120-b300-0f946ebc4d21" />
<p align="center"><font color="gray">Figure 2: Gaps for successful cross-species knowledge transfer in algorithm design.

## Proposed Framework
We propose the ResizeNet+MSA approach to enable epilepsy pattern transfer across species and modalities (see Figure 3). `rgb(9, 105, 218)`**ResizeNet is highly adaptable for cross-headset/cross-dataset transfer in BCI tasks, such as cross-headset motor imagery (MI) classification. We are actively exploring its applications in broader domains.**

<img width="1256" alt="image" src="https://github.com/user-attachments/assets/314659a4-4e1a-4fef-9a30-329b323161f9" />
<p align="center"><font color="gray">Figure 3: The framework of cross-species and cross-modality transfer network utilizes intracranial/scalp EEG data from canines and humans (left). ResizeNet, which projects EEG signals of the species with higher dimensionality to a lower dimensionality to match their feature spaces (right).

## Key Results
We validate ResizeNet+MSA on four clinical EEG datasets (Kaggle, Freiburg, CHSZ, NICU), demonstrating significant improvements in cross-species seizure detection:

- Unsupervised transfer scenario: With no labeled data in the target domain, ResizeNet+MSA achieves 85.4% accuracy, outperforming non-alignment methods by 17%.
- Limited labeled data scenario: When the target domain has <5% labeled data, ResizeNet+MSA achieves an AUC of 92.8%, surpassing the within-species baseline by 18.7%.
- Feature preservation: ResizeNet retains essential EEG signal characteristics, see Figure 4.
- Effective feature alignment: Post-alignment, category-related features cluster more distinctly across species, improving classification robustness, see Figure 5.

<img width="826" alt="image" src="https://github.com/user-attachments/assets/f76fbfb8-ba74-4a8a-bc76-d0c186f20962" />
<p align="center"><font color="gray">Figure 4: Significant characteristic preservation after ResizeNet transformation.


<img width="809" alt="image" src="https://github.com/user-attachments/assets/c99a64d0-3a3b-4742-81d8-1a9b20b1570e" />
<p align="center"><font color="gray">Figure 5: Improved feature alignment across species using ResizeNet+MSA.

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

## Contact
For any questions or collaborations, please feel free to reach out via **vivi@hust.edu.cn** or open an issue in this repository.
