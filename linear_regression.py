#!/usr/bin/env python
# coding: utf-8

# In[34]:


def my_sum(arr):
    total = 0
    for a in arr:
        total += a
    return total

def my_mean(arr):
    return my_sum(arr)/len(arr)

def my_var(arr):
    mean_arr = my_mean(arr)
    tot = 0
    for a in arr:
        tot += (a-mean_arr)**2
    return tot

def my_covar(arr_x, arr_y):
    covar = 0
    mean_x = my_mean(arr_x)
    mean_y = my_mean(arr_y)
    for i in range(len(arr_x)):
        covar += (arr_x[i]-mean_x)*(arr_y[i]-mean_y)
    return covar

def find_coeffs(x, y):
    eqn = 'y = ax + b'
    a = my_covar(x, y)/my_var(x)
    b = my_mean(y) - a * my_mean(x)
    return [a, b]
    
def make_predictions(x, y, x_for_prediction):
    predicted_y = []
    m, c = find_coeffs(x, y)
    for a in x:
        predicted_y.append(m*a+c)
    return predicted_y
    
def main():
    x = [1, 2, 4, 3, 5]
    y = [1, 3, 3, 2, 5]
    x_pred = [100]
    print(make_predictions(x, y, x_pred))
    
if __name__== "__main__":
    main()
# given y = ax + b
# a = covar(x, y) / var(x)
# b = my_mean(y) - a * my_mean(x)


# In[ ]:




