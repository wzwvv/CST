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
        cov[i] = np.cov(x[i])
    refEA = np.mean(cov, 0)
    sqrtRefEA = fractional_matrix_power(refEA, -0.5)
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
        print(inter_data.shape)
        input('')
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


def merge_data(root_path, dogs, norm):
    dog_data = []
    dog_labels = []
    for subject in dogs:
        if norm == 'ea':
            src = io.loadmat(root_path + 'MergeData/' + subject + '_EA.mat')
        elif norm == 'no':
            src = io.loadmat(root_path + 'MergeData/' + subject + '.mat')
        elif norm == 'zscore':
            src = io.loadmat(root_path + 'MergeData/' + subject + '_zscore.mat')

        data = src['X'][:, :16, :]
        labels = src['y'].squeeze()
        dog_data.append(data)
        dog_labels.append(labels)
    dog_data = np.concatenate(dog_data, axis=0)
    dog_labels = np.concatenate(dog_labels, axis=0)
    if norm == 'ea':
        # 均值方差
        # mean = np.mean(dog_data)
        # std = np.std(dog_data)
        # print('All dogs EA mean and std: ', mean, std)
        io.savemat(root_path + 'MergeData/' + 'all_patient_EA.mat', {'X': dog_data, 'y': dog_labels})
        print('All patients EA have been merged.', dog_data.shape, dog_labels.shape)
    elif norm == 'no':
        io.savemat(root_path + 'MergeData/' + 'all_patient.mat', {'X': dog_data, 'y': dog_labels})
        print('All patients have been merged.', dog_data.shape, dog_labels.shape)
    elif norm == 'zscore':
        # 均值方差
        # mean = np.mean(dog_data)
        # std = np.std(dog_data)
        # print('All dogs mean and std: ', mean, std)
        io.savemat(root_path + 'MergeData/' + 'all_patient_zscore.mat', {'X': dog_data, 'y': dog_labels})
        print('All patients zscore have been merged.', dog_data.shape, dog_labels.shape)


if __name__ == '__main__':
    root_path = './seizure-data/'
    subjects = ['Dog_1', 'Dog_2', 'Dog_3', 'Dog_4', 'Patient_1', 'Patient_2', 'Patient_3', 'Patient_4', 'Patient_5',
                'Patient_6', 'Patient_7', 'Patient_8']
    # patients = ['Patient_1', 'Patient_2', 'Patient_3', 'Patient_4', 'Patient_5', 'Patient_6', 'Patient_7', 'Patient_8']
    # dogs = ['Dog_1', 'Dog_2', 'Dog_3', 'Dog_4']
    norm = 'no'  # ['ea', 'zscore', 'no']
    load_data(root_path, subjects, norm)
    # merge_data(root_path, patients, norm)
