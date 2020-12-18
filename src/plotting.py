# Import necessary packages here
from typing import List
import warnings
from matplotlib import rc, pyplot as plt
# ============================================================================
# ============================================================================
# Date:    December 18, 2020
# Purpose: This file contains classes and functions necessary for
#          plotting.

# Source Code Metadata
__author__ = "Jonathan A. Webb"
__copyright__ = "Copyright 2020, Jon Webb Inc."
__version__ = "1.0"
# ============================================================================
# ============================================================================


def two_d_line_matplot(x_data: List[List[float]], y_data: List[List[float]],
                       line_colors: List[str], line_style: List[str],
                       line_weight: List[str], x_label: str, y_label: str,
                       dat_labels: List[str], label_pos: str, x_scale: str = 'LIN',
                       y_scale: str = 'LIN', plot_name: str = 'NULL',
                       save: bool = False, label_font_size: int = 18,
                       tick_font_size: int = 18, style_name: str = 'default') -> None:
    """

    :param x_data: A list of lists, where the inner lists contain data points
                   for the x-axis
    :param y_data: A list of lists, where the inner lists contain data points
                   for the y-axis
    :param line_colors: A list of line colors ,one for each curve.
                        Acceptable line color indicators can be found in documentation
                        for
                        `matplotlib colors <https://matplotlib.org/3.1.0/gallery/color/named_colors.html>`_.
    :param line_style: A list of line styles, one for each curve.  Acceptable line
                       styles can be found in documentation for
                       `matplotlib style <https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html>`_.
    :param line_weight: A list of line weights, one for each curve.
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param dat_labels: A list of labels, one for each curve
    :param label_pos: The position of the label in the plot, examples might be
                      ``upper left``, ``lower right``.
    :param x_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param y_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param save: True or False, defaulted to False
    :param label_font_size: The font size for plot labels, defaulted to 18
    :param tick_font_size: The tick font size, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                       found at
                       `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                       defaulted to ``default``
    :return None:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets.  This function will only produce line plots and
    not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > x_dat = np.linspace(0, 10, 15)
       > y1_dat = x_dat
       > y2_dat = x_dat ** 2.0
       > y3_dat = x_dat ** 3.0
       > x_list = [x_dat, x_dat, x_dat]
       > y_list = [y1_dat, y2_dat, y3_dat]
       > colors = ['red', 'blue', 'black']
       > line_style = ['-', '-', '--']
       > labels = ['linear', 'squared', 'cubed']
       > weight = [1, 2, 3]
       > two_d_line_matplot(x_list, y_list, colors, line_style, weight, 'x-data',
                            'y-data', labels, 'upper left')

    .. image:: line_plot.eps
       :scale: 90%
       :align: center

    """
    # Error checking and warnings
    if save and plot_name == 'NULL':
        warnings.warn('if save is True then plot name cannot be NULL')
    if len(x_data) != len(y_data):
        warnings.warn('length of x list of lists is not the same as y list of lists, plot not printed')
        return
    if len(line_colors) != len(x_data):
        warnings.warn('line colors list not the same length as data lists, plot not printed')
        return
    if len(line_style) != len(x_data):
        warnings.warn('line_style list not the same length as data lists, plot not printed')
        return
    if len(line_weight) != len(x_data):
        warnings.warn('line_weight list not the same length as data lists, plot not printed')
        return
    if y_scale != 'LOG' and y_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')
    if x_scale != 'LOG' and x_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')

    # begin plot
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    fig, td_plot = plt.subplots()
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    td_plot.set_xlabel(x_label, fontsize=label_font_size)
    td_plot.set_ylabel(y_label, fontsize=label_font_size)
    if x_scale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if y_scale.upper() == 'LOG':
        td_plot.set_yscale('log')

    for i in range(len(line_colors)):
        td_plot.plot(x_data[i], y_data[i], color=line_colors[i],
                     label=dat_labels[i], linewidth=line_weight[i],
                     linestyle=line_style[i])

    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
# ----------------------------------------------------------------------------


