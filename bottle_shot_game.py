# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:30:57 2021

@author: Sanjit_2021cs07
"""

import streamlit as st
import codecs
import streamlit.components.v1 as stc

clac_file = codecs.open('sanjitGame.html','r')
page = clac_file.read()
stc.html(page,width=900,height=650,scrolling=True)
