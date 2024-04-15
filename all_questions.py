import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.08
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = 0.424

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.53
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'No'

    # type: explain_string
    answers['Explain'] = "Alan's theory on coin flips to predict the stock market is flawed on two fronts. Coin flips are independent events so a sequence of flips cannot be considered a predictive model as there is no predictive indication. Also, the economy cannot be predicted by a coin flip as the two are unrelated." 
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = 0.1

    # type: eval_float
    answers['(a) C2-TPR'] = 0.2

    # type: eval_float
    answers['(a) C1-FPR'] = 0.1

    # type: eval_float
    answers['(a) C2-FPR'] = 0.2

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = 'no'

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "While C2 has a higher TPR, it also has an equally high FPR. It is predicting more positives at the risk at having more false positives. The proportion of TP to FP is the same between the two classifiers."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = 'TPR/FPR'

    # type: explain_string
    answers['(c) explain'] = "Precision/Recall does not account for the difference of TP to FP. Recall is increased but so is the amount of FP. TPR/FPR is more suitable as it provides a metric to showcase each classifier's random guessing component."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = 'C2'

    # type: explain_string
    answers['(i) Best classifier, explain'] = 'Both classifiers have the same precision but C2 has a higher Recall/TPR, F-1 Measure at the cost of a high FPR. This shows that C2 is better at identifying positives and false positives are not detrimental. If false positives pose a risk then C1 would be better.'

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = 'precision-recall-F1-Measure'

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = 'Precision, Recall, F-1 Measure provides a more in depth view of performance as it shows a proportional comparision of the two classifiers.'

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = 'C3'

    # type: explain_string
    answers['(iii) best classifier, explain'] = 'C3 is essentially a better C1. It has a higher precision (higher than C2 as well), F-1 measure and Recall, while still keeping the low FPR of C1. While these metrics are not as good as C2, the tradeoff of such a high FPR in my opinion is worth it.' 
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = 0.1

    # type: eval_float
    answers['(a) recall for C0'] = 0.1

    # type: eval_float
    answers['(b) F-measure of C0'] = 

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 0.533,
        'precision': 0.615,
        'F-measure': 0.571,
        'accuracy': 0.88
    }
    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = 'F-measure combines precision and recall in a single statistic, making it the clear choice for best metric between the three. Due to imbalanced classes, accuracy can be skewed heavily as it only accounts for the total number of mistakes rather than the type of mistake (doesnt account for the discrepency between FP and FN in context).
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = 'T1'

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = 'T2'

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = 'TPR/FPR'
    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = 'Given the context of the situation, failing to diagnose someone with cancer seems like a bigger deal than falsely diagnosing someone. Therefore, TPR/FPR is the most appropriate metric to be used.'


    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = 'Email-spam detection would be an appropriate situation to use F-measure rather than TPR/FPR as FP and FN are less dire and it does not end someones life if they get a spam email.'
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