def two_d_scatter_matplot(x_data: List[List[float]], y_data: List[List[float]],
                          marker_colors: List[str], marker_style: List[str],
                          x_label: str, y_label: str, dat_labels: List[str],
                          label_pos: str, x_scale: str = 'LIN',
                          y_scale: str = 'LIN', plot_name: str = 'NULL',
                          save: bool = False, label_font_size: int = 18,
                          tick_font_size: int = 18, style_name: str = 'default') -> None:
    """

    :param x_data: A list of lists, where the inner lists contain data points
                   for the x-axis
    :param y_data: A list of lists, where the inner lists contain data points
                   for the y-axis
    :param marker_colors: A list of line colors ,one for each curve.
                          Acceptable line color indicators can be found in documentation
                          for `matplotlib colors <https://matplotlib.org/3.1.0/gallery/color/named_colors.html>`_.
    :param marker_style: A list of line styles, one for each curve.  Acceptable line
                         styles can be found in documentation for `matplotlib style`_.
    :param x_label: The label for the x-axis
    :param y_label: The label for the y-axis
    :param dat_labels: A list of labels, one for each curve
    :param label_pos: The position of the label in the plot, examples might be
                      ``upper left``, ``lower right``
    :param x_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param y_scale: LOG or LIN for logarithmic or linear, defaulted to LIN
    :param plot_name: The plot name and path-link, if the user wants to save the
                      plot.  If not, the variable is defaulted to ``NULL``
    :param save: True or False, defaulted to False
    :param label_font_size: The font size for plot labels, defaulted to 18
    :param tick_font_size: The tick font size, defaulted to 18
    :param style_name: The plot style to be used.  Acceptable styles can be
                       found at
                       `matplotlib styles <https://matplotlib.org/3.2.1/gallery/style_sheets/style_sheets_reference.html>`_.
                       defaulted to ``default``
    :return None:

    This function utilizes the matplotlib
    `subplots <https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplots.html>`_ functionality
    to produce single plots of one or multiple data sets.  This function will only produce line plots and
    not scatter plots or a combination of both.  The function can be used in the following manner;

    .. code-block:: python

       > x_dat = np.linspace(0, 10, 15)
       > y1_dat = x_dat
       > y2_dat = x_dat ** 2.0
       > y3_dat = x_dat ** 3.0
       > x_list = [x_dat, x_dat, x_dat]
       > y_list = [y1_dat, y2_dat, y3_dat]
       > colors = ['red', 'blue', 'black']
       > line_style = ['-', '-', '--']
       > labels = ['linear', 'squared', 'cubed']
       > weight = [1, 2, 3]
       > two_d_line_matplot(x_list, y_list, colors, line_style, weight, 'x-data',
                           'y-data', labels, 'upper left')

    .. image:: scatter_plot.eps
       :align: center

    """
    # Error checking and warnings
    if save and plot_name == 'NULL':
        warnings.warn('if save is True then plot name cannot be NULL')
    if len(x_data) != len(y_data):
        warnings.warn('length of x list of lists is not the same as y list of lists, plot not printed')
        return
    if len(marker_colors) != len(x_data):
        warnings.warn('line colors list not the same length as data lists, plot not printed')
        return
    if len(marker_style) != len(x_data):
        warnings.warn('line_style list not the same length as data lists, plot not printed')
        return
    if y_scale != 'LOG' and y_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')
    if x_scale != 'LOG' and x_scale != 'LIN':
        warnings.warn('y_scale must be set to LOG or LIN')

    # begin plot
    plt.rcParams.update({'figure.autolayout': True})
    plt.style.use(style_name)
    fig, td_plot = plt.subplots()
    rc('xtick', labelsize=tick_font_size)
    rc('ytick', labelsize=tick_font_size)
    td_plot.set_xlabel(x_label, fontsize=label_font_size)
    td_plot.set_ylabel(y_label, fontsize=label_font_size)
    if x_scale.upper() == 'LOG':
        td_plot.set_xscale('log')
    if y_scale.upper() == 'LOG':
        td_plot.set_yscale('log')

    for i in range(len(marker_colors)):
        td_plot.plot(x_data[i], y_data[i], color=marker_colors[i],
                     label=dat_labels[i], marker=marker_style[i],
                     linestyle=' ')

    plt.legend(loc=label_pos)
    if not save:
        plt.show()
    else:
        plt.savefig(plot_name)
# ============================================================================
# ============================================================================
# eof
# TODO Add combined scatter-line plot
# TODO Add histogram plot
# TODO Add date plot
