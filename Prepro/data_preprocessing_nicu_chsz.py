'''
=================================================
coding:utf-8
@Time:      2024/6/3 14:50
@File:      data_preprocessing_nicu_chsz.py
@Author:    Ziwei Wang
@Function:
=================================================
'''
'''
=================================================
coding:utf-8
@Time:      2024/3/12 15:10
@File:      data_preprocessing.py
@Author:    Ziwei Wang
@Function:
=================================================
'''
import os
import mne
import numpy as np
import scipy.io as io
from sklearn import preprocessing
from scipy.linalg import fractional_matrix_power
from scipy import signal

def prepro(X, subject):
    filX = filter(X, subject)
    return filX

def filter(X, subject):
    # if 'Dog' not in subject:
    #     X = signal.resample(X, 400, axis=-1)
    X = mne.filter.notch_filter(X, Fs=X.shape[-1], freqs=50, n_jobs=100)
    X = mne.filter.filter_data(X, sfreq=X.shape[-1], l_freq=0.5, h_freq=50, n_jobs=100)  # n_jobs可以极大提高处理速度
    if 'Patient_1' in subject:
        X = mne.filter.resample(X, down=1.25)
    elif 'Dog' not in subject and 'Patient_1' not in subject:
        X = mne.filter.resample(X, down=12.5)
    return X


def standard_normalize(x_train):
    mean, std = np.mean(x_train), np.std(x_train)
    x_train = (x_train - mean) / std
    return x_train


def EA(x):
    """
    Parameters
    ----------
    x : numpy array
        data of shape (num_samples, num_channels, num_time_samples)

    Returns
    ----------
    XEA : numpy array
        data of shape (num_samples, num_channels, num_time_samples)
    """
    cov = np.zeros((x.shape[0], x.shape[1], x.shape[1]))
    for i in range(x.shape[0]):
        cov[i] = np.cov(x[i]) + 1e-6
    refEA = np.mean(cov, 0)
    sqrtRefEA = fractional_matrix_power(refEA, -0.5) + 1e-6
    XEA = np.zeros(x.shape)
    for i in range(x.shape[0]):
        XEA[i] = np.dot(sqrtRefEA, x[i])
    return XEA


def load_data(root_path, subjects, norm):
    for subject in subjects:
        inter_data = LoadInterictalDataTask(subject, root_path)
        inter_labels = np.zeros(inter_data.shape[0])
        ictal_data = LoadIctalDataTask(subject, root_path)
        ictal_labels = np.ones(ictal_data.shape[0])
        # print(subject)
        # print(inter_data.shape[1], inter_data.shape[2], inter_data.shape[0], ictal_data.shape[0])
        data = np.concatenate((inter_data, ictal_data), axis=0)
        labels = np.concatenate((inter_labels, ictal_labels), axis=0)
        # data preprocessing
        data = prepro(data, subject)
        # EA
        if norm == 'ea':
            data = EA(data)
            io.savemat(root_path + 'MergeData/' + subject + '_EA.mat', {'X': data, 'y': labels})
            print(subject+' EA has been processed. ', data.shape, labels.shape)
        elif norm == 'no':
            io.savemat(root_path + 'MergeData/' + subject + '.mat', {'X': data, 'y': labels})
            print(subject + ' has been processed. ', data.shape, labels.shape)
        elif norm == 'zscore':
            data = standard_normalize(data)
            io.savemat(root_path + 'MergeData/' + subject + '_zscore.mat', {'X': data, 'y': labels})
            print(subject + ' zscore has been processed. ', data.shape, labels.shape)


def LoadIctalDataTask(subject, path):
    folder_path = path + subject + '/'
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.mat')]
    all_file = []
    for file_name in file_names:
        if 'interictal' not in file_name and 'test' not in file_name:
            file_path = os.path.join(folder_path, file_name)
            mat_file = io.loadmat(file_path)
            all_file.append(mat_file['data'])
    all_file = np.array(all_file)
    return all_file


