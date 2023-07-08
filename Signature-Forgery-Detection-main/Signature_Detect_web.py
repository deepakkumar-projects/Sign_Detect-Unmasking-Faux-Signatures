import streamlit as st
import os
# import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.filters import threshold_otsu
import numpy as np
import Signature_detect


def main():
    st.set_page_config(page_title="Signature Forgery Detection")
    st.header("Signature Forgery Detection")
    png = st.file_uploader("Upload Your PDF ", type="png")
    if png is not None:
        png1 = png

if __name__ == '__main__':
    main()