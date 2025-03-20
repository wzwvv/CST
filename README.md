# Canine EEG Helps Human: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment
**News:** Our paper has been accepted for publication in **National Science Review (IF = 16.3)**.

This repository contains the original Python code for our paper [**Canine EEG Helps Human: Cross-Species and Cross-Modality Epileptic Seizure Detection via Multi-Space Alignment**](https://academic.oup.com/nsr/advance-article/doi/10.1093/nsr/nwaf086/8052010) (National Science Review, 2025).

In this paper, we considered a very challenging scenario: cross-species (canine/human) and cross-modality (scalp/intracranial) transfer for electroencephalogram (EEG) based epileptic seizure detection. And in overall sight, they are all cross-dataset (cross-headset) transfer. By employing multi-space alignments, the proposed ResizeNet+MSA aligns cross-species and cross-modality EEG signals to enhance the detection capability beyond traditional within-species and within-modality models. This is a pilot study that provides insights into the challenges and promise of multi-species and multi-modality data integration, offering an effective solution to collecting huge EEG data to train large brain models.

## Challenges
This work considers the setting that the target species itself has little or no labeled data, and some labeled data from an auxiliary species/modality are used to train a seizure classifier. It addresses the following challenges in cross-species and cross-modality transfer: 
- Differences in electrode configurations, sampling rates, and signal characteristics present significant obstacles to aligning the input space of distinct species and modalities.
- In addition to the input heterogeneity, distribution discrepancies across species, datasets, and subjects also introduce large heterogeneities in the feature and output spaces. 
- Limited labeled data for the target species, a common yet critical limitation in automatic seizure detection.

## Cross-Species Similarity
We first analyzed the feature similarities across species and modalities from the perspective of temporal, spectral, and entropy features (Figure 1). For temporal features, EEG signals from both canines and humans exhibit large fluctuations during epileptic seizures, indicating the transferability in the time domain. For entropy features, the approximate entropy of intracranial EEG from both species increases significantly during seizures, indicating their transferability across species. For spectral features, power spectral density spectrograms derived from consecutive Fourier transforms for both species show an increase in the power across all channels during seizures, suggesting the transferability in the frequency domain.
<img width="473" alt="image" src="https://github.com/user-attachments/assets/046c523e-781e-4bad-adf0-d8715f3caba5" />

## Cross-Species Discrepancy
However, discrepancies across species and modalities are also evident (Figure 2). Input space disparity across species is highlighted by the discrepancy in electrode configurations between species. In terms of data acquisition devices, canine intracranial EEG signals were captured using implanted intracranial electrodes, whereas human scalp EEG signals were collected via non-invasive scalp electrodes. Even for the same signal modality, the number and configuration of electrodes can be significantly different, e.g., 16 intracranial electrodes were used for canines’ intracranial EEG data, whereas only 6 were used for humans’ intracranial EEG data. Feature distribution gaps between canines and humans are also significant.
<img width="481" alt="image" src="https://github.com/user-attachments/assets/41d943a2-7bb0-49e3-95a1-a4285420e662" />

## Overall Framework
The proposed joint alignment mechanism in the input-feature-output space enables epilepsy pattern transfer across biological barriers (Figure 3). The framework of cross-species and cross-modality transfer network utilizes intracranial/scalp EEG data from canines and humans (left). ResizeNet, which projects EEG signals of the species with higher dimensionality to a lower dimensionality to match their feature spaces (right).
<img width="477" alt="image" src="https://github.com/user-attachments/assets/8a3e110f-cd7a-4e1b-b127-c17473b17ad9" />

## Key Results









