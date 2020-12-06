# Debug variables --------------------------------
VERBOSE = True

# Imports ----------------------------------------
import numpy as np

# Filter Classes ---------------------------------
# ----- Time-averaging filter --------------------
class TimeAveragingFilter():
    a_Weights      = [] # Placeholder
    a_Data         = [] # Placeholder
    # Constructor
    def __init__(self, a_Weights, a_Data=[], b_ValidateInputs = True):
        # This class takes in an array of weights
        # in the form of [0.4, 0.3, 0.2, 0.1] which
        # would average the signal as 0.4*x_n + 0.3*x_(n-1) + 0.2*x_n-2 ...
        # these weights must be positive and between 0 and 1
        if b_ValidateInputs:
            self.a_Weights      =   self.ValidateWeights(a_Weights)
            # We also need to provide an array of data
            self.a_Data         =   self.ValidateData(a_Data)
        if b_ValidateInputs == False:
            self.a_Weights = a_Weights
            self.a_Data = a_Data

    def ValidateWeights(self, a_Weights):
        # Check that our sum must equal 1
        if np.sum(a_Weights) != 1:
            raise ValueError(f"a_Weights must equal 1, it currently equals {np.sum(a_Weights)}")
        # Check that we have no negative weights
        for i in range(0, len(a_Weights)):
            f_Weight = a_Weights[i]
            if f_Weight < 0:
                raise ValueError(f"You have provided a negative weight of {f_Weight} at index {i} of your a_Weights")
        return a_Weights

    def ValidateData(self, a_Data):
        # We need at least as many data-points as many weights we have
        if len(a_Data) < len(self.a_Weights):
            raise ValueError(f"You have provided more weights ({len(self.a_Weights)}) than you have data points ({len(a_Data)})")
        for i in range(0, len(a_Data)):
            a_Data[i] = int(a_Data[i].replace("\n", ""))
        return np.array(a_Data)

    # This function applies itself on a provided set of data starting at the end of the signal backwards
    # The notable difference between this and ForwardpropogateFilter is that this filter averages values
    #   with the preceeding raw values, where as ForwardPropogateFilter 
    def BackPropogateFilter(self):
        if VERBOSE:
            print(f"Filtering Signal {self.a_Data}")
        a_ResultSignal = np.zeros(len(self.a_Data))
        # We need to iterate from the back forward
        for n in range(len(self.a_Data)-1, -1, -1):
            if VERBOSE:
                print(f"\nStarting at index: {n} with a value of {self.a_Data[n]}")
            # Starting at index n, we multiply X_n by it's weight, which is the first object in a_Weights
            i_AveragedData = self.a_Weights[0]*self.a_Data[n]
            if VERBOSE:
                print(f"Data point X_n = {self.a_Data[n]} weighted by a factor of {self.a_Weights[0]}, yields {i_AveragedData}")
            # Depending on how many weights we have, we multiply the preceding ith number by the ith object in a_Weights
            for i in range(1, len(self.a_Weights)):
                # For each weight, we add the weighted value to our total
                if n-i >= 0:
                    i_AveragedData += self.a_Weights[i] * self.a_Data[n-i]
                    if VERBOSE:
                        print(f"Data point X_n = {self.a_Data[n-i]} weighted by a factor of {self.a_Weights[i]}, yiekds {i_AveragedData}")
           
            a_ResultSignal[n] = i_AveragedData
        # Return the newly filtered array
        return a_ResultSignal

    # Comments for this function can be inferred by the previous function
    def FrontPropogateFilter(self):
        if VERBOSE:
            print(f"Filtering Signal {self.a_Data}")
        a_ResultSignal = np.zeros(len(self.a_Data))
        # We need to iterate from front to back
        for n in range(0, len(self.a_Data)):
            if VERBOSE:
                print(f"\nStarting at index {n} with a value of {self.a_Data[n]}")
            i_AveragedData = self.a_Weights[0]*self.a_Data[n]
            if VERBOSE:
                print(f"Data point X_n = {self.a_Data[n]} weights by a factor of {self.a_Weights[0]}, yields {i_AveragedData}")
            for i in range(1, len(self.a_Weights)):
                if n-i > 0:
                    i_AveragedData += self.a_Weights[i] * self.a_Data[n-i]
                    if VERBOSE:
                        print(f"Data point X_n = {self.a_Data[n-i]} weighted by a factor of {self.a_Weights[i]}, yiekds {i_AveragedData}")

            a_ResultSignal[n] = i_AveragedData
        return a_ResultSignal
    
    def Process(self, i_Data):
        i_AveragedValue = self.a_Weights[0] * i_Data
        for i in range(1, len(self.a_Weights)):
            if len(self.a_Data) - i > 0:
                i_AveragedValue += self.a_Weights[i] * self.a_Data[-i]
        self.a_Data.append(i_AveragedValue)