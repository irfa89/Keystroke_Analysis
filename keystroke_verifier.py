from scipy.spatial.distance import cityblock
import numpy as np

class keystroke_verifier:

    def __init__(self,df,thresholds,train_size,test_size):
        self.df = df
        self.thresholds = thresholds
        self.train_size = train_size
        self.test_size  = test_size
        self.genuine_score = []                             # list
        self.imposter_score = []                            # list
        self.mean_vector_template = []                      # numpy array
        self.false_accept_rate = []                         #list
        self.false_reject_rate = []                         #list


    def thresholds_steps(self):
        imposter_thresholds = np.arange(min(self.imposter_score),max(self.imposter_score),0.5)
        genuine_thresholds  =  np.arange(min(self.genuine_score),max(self.genuine_score),0.5)
        range_thresholds    =  np.concatenate([imposter_thresholds,genuine_thresholds])
        thresholds_value    = np.arange(min(range_thresholds),max(range_thresholds),0.5)
        #print(type(imposter_thresholds))
        #print(type(genuine_thresholds))
        #print(len(thresholds_value))
        #print(thresholds_value.sort())
        #return thresholds_value

    def model_train(self):
        self.mean_vector_template = self.train.mean().values
        #print(type(self.mean_vector_template))            # numpy array

    def score_calculate(self):
        for i in range(len(self.genuine_test_data.index)):
            self.genuine_score.append(cityblock(self.genuine_test_data.iloc[i].values,self.mean_vector_template))

        for i in range(len(self.imposter_test_data.index)):
            self.imposter_score.append(cityblock(self.imposter_test_data.iloc[i].values,self.mean_vector_template))

    def parameter_calculate(self):

        for threshold in self.thresholds:
            false_positive = 0
            false_negative = 0
            true_positive = 0
            true_negative = 0

            for score in self.genuine_score:
                if score > threshold:
                    true_negative = true_negative + 1
                else:
                    true_positive = true_positive + 1


            for score in self.imposter_score:
                if score > threshold:
                    false_negative = false_negative + 1
                else:
                    false_positive = false_positive + 1

            self.false_reject_rate.append(float(true_negative) / float(len(self.genuine_score)))
            self.false_accept_rate.append(float(false_positive) / float(len(self.imposter_score)))



    def split_data(self,users):
        false_accept_rate = []
        false_reject_rate = []
        for user in users:
            genuine_raw = self.df.loc[self.df.subject == user,"H.period":]
            imposter_raw = self.df.loc[self.df.subject != user, :]
            self.train = genuine_raw[:self.train_size]
            self.genuine_test_data = genuine_raw[self.test_size:]  # pandas dataframe
            self.imposter_test_data = imposter_raw.groupby("subject").tail(self.test_size).iloc[:,1:] #pandas dataframe
            self.model_train()
            self.score_calculate()
        self.parameter_calculate()
        false_accept_rate = self.false_accept_rate
        false_reject_rate = self.false_reject_rate
        return false_accept_rate, false_reject_rate

        #self.thresholds_steps()
        #print(type(self.false_accept_rate))
        #print(len(self.false_accept_rate))
        #print(self.false_accept_rate)
        #print(type(self.false_reject_rate))
        #print(len(self.false_reject_rate))
        #print(self.false_reject_rate)

        #print(len(self.genuine_score))              # 10,200 for 200 sample data
        #print(len(self.imposter_score))             # 5,10,000 for 200 sample data
        #print(type(self.genuine_score))
        #print((self.imposter_score))
        #print(self.imposter_score)
        #print(self.genuine_test_data.info())        #pandas
        #print(self.imposter_test_data.info())      #pandas
        #print(genuine_raw.info())                  #pandas
        #print(imposter_raw.info())                 #pandas


