import argparse
import os


class Feature:
    def __init__(self, column, data):
        self._name = 'F' + str(column)

        self._values = set()
        for row in range(len(data)):
            self._values.add(FeatureValue(data[row][column]))

        for featureVal in self._values:
            counter = 0
            for row in range(len(data)):
                if featureVal.get_name() == data[row][column]:
                    counter += 1
            featureVal.set_occurrences(counter)

    def get_values(self):
        return self._values

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class FeatureValue:
    def __init__(self, name):
        self._name = name;
        self._occurrences = 0;
        self._prob = 0

    def get_name(self): return self._name

    def get_occurrences(self): return self._occurrences

    def set_occurrences(self, occurrences): self._occurrences = occurrences

    def get_prob(self): return self._prob

    def set_prob(self, prob): self._prob = prob

    def __eq__(self, o): return (isinstance(o, FeatureValue)) and (o._name == self._name)

    def __hash__(self): return hash(self._name)

    def __str__(self): return self._name


def prepare_dateset(file):
    dataset = []
    with open(file, 'r') as f:
        data = f.read().split('\n')
        for i in range(len(data)):
            line = data[i].split()
            if line != '\n' and line != '\r' and len(line) != 0:
                dataset.append(line)

    return dataset


def calculate_feature_probability(dataset, output_file):
    c = Feature(12, dataset)
    last_col = len(dataset[0]) - 1  # class
    prob = []
    for column in range(last_col):
        # in case of zero occurrence
        ff = 1
        ft = 1
        tf = 1
        tt = 1
        for row in range(len(dataset)):
            if dataset[row][column] == '0' and dataset[row][last_col] == '0':
                ff += 1
            elif dataset[row][column] == '0' and dataset[row][last_col] == '1':
                ft += 1
            elif dataset[row][column] == '1' and dataset[row][last_col] == '0':
                tf += 1
            elif dataset[row][column] == '1' and dataset[row][last_col] == '1':
                tt += 1

        f = Feature(column, dataset)

        ffp = float(ff / (ff + tf))  # P(F=0|S=0)
        ftp = float(ft / (ft + tt))  # P(F=0|S=1)
        tfp = float(tf / (ff + tf))  # P(F=1|S=0)
        ttp = float(tt / (ft + tt))  # P(F=1|S=1)

        out = open(output_file, "a")

        out.write('P({} = 0 | c = 0) = {}'.format(f.get_name(), ffp) + '\n')
        out.write('P({} = 0 | c = 1) = {}'.format(f.get_name(), ftp) + '\n')
        out.write('P({} = 1 | c = 0) = {}'.format(f.get_name(), tfp) + '\n')
        out.write('P({} = 1 | c = 1) = {}'.format(f.get_name(), ttp) + '\n')

        print('P({} = 0 | c = 0) = {}'.format(f.get_name(), ffp))
        print('P({} = 0 | c = 1) = {}'.format(f.get_name(), ftp))
        print('P({} = 1 | c = 0) = {}'.format(f.get_name(), tfp))
        print('P({} = 1 | c = 1) = {}'.format(f.get_name(), ttp))

        print('\n')
        out.write('\n')
        prob.append((ffp, ftp, tfp, ttp))

    return prob


def prediction(trainingset, testset, prob, output_file):
    c = Feature(12, trainingset)

    for val in c.get_values():
        if val.get_name() == '0':
            p0 = float((val.get_occurrences() + 1) / (len(trainingset) + 2))  # not spam
        elif val.get_name() == '1':
            p1 = float((val.get_occurrences() + 1) / (len(trainingset) + 2))  # is spam

    f = open(output_file, "a")

    for row in range(len(testset)):
        f.write('Test instance ' + str(row + 1) + ': ' + str(testset[row]) + '\n')
        print('Test instance ' + str(row + 1) + ': ' + str(testset[row]))
        pn = p0
        ps = p1  # possibility of spam

        for col in range(len(testset[0])):
            f_prob = prob[col]

            if testset[row][col] == '0':
                pn *= f_prob[0]
                ps *= f_prob[1]
            elif testset[row][col] == '1':
                pn *= f_prob[2]
                ps *= f_prob[3]
        f.write('MV(S) = ' + str(ps) + '\n')
        f.write('MV(Non-S) = ' + str(pn) + '\n')
        print('MV(S) = ' + str(ps))
        print('MV(Non-S) = ' + str(pn))
        if ps > pn:
            f.write('The predicted class of the input vector is: ' + 'Spam\n')
            print('The predicted class of the input vector is: ' + 'Spam\n')
        else:
            f.write('The predicted class of the input vector is: ' + 'Non-Spam\n')
            print('The predicted class of the input vector is: ' + 'Non-Spam\n')
        f.write('\n')

def Main():
    output_file = 'sampleoutput.txt'
    if os.path.exists(output_file):
        os.remove(output_file)

    parser = argparse.ArgumentParser()
    parser.add_argument('trainingset', help='Choose a training data set')
    parser.add_argument('testset', help='Choose a test data set')
    args = parser.parse_args()

    trainingset = prepare_dateset(args.trainingset)
    testset = prepare_dateset(args.testset)
    (prob) = calculate_feature_probability(trainingset, output_file)

    prediction(trainingset, testset, prob, output_file)


Main()
