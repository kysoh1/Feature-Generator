import pandas as pd
from sklearn import preprocessing as p
import numpy as np
import math
from trans_functions import get_trans_functions_1, get_trans_functions_2, get_trans_functions_3, get_trans_functions_4, get_trans_functions_5

def main():
    # Load tabular data (excel)
    df = pd.read_excel('original_data.xlsx')
    # Dimensions of square image
    length = 30

    # features : Original features in excel sheet
    # row_data : All samples loaded as an array
    # feature_limit: Number of features to generate for each pixel in a square image
    features = df.columns.values[1:]
    row_data = collect_rows(df)
    feature_limit = length * length
    '''
    x = df.values
    samples = x[:,0]
    data = x[:,1:]
    min_max_scaler = p.MinMaxScaler()
    data_scaled = min_max_scaler.fit_transform(data)
    samples = pd.DataFrame(samples, columns=['?'])
    data_scaled = pd.DataFrame(data_scaled, columns=features)
    df = pd.concat([samples, data_scaled], axis=1, ignore_index=False)
    '''
    # Generate features using algebraic transformations between one or more original features
    df = generate_features_1(df, features, row_data, feature_limit)
    df = generate_features_2_sensor(df, features, row_data, feature_limit)
    df = generate_features_3_sensor(df, features, row_data, feature_limit)
    df = generate_features_4_sensor(df, features, row_data, feature_limit)
    df = generate_features_5_sensor(df, features, row_data, feature_limit)
    
    #df = generate_features_1(df, features, row_data, feature_limit)
    #df = generate_features_2(df, features, row_data, feature_limit)
    #df = generate_features_3(df, features, row_data, feature_limit)
    #df = generate_features_4(df, features, row_data, feature_limit)
    
    print('\nSaving data frame to file.')
    df.to_csv('new_data_30.txt', index=False, sep = '\t')

# FEATURE GENERATION

def collect_rows(df):
    row_data = []
    for i in range(0, len(df.index)):
        row = df.iloc[i].to_numpy()[1:]
        row_data.append(row)
    
    return row_data

# Use single feature transformation functions

