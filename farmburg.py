#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 06:18:10 2018

@author: mark
"""

import pandas as pd
import numpy as np
df = pd.read_csv('clicks.csv')
df['is_purchase'] = df.click_day.apply(lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase')
print(df.head(10))