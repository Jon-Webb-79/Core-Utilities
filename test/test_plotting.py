# Import necessary packages here
import numpy as np
import pandas as pd
import sys
import os
import platform
#import yfinance as yf
sys.path.insert(0, os.path.abspath('../src'))
from core_utilities.plotting import two_d_line_matplot, two_d_scatter_matplot
from core_utilities.plotting import two_d_scatter_line_matplot, one_d_histogram_plot
from core_utilities.plotting import text_date_plot, MatPlotDataFrame
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


def test_date_plot():
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/date.eps'
    else:
        plt_name = r'..\data\test\date.eps'
    # Use stock data for example
    tickers = ['AAPL', 'WMT']
    data = yf.download(tickers, '2015-1-1')['Adj Close']
    # transform Timestamps to string
    dates = list(data.index.strftime('%Y-%m-%d'))
    date_list = [dates, dates]
    y_list = [list(data[tickers[0]]), list(data[tickers[1]])]
    colors = ['red', 'green']
    line_style = ['-', '-']
    weight = [1.0, 1.0]
    text_date_plot(date_list, y_list, colors, line_style, weight, 'Date',
                   '$', tickers, 'upper left', save=True, plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ----------------------------------------------------------------------------


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
# ================================================================================
# ================================================================================
# Test MatPlotDataFrame


def test_matplot_scatter_plot_parse_column():
    plat = platform.system()
    if plat == 'Darwin':
        plt_name = '../data/test/hist1.eps'
    else:
        plt_name = r'..\data\test\hist1.eps'
    length = 20
    x = np.linspace(0, 20, num=20)
    linear = x
    squared = x ** 2.0
    lin = np.repeat('linear', 20)
    sq = np.repeat('squared', 20)
   
    # Combine arrays into one
    x = np.hstack((x, x))
    y = np.hstack((linear, squared))
    power = np.hstack((lin, sq))

    # Create dataframe
    dictionary = {'x': x, 'y': y, 'power': power}
    df = pd.DataFrame(dictionary)

    # Plot data
    obj = MatPlotDataFrame(df)

    parsing_header = 'power'
    column_values = ['linear', 'squared']
    obj.scatter_plot_parse_column('x', 'y', parsing_header, column_values, 
                                  x_label='x-axis', y_label='y-axis', title='Test', 
                                  style_name='default',marker_colors=['red', 'green'], 
                                  fill_alpha=0.7, marker_style=['o', '^'], 
                                  label_pos='upper left', grid=True, save=True,
                                  plot_name=plt_name)
    assert os.path.isfile(plt_name)
    if os.path.isfile(plt_name):
        os.remove(plt_name)
# ================================================================================
# ================================================================================
# eof