def generate_features_1(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_1():
        for i in range(0, len(features)):
            if num_features < feature_limit:
                new_col_data = []
                title = features[i] + ',' + transform_func.__name__
                
                try:
                    for row in row_data:
                        new_col_data.append(transform_func(row[i]))
                except:
                    print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                else:  
                    new_col_data = np.array(new_col_data)
                    new_col_data = np.reshape(new_col_data, (-1, 1))
                    new_col_data = min_max_scaler.fit_transform(new_col_data)
                    new_col_data = new_col_data.ravel()
                    new_feature_data[title] = new_col_data
                    num_features = num_features + 1
            else:
                new_df = pd.DataFrame(new_feature_data)
                return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine two features, using double feature transformation functions

def generate_features_2(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_2():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                if num_features < feature_limit:
                    new_col_data = []
                    title = features[i] + ',' + features[j] + ',' +  transform_func.__name__
                
                    try:
                        for row in row_data:
                            new_col_data.append(transform_func(row[i], row[j]))
                    except:
                        print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                    else:  
                        new_col_data = np.array(new_col_data)
                        new_col_data = np.reshape(new_col_data, (-1, 1))
                        new_col_data = min_max_scaler.fit_transform(new_col_data)
                        new_col_data = new_col_data.ravel()
                        new_feature_data[title] = new_col_data
                        num_features = num_features + 1
                else:
                    new_df = pd.DataFrame(new_feature_data)
                    return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 3 features, using triple feature transformation functions

def generate_features_3(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_3():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                for k in range(j + 1, len(features)):
                    if num_features < feature_limit:
                        new_col_data = []
                        title = features[i] + ',' + features[j] + ',' + features[k] + ',' + transform_func.__name__ 
                
                        try:
                            for row in row_data:
                                new_col_data.append(transform_func(row[i], row[j], row[k]))
                        except:
                            print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                        else:  
                            new_col_data = np.array(new_col_data)
                            new_col_data = np.reshape(new_col_data, (-1, 1))
                            new_col_data = min_max_scaler.fit_transform(new_col_data)
                            new_col_data = new_col_data.ravel()
                            new_feature_data[title] = new_col_data
                            num_features = num_features + 1
                    else:
                        new_df = pd.DataFrame(new_feature_data)
                        return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 4 features, using quadruple feature transformation functions

def generate_features_4(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_4():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                for k in range(j + 1, len(features)):
                    for l in range(k + 1, len(features)):
                        if num_features < feature_limit:
                            new_col_data = []
                            title = features[i] + ',' + features[j] + ',' + features[k] + ',' + features[l] + ',' + transform_func.__name__ 
                
                            try:
                                for row in row_data:
                                    new_col_data.append(transform_func(row[i], row[j], row[k], row[l]))
                            except:
                                print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                            else:
                                new_col_data = np.array(new_col_data)
                                new_col_data = np.reshape(new_col_data, (-1, 1))
                                new_col_data = min_max_scaler.fit_transform(new_col_data) 
                                new_col_data = new_col_data.ravel()
                                new_feature_data[title] = new_col_data
                                num_features = num_features + 1
                        else:
                            new_df = pd.DataFrame(new_feature_data)
                            return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 2 features, using double feature transformation functions, include sensor_dist

def generate_features_2_sensor(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_2():
        for i in range(0, len(features)):
            if num_features < feature_limit:
                new_col_data = []
                title = features[i] + ',' + features[len(features) - 1] + ',' + transform_func.__name__
                
                try:
                    for row in row_data:
                        new_col_data.append(transform_func(row[i], row[len(features) - 1]))
                except:
                    print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                else:
                    new_col_data = np.array(new_col_data)
                    new_col_data = np.reshape(new_col_data, (-1, 1))
                    new_col_data = min_max_scaler.fit_transform(new_col_data)
                    new_col_data = new_col_data.ravel()
                    new_feature_data[title] = new_col_data
                    num_features = num_features + 1
            else:
                new_df = pd.DataFrame(new_feature_data)
                return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 3 features, using triple feature transformation functions, include sensor_dist

def generate_features_3_sensor(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_3():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                if num_features < feature_limit:
                    new_col_data = []
                    title = features[i] + ',' + features[j] + ',' + features[len(features) - 1] + ',' + transform_func.__name__
                
                    try:
                        for row in row_data:
                            new_col_data.append(transform_func(row[i], row[j], row[len(features) - 1]))
                    except:
                        print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                    else:
                        new_col_data = np.array(new_col_data)
                        new_col_data = np.reshape(new_col_data, (-1, 1))
                        new_col_data = min_max_scaler.fit_transform(new_col_data)  
                        new_col_data = new_col_data.ravel()
                        new_feature_data[title] = new_col_data
                        num_features = num_features + 1
                else:
                    new_df = pd.DataFrame(new_feature_data)
                    return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 4 features, using quadruple feature transformation functions, include sensor_dist

def generate_features_4_sensor(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_4():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                for k in range(j + 1, len(features)):
                    if num_features < feature_limit:
                        new_col_data = []
                        title = features[i] + ',' + features[j] + ',' + features[k] + ',' + features[len(features) - 1] + ',' + transform_func.__name__ 
                
                        try:
                            for row in row_data:
                                new_col_data.append(transform_func(row[i], row[j], row[k], row[len(features) - 1]))
                        except:
                            print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                        else:
                            new_col_data = np.array(new_col_data)
                            new_col_data = np.reshape(new_col_data, (-1, 1))
                            new_col_data = min_max_scaler.fit_transform(new_col_data)
                            new_col_data = new_col_data.ravel()
                            new_feature_data[title] = new_col_data
                            num_features = num_features + 1
                    else:
                        new_df = pd.DataFrame(new_feature_data)
                        return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

# Combine 5 features, using pentuple feature transformation functions

def generate_features_5_sensor(df, features, row_data, feature_limit):
    num_features = df.shape[1] - 1
    new_feature_data = {}
    min_max_scaler = p.MinMaxScaler()
    for transform_func in get_trans_functions_5():
        for i in range(0, len(features)):
            for j in range(i + 1, len(features)):
                for k in range(j + 1, len(features)):
                    for l in range(k + 1, len(features)):
                        if num_features < feature_limit:
                            new_col_data = []
                            title = features[i] + ',' + features[j] + ',' + features[k] + ',' + features[l] + ',' +features[len(features) - 1] + ',' + transform_func.__name__ 
                
                            try:
                                for row in row_data:
                                    new_col_data.append(transform_func(row[i], row[j], row[k], row[l], row[len(features) - 1]))
                            except:
                                print('Unable to generate feature ' + title + ' using ' + transform_func.__name__ + ' function.')
                            else:
                                new_col_data = np.array(new_col_data)
                                new_col_data = np.reshape(new_col_data, (-1, 1))
                                new_col_data = min_max_scaler.fit_transform(new_col_data) 
                                new_col_data = new_col_data.ravel()
                                new_feature_data[title] = new_col_data
                                num_features = num_features + 1
                        else:
                            new_df = pd.DataFrame(new_feature_data)
                            return pd.concat([df, new_df], axis=1, ignore_index=False)

    new_df = pd.DataFrame(new_feature_data)
    return pd.concat([df, new_df], axis=1, ignore_index=False)

if __name__ == "__main__":
    main()