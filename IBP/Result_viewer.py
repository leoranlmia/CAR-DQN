import numpy as np
import argparse

parser = argparse.ArgumentParser(description='DQN')

parser.add_argument(
    '--test-model-dir',
    default='',
    metavar='TMD',
    help='folder to load the test result')


def nominal_info(path):
    nominal = np.load(path + 'nominal.npy')
    print(np.mean(nominal))
    sem = np.std(nominal) / np.sqrt(np.shape(nominal))
    print(sem)


def pgd_info(path):
    eps = np.load(path + 'pgd_epsilons.npy')
    print(eps)
    vals = np.load(path + 'pgd.npy')
    print(np.mean(vals, axis=1))
    sem = np.std(vals, axis=1) / np.sqrt(np.shape(vals)[1])
    print(sem)


if __name__ == '__main__':
    args = parser.parse_args()

    path = '{}/'.format(args.test_model_dir)
    nominal_info(path)
    pgd_info(path)