def LoadInterictalDataTask(subject, path):
    folder_path = path + subject + '/'
    file_names = [f for f in os.listdir(folder_path) if f.endswith('.mat')]
    all_file = []
    for file_name in file_names:
        if 'interictal' in file_name:
            file_path = os.path.join(folder_path, file_name)
            mat_file = io.loadmat(file_path)
            all_file.append(mat_file['data'])
    all_file = np.array(all_file)
    return all_file


def merge_data(root_path, patients, norm, dataset):
    person_data = []
    person_labels = []
    for subject in patients:
        src = io.loadmat(root_path + 'prepro/prepro_' + subject + '.mat')
        data = np.transpose(src['X'], (0, 2, 1))
        if dataset == 'NICU':
            data = mne.filter.resample(data, down=2.56)
        else:
            if data.shape[-1] == 2000:
                data = mne.filter.resample(data, down=5)
            elif data.shape[-1] == 4000:
                data = mne.filter.resample(data, down=10)
        labels = src['y'].squeeze()
        if norm == 'ea':
            data = EA(data)
            # io.savemat(root_path + 'MergeData/' + subject + '_EA.mat', {'X': data, 'y': labels})
            # print(subject+' EA has been processed. ', data.shape, labels.shape)
        # elif norm == 'no':
        #     io.savemat(root_path + 'MergeData/' + subject + '.mat', {'X': data, 'y': labels})
        #     print(subject + ' has been processed. ', data.shape, labels.shape)
        elif norm == 'zscore':
            data = standard_normalize(data)
            # io.savemat(root_path + 'MergeData/' + subject + '_zscore.mat', {'X': data, 'y': labels})
            # print(subject + ' zscore has been processed. ', data.shape, labels.shape)
        person_data.append(data)
        person_labels.append(labels)
    person_data = np.concatenate(person_data, axis=0)
    person_labels = np.concatenate(person_labels, axis=0)
    if norm == 'ea':
        io.savemat(root_path + 'MergeData/' + 'all_patient_EA.mat', {'X': person_data, 'y': person_labels})
        print('All patients EA have been merged.', person_data.shape, person_labels.shape)
    elif norm == 'no':
        io.savemat(root_path + 'MergeData/' + 'all_patient.mat', {'X': person_data, 'y': person_labels})
        print('All patients have been merged.', person_data.shape, person_labels.shape)
    elif norm == 'zscore':
        io.savemat(root_path + 'MergeData/' + 'all_patient_zscore.mat', {'X': person_data, 'y': person_labels})
        print('All patients zscore have been merged.', person_data.shape, person_labels.shape)


if __name__ == '__main__':
    dataset = 'NICU'  # 'NICU', 'CHSZ'
    if dataset == 'NICU':
        root_path = './seizure-data/NICU/'
        patients = ['subject_1', 'subject_4', 'subject_5', 'subject_7', 'subject_9', 'subject_11', 'subject_13',
                           'subject_14', 'subject_15', 'subject_16', 'subject_17', 'subject_19', 'subject_20', 'subject_21',
                           'subject_22', 'subject_25', 'subject_31', 'subject_34', 'subject_36', 'subject_38', 'subject_39',
                           'subject_40', 'subject_41', 'subject_44', 'subject_47', 'subject_50', 'subject_51', 'subject_52',
                           'subject_62', 'subject_63', 'subject_66', 'subject_67', 'subject_69', 'subject_73', 'subject_75',
                           'subject_76', 'subject_77', 'subject_78', 'subject_79']
    else:
        root_path = './seizure-data/CHSZ/'
        patients = ['subject_1', 'subject_2', 'subject_3', 'subject_4', 'subject_5', 'subject_6', 'subject_7',
                       'subject_8', 'subject_9', 'subject_10', 'subject_11', 'subject_12', 'subject_13', 'subject_14',
                       'subject_15', 'subject_16', 'subject_17', 'subject_18', 'subject_19', 'subject_20', 'subject_21',
                       'subject_22', 'subject_23', 'subject_24', 'subject_25', 'subject_26', 'subject_27']
    norm = 'ea'  # ['ea', 'zscore', 'no']
    merge_data(root_path, patients, norm, dataset)
