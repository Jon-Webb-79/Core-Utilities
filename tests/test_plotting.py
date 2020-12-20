# Import necessary packages here
import numpy as np
import sys
import os
import platform
import random
sys.path.insert(0, os.path.abspath('../src'))
from plotting import two_d_line_matplot, two_d_scatter_matplot
from plotting import two_d_scatter_line_matplot, one_d_histogram_plot
# ============================================================================
# ============================================================================
# Date:    December 18, 2020
# Purpose: This file contains functions that tests functions and classes
#          in the plotting.py file

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ============================================================================
# ============================================================================
# Test plotting routines in plotting.py


def test_two_d_line_plot():
    """

    This function tests the two_d_line_matplot function to ensure it
    produces a plot
    """
    x_dat = np.linspace(0, 10, 15)
    y1_dat = x_dat
    y2_dat = x_dat ** 2.0
    y3_dat = x_dat ** 3.0
    x_list = [x_dat, x_dat, x_dat]
    y_list = [y1_dat, y2_dat, y3_dat]
    colors = ['red', 'blue', 'black']
    line_style = ['-', '-', '--']
    labels = ['linear', 'squared', 'cubed']
    weight = [1, 2, 3]
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/test.png'
    else:
        plt_name = r'..\data\test\test.png'
    two_d_line_matplot(x_list, y_list, colors, line_style, weight, 'x-data',
                       'y-data', labels, 'upper left', save=True,
                       plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ----------------------------------------------------------------------------


def test_two_d_scatter_matplot():
    x_dat = np.linspace(0, 10, 15)
    y1_dat = x_dat
    y2_dat = x_dat ** 2.0
    y3_dat = x_dat ** 3.0
    x_list = [x_dat, x_dat, x_dat]
    y_list = [y1_dat, y2_dat, y3_dat]
    colors = ['red', 'blue', 'black']
    marker_style = ['^', 'o', 'd']
    labels = ['linear', 'squared', 'cubed']
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/test.eps'
    else:
        plt_name = r'..\data\test\test.eps'
    two_d_scatter_matplot(x_list, y_list, colors, marker_style, 'x-data',
                          'y-data', labels, 'upper left', save=True,
                          plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ----------------------------------------------------------------------------


def test_two_d_scatter_line_matplot():
    """

    This function tests the two_d_scatter_line_matplot function to determine if
    it generates an output file
    """
    x_dat = np.linspace(0, 10, 15)
    y1_dat = x_dat
    y2_dat = x_dat ** 2.0
    y3_dat = x_dat ** 3.0
    x_list = [x_dat, x_dat, x_dat]
    y_list = [y1_dat, y2_dat, y3_dat]
    colors = ['red', 'blue', 'black']
    line_style = ['-', '-', '--']
    labels = ['linear', 'squared', 'cubed']
    weight = [1, 2, 3]
    marker_style = ['^', 'o', 'd']
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/line_mark.eps'
    else:
        plt_name = r'..\data\test\line_mark.eps'
    two_d_scatter_line_matplot(x_list, y_list, colors, marker_style,
                               line_style, weight, 'x-axis', 'y-axis',
                               labels, 'upper left', save=True, plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ----------------------------------------------------------------------------


def test_histogram_plot():
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/hist1.eps'
    else:
        plt_name = r'..\data\test\hist1.eps'
    np.random.seed(19680801)
    x = np.random.normal(15.0, 3.0, 1000)
    y = np.random.normal(20.0, 3.0, 1000)
    data = [x, y]
    labels = ['one', 'two']
    colors = ['blue', 'green']
    edge_colors = ['black', 'black']
    alpha = [0.9, 0.4]
    x_label = 'x-axis'
    y_label = 'y-axis'
    one_d_histogram_plot(data, labels, x_label, y_label, colors, edge_colors,
                         alpha, 'upper left', num_bins=50, save=True,
                         plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ============================================================================
# ============================================================================
# eof