#%%
import pandas as pd
import os
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv(os.path.expanduser("~/development/git/python/jeopardy_starting/jeopardy.csv"))

jeopardy.columns = ['show_number', 'air_date', 'round', 'category', 'value', 'question', 'answer']

#jeopardy = jeopardy.head(10)

#jeopardy_filtered = lambda x: True for x in jeopardy.question if all(filter_list) 

def filter_questions_by_keyword(data, words):
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    return data.loc[data['question'].apply(filter)]

filtered = filter_questions_by_keyword(jeopardy, ['King', 'England']).reset_index()

def scrub_values(data):
    if data.loc[data['value']] != 'None' & "," in data.loc[data['value']]:
        no_comma = data.loc[data['value'].replace(',', '')]
        return no_comma[1:]
    elif data.loc[data['value']] != 'None':
        return data.loc[data['value']][1:]
    else:
        return 'None'

scrubbed_values = scrub_values(jeopardy).reset_index()

jeopardy['float_values'] = pd.to_numeric(scrubbed_values, errors='coerce')

print(scrubbed_values)

# %%


# %%
